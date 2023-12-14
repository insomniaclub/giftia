from typing import List

from message import BaseMessage
from memory import BaseMemory


class ChatBuffer(BaseMemory):
    def __init__(self) -> None:
        super().__init__()
        self.buffer: List[BaseMessage] = []

    def load(self) -> List[BaseMessage]:
        return self.buffer

    def store(self, messages: List[BaseMessage]) -> None:
        self.buffer.extend(messages)
