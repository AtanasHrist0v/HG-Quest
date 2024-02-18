import pygame
from Entities.enemy import Enemy


dark_knight_surf = pygame.image.load('Assets/enemy_knight.png').convert_alpha()
dark_knight_rect = dark_knight_surf.get_rect()
dark_knight = Enemy('Dark Knight', 1, None, 100, dark_knight_surf, dark_knight_rect)