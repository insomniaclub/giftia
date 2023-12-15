from typing import Literal


class Message:
    ''' Base Message '''

    def __init__(self, content: str, type: str = Literal['system', 'human', 'ai']) -> None:
        self.content = content
        self.type = type
