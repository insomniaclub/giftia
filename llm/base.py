from abc import ABC, abstractmethod
from typing import Union, Iterator, List

from message import BaseMessage


class BaseLLM(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def generate(self, messages: List[BaseMessage], stream: bool = False) -> Union[str, Iterator[str]]:
        raise NotImplementedError

    @abstractmethod
    def token_size(messages: List[BaseMessage]) -> int:
        raise NotImplementedError
