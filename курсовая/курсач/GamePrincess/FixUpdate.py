from os import path
import pickle
import pygame
from GamePrincess.World import World
from GamePrincess.creating.Flower import Flower
import GamePrincess.settings as conf


class Loader:

    white = (255, 255, 255)
    blue = (0, 0, 255)

    game_over_fx = pygame.mixer.Sound('.\\GamePrincess\\Resources\\Music\\game_over.mp3')
    game_over_fx.set_volume(0.5)
    white = (255, 255, 255)
    blue = (0, 0, 255)
    
    # Загружаем изображения
    moon_img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\moon.png')
    bg_img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\bg.jpg')
    restart_img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\restart_btn.png')
    start_img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\start_btn.png')
    exit_img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\exit_btn.png')

    # Загружаем музыку
    pygame.mixer.music.load('.\\GamePrincess\\Resources\\Music\\music.mp3')
    pygame.mixer.music.play(-1, 0.0, 5000)
    flower_fx = pygame.mixer.Sound('.\\GamePrincess\\Resources\\Music\\flower.mp3')
    flower_fx.set_volume(0.5)
    jump_fx = pygame.mixer.Sound('.\\GamePrincess\\Resources\\Music\\jump.mp3')
    jump_fx.set_volume(0.5)
    game_over_fx = pygame.mixer.Sound('.\\GamePrincess\\Resources\\Music\\game_over.mp3')
    game_over_fx.set_volume(0.5)

    # Эта функция отвечает за рисование текста (преображает текст в картинку)
    def draw_text(self, font, text_col, x, y):
        img = font.render(self, True, text_col)
        conf.screen.blit(img, (x, y))

    # Эта функция отвечает за сброс уровня
    def reset_level(self, player):
        player.reset(100, conf.screen_height - 130)
        conf.enemy_group.empty()
        conf.platform_group.empty()
        conf.flower_group.empty()
        conf.lava_group.empty()
        conf.exit_group.empty()

        # загружаем уровень и создаем мир
        if path.exists(f'.\GamePrincess\Resources\Data\level{conf.level}_data'):
            pickle_in = open(f'.\GamePrincess\Resources\Data\level{conf.level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        world = World(world_data)

        # создаем цветок для отображения его подсчета
        conf.score_flower = Flower(conf.tile_size // 2, conf.tile_size // 2)
        conf.flower_group.add(conf.score_flower)
        return world
