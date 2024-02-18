class Entity:
    def __init__(self, name, health, position, speed, surf, rect):
        self.name = name
        self.health = health
        self.position = position
        self.speed = speed
        self.surf = surf
        self.rect = rect
    
    def alive(self):
        return self.health > 0
    
    def move(self, movement_vector):
        self.rect.center = tuple(map(sum, zip(self.rect.center, movement_vector)))
    
    def attack(self, target):
        pass
    
    def take_damage(self, damage):
        pass
    
    def drop(self, item):
        item.position = tuple(self.position)