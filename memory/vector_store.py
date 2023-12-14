from typing import List

from message import BaseMessage


class VectorStore(BaseMessage):
    def __init__(self) -> None:
        super().__init__()
        pass

    def load(self) -> List[BaseMessage]:
        raise NotImplementedError

    def store(self, messages: List[BaseMessage]) -> None:
        raise NotImplementedError