import pygame
from random import randrange, choice

from constants import DISPLAY_SIZE, DISPLAY_CENTER
from Prefabs import GUI_prefabs, player_prefab, dark_knight_prefab
from Utilities.helper_functions import blitRotate
from Entities.enemy import Enemy


# pygame setup
pygame.init()
screen = pygame.display.set_mode(DISPLAY_SIZE)
pygame.display.set_caption('HG Quest')
clock = pygame.time.Clock()
running = True
dt = 0

# prefab setup
player_prefab.init()
dark_knight_prefab.init()
GUI_prefabs.init()

GUI_font = GUI_prefabs.GUI_font
game_over_surf = GUI_prefabs.game_over_surf
game_over_rect = GUI_prefabs.game_over_rect
hp_rect = GUI_prefabs.hp_rect
score_rect = GUI_prefabs.score_rect
player = player_prefab.player
score = 0
entities = []
inside_enemy = False
attacking = False


def end_game():
    screen.fill("black")
    screen.blit(game_over_surf, game_over_rect)
    score_surf = GUI_font.render(f'SCORE: {score}', False, 'white')
    score_rect = score_surf.get_rect(midtop = game_over_rect.midbottom)
    screen.blit(score_surf, score_rect)
    pygame.display.update()


def display_everything():
    global score, GUI_font

    screen.fill("darkgreen")

    for entity in entities:
        if not entity.alive():
            score += 1
            entities.remove(entity)
            spawn_enemies(1, dark_knight_prefab.dark_knight)
            continue
        screen.blit(entity.surf, entity.rect)
    screen.blit(player.surf, player.rect)
    hp_surf = GUI_font.render(f"{player.health} HP", False, 'Black')
    screen.blit(hp_surf, hp_rect)
    score_surf = GUI_font.render(str(score), False, 'Black')
    screen.blit(score_surf, score_rect)

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


def move_everything():
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


def get_hit_by_everything():
    global inside_enemy
    
    if player.rect.collidelist([entity.rect for entity in entities]) != -1:
        if not inside_enemy:
            player.health -= 1
            inside_enemy = True
    else:
        inside_enemy = False


def spawn_enemies(count, enemy):
    for _ in range(count):
        enemy_pos_x = randrange(-32, screen.get_width() + 32)
        enemy_pos_y = randrange(-32, screen.get_height() + 32)
        if enemy_pos_x > 0 and enemy_pos_x < screen.get_width():
            enemy_pos_y = choice([-32, screen.get_height() + 32])
        if enemy_pos_y > 0 and enemy_pos_y < screen.get_height():
            enemy_pos_x = choice([-32, screen.get_width() + 32])
        entities.append(Enemy(str(enemy.name), int(enemy.health), None, int(enemy.speed), enemy.surf, enemy.surf.get_rect(center = (enemy_pos_x, enemy_pos_y))))

spawn_enemies(10, dark_knight_prefab.dark_knight)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if player.alive():
            if event.type == pygame.MOUSEBUTTONDOWN:
                player.attack(entities)
                attacking = True
            if event.type == pygame.MOUSEBUTTONUP:
                attacking = False

    if not player.alive():
        end_game()
        continue
    
    display_everything()
    move_everything()
    get_hit_by_everything()

    pygame.display.update()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()