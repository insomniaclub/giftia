from typing import Literal


class BaseMessage:

    def __init__(self, content: str, type: str = Literal['system', 'human', 'ai']) -> None:
        self.content = content
        self.type = type
