from GamePrincess.creating import *


class Exit(pygame.sprite.Sprite):
    """Этот класс отвечает за выход"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\exit.png')
        self.image = pygame.transform.scale(img, (Conf.tile_size, int(Conf.tile_size * 1.5)))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
