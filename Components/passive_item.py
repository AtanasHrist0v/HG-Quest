from .item import Item

class PassiveItem(Item):
    def __init__(self, name, surf, rect):
        super().__init__(name, surf, rect)