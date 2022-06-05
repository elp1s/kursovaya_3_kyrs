import pygame


class Button:
    """Этот класс отвечает за кнопки"""
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        action = False

        # Получаем положение мыши
        pos = pygame.mouse.get_pos()

        # Проверяем условия наведения и нажатия мышки
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is not True:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # Создаем кнопку
        screen.blit(self.image, self.rect)

        return action
