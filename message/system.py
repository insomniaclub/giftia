from .message import Message


class SystemMessage(Message):
    ''' System Message '''

    def __init__(self, content: str) -> None:
        super().__init__(content, 'system')
