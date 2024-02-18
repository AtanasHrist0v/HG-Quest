from pygame import Vector2
from math import isclose
from .entity import Entity


class Enemy(Entity):


    def __init__(self, name, health, position, speed, surf, rect):
        super().__init__(name, health, position, speed, surf, rect)


    def attack(self, target):
        target.take_damage(self.weapon.damage)


    def take_damage(self, damage):
        self.health -= damage


    def move(self, target, dt):
        movement_vector = Vector2(target.rect.x - self.rect.x, target.rect.y - self.rect.y)
        if isclose(movement_vector.length(), 0):
            return
        movement_vector.normalize_ip()
        movement_vector.scale_to_length(self.speed * dt)
        super().move(movement_vector)