import pygame

from Components.weapon import Weapon
from constants import DISPLAY_CENTER


excalibur = Weapon('Excalibur', None, None, 420, pygame.Rect(DISPLAY_CENTER, (100, 100)), 50)

def init():
    excalibur.surf = pygame.image.load('Assets/phat_excalibur.png').convert_alpha()
    excalibur.rect = excalibur.surf.get_rect(center = DISPLAY_CENTER)