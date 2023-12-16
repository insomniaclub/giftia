from abc import ABC, abstractmethod
from typing import List


class Embedding(ABC):
    '''Interface for embedding models.'''

    @abstractmethod
    def embed(self, texts: List[str]) -> List[List[float]]:
        '''Embed search docs.'''
