from .item import Item


class ActiveItem(Item):
    def __init__(self, name, surf, rect):
        super().__init__(name, surf, rect)