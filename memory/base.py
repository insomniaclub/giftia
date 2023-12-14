from abc import ABC, abstractmethod
from typing import List

from message import BaseMessage


class BaseMemory(ABC):
    def __init__(self) -> None:
        super().__init__()
        pass

    @abstractmethod
    def load(self) -> List[BaseMessage]:
        raise NotImplementedError

    @abstractmethod
    def store(self, messages: List[BaseMessage]) -> None:
        raise NotImplementedError
