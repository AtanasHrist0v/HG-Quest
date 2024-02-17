from .item import Item

class Weapon(Item):
    def __init__(self, name, position, damage):
        super().__init__(name, position)
        self.damage = damage