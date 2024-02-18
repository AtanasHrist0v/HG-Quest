from .item import Item

class Weapon(Item):
    def __init__(self, name, surf, rect, damage, aoe, range):
        super().__init__(name, surf, rect)
        self.damage = damage
        self.aoe = aoe
        self.range = range