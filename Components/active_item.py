from .item import Item

class ActiveItem(Item):
    def __init__(self, name, rect):
        super().__init__(name, rect)