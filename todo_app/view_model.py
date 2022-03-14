from todo_app.item import Item


class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def todo_items(self):
        output = []
        for item in self._items:
            if item.status == "To Do":
                output.append(item)
        return output

    @property
    def doing_items(self):
        output = []
        for item in self._items:
            if item.status == "Doing":
                output.append(item)
        return output

    @property
    def done_items(self):
        output = []
        for item in self._items:
            if item.status == "Done":
                output.append(item)
        return output