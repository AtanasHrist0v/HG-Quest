import pygame

from Prefabs import excalibur_prefab
from constants import DISPLAY_CENTER
from Entities.player import Player


player = Player('Player', 
                Player.MAX_HEALTH, 
                pygame.Vector2(DISPLAY_CENTER), 
                300, 
                None, 
                None, 
                0, 
                excalibur_prefab.excalibur, 
                None, 
                [])


def init():
    excalibur_prefab.init()
    player.surf = pygame.image.load('Assets/player.png').convert_alpha()
    player.rect = player.surf.get_rect(center = DISPLAY_CENTER)