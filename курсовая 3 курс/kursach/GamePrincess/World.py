import pygame
from GamePrincess.Enemy import Enemy
from GamePrincess.Platform import Platform
from GamePrincess.creating import Exit, Flower, Lava
from GamePrincess.creating.Exit import Exit
from GamePrincess.creating.Flower import Flower
from GamePrincess.creating.Lava import Lava
import GamePrincess.Settings as Conf


class World:
    """Этот класс отвечает за создание мира"""

    def __init__(self, data: list):
        self.tile_list = []
        transform_scale = pygame.transform.scale
        self.ap = self.tile_list.append
        # Загрузка изображения мира
        dirt_img = pygame.image.load(r'.\GamePrincess\Resources\Picture\dirt.jpg')

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    img = transform_scale(dirt_img, (Conf.tile_size, Conf.tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * Conf.tile_size
                    img_rect.y = row_count * Conf.tile_size
                    tile = (img, img_rect)
                    self.ap(tile)
                elif tile == 2:
                    enemy = Enemy(col_count * Conf.tile_size, row_count * Conf.tile_size - 7)
                    Conf.enemy_group.add(enemy)
                elif tile == 3:
                    platform = Platform(col_count * Conf.tile_size, row_count * Conf.tile_size, 1, 0)
                    Conf.platform_group.add(platform)
                elif tile == 4:
                    platform = Platform(col_count * Conf.tile_size, row_count * Conf.tile_size, 0, 1)
                    Conf.platform_group.add(platform)
                elif tile == 5:
                    lava = Lava(col_count * Conf.tile_size, row_count * Conf.tile_size + (Conf.tile_size >> 1))
                    Conf.lava_group.add(lava)
                elif tile == 6:
                    coin = Flower(col_count * Conf.tile_size + (Conf.tile_size >> 1),
                                  row_count * Conf.tile_size + (Conf.tile_size >> 1))
                    Conf.flower_group.add(coin)
                elif tile == 7:
                    exit_1 = Exit(col_count * Conf.tile_size, row_count * Conf.tile_size - (Conf.tile_size >> 1))
                    Conf.exit_group.add(exit_1)
                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            Conf.screen.blit(tile[0], tile[1])
