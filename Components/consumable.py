from item import Item

class Consumable(Item):
    def __init__(self, name, position):
        super().__init__(name, position)