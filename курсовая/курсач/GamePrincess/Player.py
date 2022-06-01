import GamePrincess.settings as conf
import pygame
import GamePrincess.FixUpdate as load


class Player:
    """Этот класс отвечает за персонажа"""

    def __init__(self, x, y):
        self.reset(x, y)

    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 5
        col_thresh = 20

        if conf.game_over == 0:
            # Получаем нажатия клавиш
            key = pygame.key.get_pressed()

            if key[pygame.K_SPACE] and self.jumped is not True and self.in_air is not True:
                load.Loader.jump_fx.play()
                self.vel_y = -15
                self.jumped = True

            if key[pygame.K_SPACE] is not True:
                self.jumped = False

            if key[pygame.K_LEFT]:
                dx -= 5
                self.counter += 1
                self.direction = -1

            if key[pygame.K_RIGHT]:
                dx += 5
                self.counter += 1
                self.direction = 1

            if key[pygame.K_LEFT] is not True and key[pygame.K_RIGHT] is not True:
                self.counter = 0
                self.index = 0

                if self.direction == 1:
                    self.image = self.images_right[self.index]

                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # Обрабатываем анимацию
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1

                if self.index >= len(self.images_right):
                    self.index = 0

                if self.direction == 1:
                    self.image = self.images_right[self.index]

                if self.direction == -1:
                    self.image = self.images_left[self.index]

            # Создаем гравитацию
            self.vel_y += 1
            if self.vel_y > 10:
                self.vel_y = 10
            dy += self.vel_y

            # Проверяем на столкновения
            self.in_air = True
            for tile in conf.world.tile_list:

                # Столкновения в направлении x
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # Столкновения в направлении y
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):

                    # Проверяем находится он на земле, т.е. прыгает
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0

                    # Проверяем находится он над землей, т.е. падает
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            # Проверка на столкновение с врагами
            if pygame.sprite.spritecollide(self, conf.enemy_group, False):
                conf.game_over = -1
                load.Loader.game_over_fx.play()

            # Проверка на столкновение с лавой
            if pygame.sprite.spritecollide(self, conf.lava_group, False):
                conf.game_over = -1
                load.Loader.game_over_fx.play()

            # Проверка на столкновение с выходом
            if pygame.sprite.spritecollide(self, conf.exit_group, False):
                conf.game_over = 1

            # Проверка на столкновение с платформами
            for platform in conf.platform_group:

                # Столкновение в направлении х
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # Столкновение в направлении y
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):

                    # Проверка, если ниже платформы
                    if abs((self.rect.top + dy) - platform.rect.bottom) < col_thresh:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top

                    # Проверка, если над платформой
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < col_thresh:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0

                    # Движение вместе с платформой
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            # Обновить координаты игрока
            self.rect.x += dx
            self.rect.y += dy

        elif conf.game_over == -1:
            self.image = self.dead_image
            load.Loader.draw_text('GAME OVER!', conf.font, load.Loader.blue, (conf.screen_width // 2) - 200, conf.screen_height // 2)
            if self.rect.y > 200:
                self.rect.y -= 5

        # Вывести игрока на экран
        conf.screen.blit(self.image, self.rect)

        return conf.game_over

    def reset(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'.\\GamePrincess\\Resources\\Picture\\girl{num}.png')
            img_right = pygame.transform.scale(img_right, (40, 80))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('.\\GamePrincess\\Resources\\Picture\\ghost.png')
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
