from .item import Item

class Consumable(Item):
    def __init__(self, name, rect):
        super().__init__(name, rect)