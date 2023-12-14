from typing import Literal

from message import BaseMessage


class SystemMessage(BaseMessage):
    def __init__(self, content: str) -> None:
        super().__init__(content, "system")
