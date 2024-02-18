import pygame
from constants import DISPLAY_CENTER
from Components.weapon import Weapon


excalibur_surf = pygame.image.load('Assets/phat_excalibur.png').convert_alpha()
excalibur_rect = excalibur_surf.get_rect(center = DISPLAY_CENTER)
excalibur = Weapon('Excalibur', excalibur_surf, excalibur_rect, 420, pygame.Rect(DISPLAY_CENTER, (100, 100)), 50)