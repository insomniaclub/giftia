from argparse import Namespace
from typing import List

import torch
from transformers import AutoModel, AutoTokenizer

from giftia.embedding import Embedding
from giftia.util.device import get_torch_device
from giftia.util.text import detect_language


_LUOTUO_MODEL_NAMES = {
    'zh': 'silk-road/luotuo-bert-medium',
    'en': 'silk-road/luotuo-bert-en',
}


class LuotuoEmbedding(Embedding):
    ''' Luotuo Embedding '''

    def __init__(self) -> None:
        super().__init__()

        self.models = {}
        self.tokenizers = {}
        self.device = get_torch_device()

        for lang, model_name in _LUOTUO_MODEL_NAMES.items():
            model, tokenizer = self.load_model(model_name)
            self.models[lang] = model
            self.tokenizers[lang] = tokenizer

    def embed(self, texts: List[str]) -> List[List[float]]:
        return [embed.tolist() for embed in self.get_embeddings(texts)]

    def get_embeddings(self, texts: List[str]):
        embeddings = []
        chunk_size = 64

        for i in range(0, len(texts), chunk_size):
            max_len = i + chunk_size if i + chunk_size < len(texts) else len(texts)
            chunk_texts = texts[i: max_len if i + max_len else len(texts)]
            chunk_lang = detect_language(chunk_texts[0])  # 暂时选取每个chunk的第一条来判断

            model = self.models[chunk_lang]
            tokenizer = self.tokenizers[chunk_lang]

            # 截断
            chunk_texts = [text[:510] if len(text) > 510 else text for text in chunk_texts]

            embeddings.append(self.embedding(model, tokenizer, chunk_texts))

        return torch.cat(embeddings, dim=0)

    def embedding(self, model, tokenizer, texts):
        '''Embed search docs.'''

        inputs = tokenizer(
            texts,
            padding=True,
            truncation=False,
            return_tensors='pt',
        )
        inputs = inputs.to(self.device)
        # Extract the embeddings
        # Get the embeddings
        with torch.no_grad():
            embeddings = model(
                **inputs,
                output_hidden_states=True,
                return_dict=True,
                sent_emb=True,
            ).pooler_output
        return embeddings

    def load_model(self, model_name: str):
        model_args = Namespace(
            do_mlm=None,
            pooler_type='cls',
            temp=0.05,
            mlp_only_train=False,
            init_embeddings_model=None,
        )

        print(f'正在加载 {model_name} ... ', end='', flush=True)
        model = AutoModel.from_pretrained(
            pretrained_model_name_or_path=model_name,
            trust_remote_code=True,
            model_args=model_args,
        ).to(self.device)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        print('加载完成')

        return model, tokenizer
