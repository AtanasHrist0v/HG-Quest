from .item import Item


class Consumable(Item):
    def __init__(self, name, surf, rect):
        super().__init__(name, surf, rect)