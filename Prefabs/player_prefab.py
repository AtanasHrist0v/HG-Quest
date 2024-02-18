import pygame
from constants import DISPLAY_CENTER
from Entities.player import Player
from Prefabs.excalibur_prefab import excalibur


player_surf = pygame.image.load('Assets/player.png').convert_alpha()
player_rect = player_surf.get_rect(center = DISPLAY_CENTER)
player = Player('Player', 
                Player.MAX_HEALTH, 
                pygame.Vector2(DISPLAY_CENTER), 
                300, 
                player_surf, 
                player_rect, 
                0, 
                excalibur, 
                None, 
                [])