import pygame
from Components.weapon import Weapon

excalibur_surf = pygame.image.load('Assets/phat_excalibur.png').convert_alpha()
excalibur_rect = excalibur_surf.get_rect(center = screen_center)
excalibur = Weapon('Excalibur', excalibur_surf, excalibur_rect, 420, pygame.Rect(screen_center, (100, 100)), 50)