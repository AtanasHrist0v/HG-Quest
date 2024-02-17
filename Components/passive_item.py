from .item import Item

class PassiveItem(Item):
    def __init__(self, name, position):
        super().__init__(name, position)