from message import BaseMessage


class AIMessage(BaseMessage):
    def __init__(self, content: str) -> None:
        super().__init__(content, "ai")
