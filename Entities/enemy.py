from .entity import Entity

class Enemy(Entity):


    def __init__(self, name, health, position, speed, surf, rect):
        super().__init__(name, health, position, speed, surf, rect)


    def attack(self, target):
        target.take_damage(self.weapon.damage)


    def take_damage(self, damage):
        self.health -= damage


    def move(self, target, dt):
        movement_vector = (self.rect.center - target.rect.center) * self.speed * dt
        super().move(movement_vector)