from item import Item

class Weapon(Item):
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage
        