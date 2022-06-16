import pygame


class Enemy(pygame.sprite.Sprite):
    """Этот класс отвечает за врагов"""
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(r'.\GamePrincess\Resources\Picture\enemy.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        """Этот метод отвечает за действие врага"""
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
