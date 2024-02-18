from .item import Item

class PassiveItem(Item):
    def __init__(self, name, rect):
        super().__init__(name, rect)