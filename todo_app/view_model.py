class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def itemsToDo(self):
        return get_ToDo_Trello(self._items)

    @property
    def itemsDoing(self):
        return get_Doing_Trello(self._items)

    @property
    def itemsDone(self):
        return get_Done_Trello(self._items)  