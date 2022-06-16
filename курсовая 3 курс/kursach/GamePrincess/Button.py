import pygame


class Button:
    """Этот класс отвечает за кнопки"""
    def __init__(self, x: int, y: int, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clicked = False

    def draw(self, screen):
        """Этот метод отвечает за рисование"""
        action = False

        # Получение положения мыши
        pos = pygame.mouse.get_pos()

        # Проверка условия наведения и нажатия мышки
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True
                self.clicked = True

        else:
            self.clicked = False

        # Создание кнопки
        screen.blit(self.image, self.rect)

        return action
