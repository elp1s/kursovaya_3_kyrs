import pygame
from GamePrincess import Enemy
from GamePrincess.Platform import Platform
from GamePrincess.creating import Exit, Flower, Lava
from GamePrincess.creating.Exit import Exit
from GamePrincess.creating.Flower import Flower
from GamePrincess.creating.Lava import Lava
import GamePrincess.settings as conf


class World:
    """Этот класс отвечает за создание мира"""
    def __init__(self, data):
        self.tile_list = []

        # Загружаем изображения мира
        dirt_img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\dirt.jpg')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (conf.tile_size, conf.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * conf.tile_size
                    img_rect.y = row_count * conf.tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    enemy = Enemy.Enemy(col_count * conf.tile_size, row_count * conf.tile_size - 7)
                    conf.enemy_group.add(enemy)
                if tile == 3:
                    platform = Platform(col_count * conf.tile_size, row_count * conf.tile_size, 1, 0)
                    conf.platform_group.add(platform)
                if tile == 4:
                    platform = Platform(col_count * conf.tile_size, row_count * conf.tile_size, 0, 1)
                    conf.platform_group.add(platform)
                if tile == 5:
                    lava = Lava(col_count * conf.tile_size, row_count * conf.tile_size + (conf.tile_size // 2))
                    conf.lava_group.add(lava)
                if tile == 6:
                    coin = Flower(col_count * conf.tile_size + (conf.tile_size // 2), row_count * conf.tile_size + (conf.tile_size // 2))
                    conf.flower_group.add(coin)
                if tile == 7:
                    exit_1 = Exit(col_count * conf.tile_size, row_count * conf.tile_size - (conf.tile_size // 2))
                    conf.exit_group.add(exit_1)
                col_count += 1
            row_count += 1

    def draw(self, screen):
        for tile in self.tile_list:
             conf.screen.blit(tile[0], tile[1])
