import pygame
import random
from Entities.enemy import Enemy
from Components.weapon import Weapon
from constants import DISPLAY_SIZE, DISPLAY_CENTER
from Prefabs.player_prefab import player
from Utilities.helper_functions import blitRotate

# pygame setup
pygame.init()
pygame.display.set_caption('HG Quest')
screen = pygame.display.set_mode(DISPLAY_SIZE)
clock = pygame.time.Clock()
running = True
dt = 0

# excalibur_surf = pygame.image.load('Assets/phat_excalibur.png').convert_alpha()
# excalibur_rect = excalibur_surf.get_rect(center = DISPLAY_CENTER)
# excalibur = Weapon('Excalibur', excalibur_surf, excalibur_rect, 420, pygame.Rect(DISPLAY_CENTER, (100, 100)), 50)

# player_surf = pygame.image.load('Assets/player.png').convert_alpha()
# player_rect = player_surf.get_rect(center = DISPLAY_CENTER)
# player = Player('Player', 
#                 Player.MAX_HEALTH, 
#                 pygame.Vector2(DISPLAY_CENTER), 
#                 300, 
#                 player_surf, 
#                 player_rect, 
#                 0, 
#                 excalibur, 
#                 None, 
#                 [])

game_over_font = pygame.font.Font('Fonts/Pixeltype.ttf', 400)
game_over_surf = game_over_font.render('YOU DIED', False, 'RED')
game_over_rect = game_over_surf.get_rect(center = DISPLAY_CENTER)

score = 0

GUI_font = pygame.font.Font('Fonts/Pixeltype.ttf', 100)
hp_surf = GUI_font.render(f"{player.health} HP", False, 'Black')
hp_rect = hp_surf.get_rect(topleft = (10, 10))
score_surf = GUI_font.render(str(score) , False, 'Black')
score_rect = score_surf.get_rect(midtop = (screen.get_width() / 2, 10))

enemy_surf = pygame.image.load('Assets/enemy_knight.png').convert_alpha()
enemy_rect = enemy_surf.get_rect()
enemy = Enemy('Dark Knight', 1, None, 100, enemy_surf, enemy_rect)

inside_enemy = False

entities = []

def spawnEnemies(count):
    for _ in range(count):
        enemy_pos_x = random.randrange(-32, screen.get_width() + 32)
        enemy_pos_y = random.randrange(-32, screen.get_height() + 32)
        if enemy_pos_x > 0 and enemy_pos_x < screen.get_width():
            enemy_pos_y = random.choice([-32, screen.get_height() + 32])
        if enemy_pos_y > 0 and enemy_pos_y < screen.get_height():
            enemy_pos_x = random.choice([-32, screen.get_width() + 32])
        entities.append(Enemy(str(enemy.name), int(enemy.health), None, int(enemy.speed), enemy_surf, enemy_surf.get_rect(center = (enemy_pos_x, enemy_pos_y))))

spawnEnemies(10)

attacking = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if player.alive() and event.type == pygame.MOUSEBUTTONDOWN:
            player.attack(entities)
            attacking = True
        if player.alive() and event.type == pygame.MOUSEBUTTONUP:
            attacking = False

    if not player.alive():
        screen.fill("black")
        screen.blit(game_over_surf, game_over_rect)
        score_surf = GUI_font.render(f'SCORE: {score}', False, 'white')
        score_rect = score_surf.get_rect(midtop = game_over_rect.midbottom)
        screen.blit(score_surf, score_rect)
        pygame.display.update()
        continue
    
    screen.fill("darkgreen")    

    for entity in entities:
        if not entity.alive():
            score += 1
            entities.remove(entity)
            spawnEnemies(1)
            continue
        screen.blit(entity.surf, entity.rect)
    screen.blit(player.surf, player.rect)
    hp_surf = GUI_font.render(f"{player.health} HP", False, 'Black')
    screen.blit(hp_surf, hp_rect)
    score_surf = GUI_font.render(str(score), False, 'Black')
    screen.blit(score_surf, score_rect)

    for entity in entities:
        if not player.rect.colliderect(entity.rect):
            entity.move(player, dt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.rect.y -= player.speed * dt
    if keys[pygame.K_s]:
        player.rect.y += player.speed * dt
    if keys[pygame.K_a]:
        player.rect.x -= player.speed * dt
    if keys[pygame.K_d]:
        player.rect.x += player.speed * dt

    if attacking:
        mouse_pos = pygame.mouse.get_pos()
        up = pygame.Vector2(0, 1)
        direction = pygame.Vector2(mouse_pos[0] - player.rect.x, mouse_pos[1] - player.rect.y)
        direction.normalize_ip()
        direction.scale_to_length(player.weapon.range)
        player.weapon.aoe.center = player.rect.center
        player.weapon.aoe.center = tuple(map(sum, zip(player.weapon.aoe.center, direction)))
        player.weapon.rect.center = tuple(player.weapon.aoe.center)
        blitRotate(screen, player.weapon.surf, player.rect.center, (16, 32 + player.weapon.range), 180 - up.angle_to(direction))

    if player.rect.collidelist([entity.rect for entity in entities]) != -1:
        if not inside_enemy:
            player.health -= 1
            inside_enemy = True
    else:
        inside_enemy = False

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()