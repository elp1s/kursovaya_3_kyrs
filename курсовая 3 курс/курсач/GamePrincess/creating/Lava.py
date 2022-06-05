from GamePrincess.creating import *


class Lava(pygame.sprite.Sprite):
    """Этот класс отвечает за создание лавы"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\lava.png')
        self.image = pygame.transform.scale(img, (Conf.tile_size, Conf.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
