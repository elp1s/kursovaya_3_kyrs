from GamePrincess.creating import *
class Flower(pygame.sprite.Sprite):
    """Этот класс создает цветы"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\flower.png')
        self.image = pygame.transform.scale(img, (conf.tile_size // 2, conf.tile_size // 2))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

