import pygame
import GamePrincess.Settings as Conf


class Platform(pygame.sprite.Sprite):
    """Этот класс отвечает за создание платформ"""

    def __init__(self, x: int, y: int, move_x: int, move_y: int):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load(r'.\GamePrincess\Resources\Picture\platform.png')
        self.image = pygame.transform.scale(img, (Conf.tile_size, Conf.tile_size >> 1))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_counter = 0
        self.move_direction = 1
        self.move_x = move_x
        self.move_y = move_y

    def update(self):
        """Этот метод отвечает за движение платформ"""
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
