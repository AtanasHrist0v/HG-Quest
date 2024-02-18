import pygame

from constants import DISPLAY_CENTER


game_over_font = None
game_over_surf = None
game_over_rect = None

GUI_font = None
hp_surf = None
hp_rect = None
score_surf = None
score_rect = None


def init():
    global game_over_font, game_over_surf, game_over_rect, GUI_font, hp_surf, hp_rect, score_surf, score_rect
    
    game_over_font = pygame.font.Font('Fonts/Pixeltype.ttf', 400)
    game_over_surf = game_over_font.render('YOU DIED', False, 'RED')
    game_over_rect = game_over_surf.get_rect(center = DISPLAY_CENTER)

    GUI_font = pygame.font.Font('Fonts/Pixeltype.ttf', 100)
    hp_surf = GUI_font.render('0 HP', False, 'Black')
    hp_rect = hp_surf.get_rect(topleft = (10, 10))
    score_surf = GUI_font.render('0' , False, 'Black')
    score_rect = score_surf.get_rect(midtop = (DISPLAY_CENTER[0], 10))