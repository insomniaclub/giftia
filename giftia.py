from typing import Iterator, Union

from llm import BaseLLM, YiChat
from message import SystemMessage, HumanMessage, AIMessage
from memory import BaseMemory, ChatBuffer


class Giftia:
    def __init__(self, llm: BaseLLM, mem: BaseMemory) -> None:
        self.llm = llm
        self.mem = mem

    def chat(self, prompt: str, msg: str, stream: bool = False) -> Union[str, Iterator[str]]:
        msgs = [SystemMessage(prompt)] if prompt else []
        msgs.extend(self.mem.load())
        msgs.append(HumanMessage(msg))

        resp  =""
        for chunk in self.llm.generate(msgs, stream=stream):
            resp += chunk
            yield chunk
        
        self.mem.store([HumanMessage(msg), AIMessage(resp)])


llm = YiChat()
history = ChatBuffer()

giftia = Giftia(llm, history)

while True:
    msg = input(">>> ")
    if msg == "exit":
        break
    print("<<< ", end="", flush=True)
    for chunk in giftia.chat("你的回答要尽可能简短明了", msg, stream=True):
        print(chunk, end="", flush=True)
    print()
