import pygame
from pygame import mixer

from GamePrincess.creating.Flower import Flower

tile_size = 50
game_over = 0
main_menu = True
level = 1
max_levels = 8
score = 0

clock = pygame.time.Clock()
fps = 60

screen_width = 1000
screen_height = 1000

screen = pygame.display.set_mode((screen_width, screen_height))
    
enemy_group = pygame.sprite.Group()
platform_group = pygame.sprite.Group()
lava_group = pygame.sprite.Group()
flower_group = pygame.sprite.Group()
exit_group = pygame.sprite.Group()
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()
# определяем шрифт
font = pygame.font.SysFont('Bauhaus 93', 70)
font_score = pygame.font.SysFont('Bauhaus 93', 30)
# Создаем цветок для отображения подсчета
score_flower = Flower(tile_size // 2, tile_size // 2)
flower_group.add(score_flower)
