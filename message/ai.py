from message import Message


class AIMessage(Message):
    ''' AI Message '''

    def __init__(self, content: str) -> None:
        super().__init__(content, 'ai')
