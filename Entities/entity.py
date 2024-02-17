class Entity:
    def __init__(self, name, health, position):
        self.name = name
        self.health = health
        self.position = position
        
    def alive(self):
        return self.health > 0
    
    def move(self, movement_vector):
        self.position = tuple(map(sum, zip(self.position, movement_vector)))
        
    def attack(self, target):
        pass
    
    def take_damage(self, damage):
        pass