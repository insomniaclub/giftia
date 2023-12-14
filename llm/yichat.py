from typing import Union, Iterator, List

from llama_cpp import Llama

from message import BaseMessage

from .base import BaseLLM

_YI_34B_CHAT_GGUF_PATH = "model/yi-34b-chat.Q4_K_M.gguf"

_ROLE_CONVETOR = {
    "system": "system",
    "human": "user",
    "ai": "assistant",
}


class YiChat(BaseLLM):
    def __init__(
        self,
        model_path: str = _YI_34B_CHAT_GGUF_PATH
    ):
        super().__init__()
        self.llm = Llama(
            model_path=model_path,
            n_gpu_layers=1,
            f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
            chat_format="chatml",
            # callback_manager=callback_manager,
            echo=True,
            n_ctx=4096,
            n_batch=4096,
            verbose=True,  # Verbose is required to pass to the callback manager
        )

    def generate(self, messages: List[BaseMessage], stream: bool = False) -> Union[str, Iterator[str]]:
        msgs = [
            {
                "role": _ROLE_CONVETOR[msg.type],
                "content": msg.content
            }
            for msg in messages
        ]
        resp = self.llm.create_chat_completion(
            messages=msgs,
            stream=stream,
            stop=["<|im_end|>"],
        )

        if not stream:
            yield resp["choices"][0]["message"].get("content", "").__str__()
            return

        for part in resp:
            yield part["choices"][0]["delta"].get("content", "").__str__()

    def token_size(self, messages: List[BaseMessage]) -> int:
        str = ""
        for msg in messages:
            template = ""
            if msg.type == 'system':
                template = '<|im_start|>user\n{content}<|im_end|>'
            elif msg.type == 'human':
                template = '<|im_start|>user\n{content}<|im_end|>'
            elif msg.type == 'ai':
                template = '<|im_start|>assistant\n{content}<|im_end|>'
            else:
                raise ValueError(f"Unknown message type: {msg.type}")
            str += template.format(content=msg.content)
        return len(self.llm.tokenize(str))
