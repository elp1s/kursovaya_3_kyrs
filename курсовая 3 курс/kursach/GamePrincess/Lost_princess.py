from GamePrincess import *
from GamePrincess.FixUpdate import Loader
from GamePrincess.Player import Player
from GamePrincess.World import World
from GamePrincess.Button import Button
from GamePrincess.creating.Flower import Flower
import GamePrincess.Settings as Conf


class Lost_princess:
    """Этот класс отвечает за саму игру"""

    @staticmethod
    def start_game():
        print("Good")
        load = Loader()
        player = Player(100, Conf.screen_height - 130)

        # Создание цветка для отображения подсчета
        score_flower = Flower(Conf.tile_size >> 1, Conf.tile_size >> 1)
        Conf.flower_group.add(score_flower)

        # Загрузка данных уровня и создание мира
        if path.exists(rf'.\GamePrincess\Resources\Data\level{Conf.level}_data'):
            pickle_in = open(rf'.\GamePrincess\Resources\Data\level{Conf.level}_data', 'rb')
            Conf.world_data = pickle.load(pickle_in)
        Conf.world = World(Conf.world_data)

        # Создание кнопок
        restart_button = Button(Conf.screen_width // 2 - 50, Conf.screen_height // 2 + 100, load.restart_img)
        start_button = Button(Conf.screen_width // 2 - 350, Conf.screen_height // 2, load.start_img)
        exit_button = Button(Conf.screen_width // 2 + 150, Conf.screen_height // 2, load.exit_img)

        run = True
        while run:
            # обновление
            Conf.clock.tick(Conf.fps)

            Conf.screen.blit(load.bg_img, (0, 0))
            Conf.screen.blit(load.moon_img, (100, 100))

            if Conf.main_menu is True:
                if exit_button.draw(Conf.screen):
                    run = False
                if start_button.draw(Conf.screen):
                    Conf.main_menu = False
            else:
                Conf.world.draw()
               
                if Conf.game_over == 0:
                    Conf.enemy_group.update()
                    Conf.platform_group.update()
                    # Обновлеение скорости
                    # проверка на сбор цветков
                    if pygame.sprite.spritecollide(player, Conf.flower_group, True):
                        Conf.score += 1
                        load.flower_fx.play()
                    Loader.draw_text('X ' + str(Conf.score), Conf.font_score, load.white, Conf.tile_size - 10, 10)

                Conf.enemy_group.draw(Conf.screen)
                Conf.platform_group.draw(Conf.screen)
                Conf.lava_group.draw(Conf.screen)
                Conf.flower_group.draw(Conf.screen)
                Conf.exit_group.draw(Conf.screen)

                Conf.game_over = player.update()

                # если игрок умер
                if Conf.game_over == -1:
                    if restart_button.draw(Conf.screen):
                        Conf.world_data = []
                        Conf.world = load.reset_level(player)
                        Conf.game_over = 0
                        Conf.score = 0

                # Если игрок прошел уровень
                if Conf.game_over == 1:
                    # Сброс игры и переход на следующий уровень
                    Conf.level += 1
                    if Conf.level <= Conf.max_levels:
                        # Сброс уровеня
                        Conf.world_data = []
                        Conf.world = load.reset_level(player)
                        Conf.game_over = 0
                    else:
                        Loader.draw_text('YOU WIN!', Conf.font, load.blue, (Conf.screen_width >> 1) - 140,
                        Conf.screen_height >> 1)
                        if restart_button.draw(Conf.screen):
                            Conf.level = 1
                            Conf.world_data = []
                            Conf.world = load.reset_level(player)
                            Conf.game_over = 0
                            Conf.score = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()
