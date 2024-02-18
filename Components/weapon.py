from .item import Item

class Weapon(Item):
    def __init__(self, name, rect, damage):
        super().__init__(name, rect)
        self.damage = damage