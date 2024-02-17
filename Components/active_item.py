from .item import Item

class ActiveItem(Item):
    def __init__(self, name, position):
        super().__init__(name, position)