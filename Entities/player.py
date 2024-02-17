import entity
from Components.passive_item import PassiveItem
from Components.active_item import ActiveItem
from Components.consumable import Consumable
from Components.weapon import Weapon

class Player(entity.Entity):
    MAX_HEALTH = 6
    def __init__(self, name, health, position, speed, surf, rect, armor, weapon, active_item, passive_items):
        super().__init__(name, health, position, speed, surf, rect)
        self.armor = armor
        self.weapon = weapon
        self.active_item = active_item
        self.passive_items = passive_items
        
    def attack(self, target):
        target.take_damage(self.weapon.damage)
    
    def take_damage(self, damage):
        self.armor -= damage
        if self.armor < 0:
            self.health += self.armor
            self.armor = 0
        
    def pick_up(self, item):
        item.position = self.position
        
        if isinstance(item, Consumable):
            if item.name == 'Health' and self.health < Player.MAX_HEALTH:
                self.health += 1
            if item.name == 'Armor':
                self.armor += 1
        elif isinstance(item, Weapon):
            self.drop(self.weapon)
            self.weapon = item
        elif isinstance(item, ActiveItem):
            self.drop(self.active_item)
            self.active_item = item
        elif isinstance(item, PassiveItem):
            self.passive_items.add(item)