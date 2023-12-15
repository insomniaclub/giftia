from message import Message


class HumanMessage(Message):
    ''' Human Message '''

    def __init__(self, content: str) -> None:
        super().__init__(content, 'human')
