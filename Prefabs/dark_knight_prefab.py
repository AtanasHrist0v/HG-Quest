import pygame

from Entities.enemy import Enemy


dark_knight = Enemy('Dark Knight', 1, None, 100, None, None)

def init():
    dark_knight.surf = pygame.image.load('Assets/enemy_knight.png').convert_alpha()
    dark_knight.rect = dark_knight.surf.get_rect()