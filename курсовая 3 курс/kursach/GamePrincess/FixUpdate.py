from os import path
import pickle
import pygame
from GamePrincess.World import World
from GamePrincess.creating.Flower import Flower
import GamePrincess.Settings as Conf


class Loader:
    """Класс отвечает за загрузку ресурсов"""
    def __init__(self):
        self.white = (255, 255, 255)  # цвет подсчета цветочков (белый)
        self.blue = (0, 0, 255)  # цвет GameOver (синий)
        self.loops = -1  # зацикливаение музыки
        self.start = 0.0  # начало песни
        self.fade_ms = 5000  # регулирует громкость
        self.volume = 0.5  # громкость

        self.game_over_fx = pygame.mixer.Sound(r'.\GamePrincess\Resources\Music\game_over.mp3')
        self.game_over_fx.set_volume(self.volume)

        # Загрузка изображений
        self.moon_img = pygame.image.load(r'.\GamePrincess\Resources\Picture\moon.png')
        self.bg_img = pygame.image.load(r'.\GamePrincess\Resources\Picture\bg.jpg')
        self.restart_img = pygame.image.load(r'.\GamePrincess\Resources\Picture\restart_btn.png')
        self.start_img = pygame.image.load(r'.\GamePrincess\Resources\Picture\start_btn.png')
        self.exit_img = pygame.image.load(r'.\GamePrincess\Resources\Picture\exit_btn.png')

        # Загрузка музыки
        pygame.mixer.music.load(r'.\GamePrincess\Resources\Music\music.mp3')
        pygame.mixer.music.play()

        pygame.mixer.music.load(r'.\GamePrincess\Resources\Music\music.mp3')
        pygame.mixer.music.play(self.loops, self.start, self.fade_ms)
        self.flower_fx = pygame.mixer.Sound(r'.\GamePrincess\Resources\Music\flower.mp3')
        self.flower_fx.set_volume(self.volume)
        self.jump_fx = pygame.mixer.Sound(r'.\GamePrincess\Resources\Music\jump.mp3')
        self.jump_fx.set_volume(self.volume)
        self.game_over_fx = pygame.mixer.Sound(r'.\GamePrincess\Resources\Music\game_over.mp3')
        self.game_over_fx.set_volume(self.volume)

    # Преображение текста в картинку
    def draw_text(self, font, text_col, x: int, y: int):
        img = font.render(self, True, text_col)
        Conf.screen.blit(img, (x, y))

    # Эта функция отвечает за сброс уровня
    @staticmethod
    def reset_level(player):
        player.reset(100, Conf.screen_height - 130)
        Conf.enemy_group.empty()
        Conf.platform_group.empty()
        Conf.flower_group.empty()
        Conf.lava_group.empty()
        Conf.exit_group.empty()

        # загрузка уровня и создание мира
        if path.exists(rf'.\GamePrincess\Resources\Data\level{Conf.level}_data'):
            pickle_in = open(rf'.\GamePrincess\Resources\Data\level{Conf.level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        world = World(world_data)

        # создание цветка для отображения его подсчета
        Conf.score_flower = Flower(Conf.tile_size >> 1, Conf.tile_size >> 1)
        Conf.flower_group.add(Conf.score_flower)
        return world
