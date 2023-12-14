from abc import ABC, abstractmethod

from abc import ABC, abstractmethod


class VectorStore(ABC):
    def __init__(self) -> None:
        super().__init__()
        pass

    @abstractmethod
    def search(self, messages) -> None:
        raise NotImplementedError
