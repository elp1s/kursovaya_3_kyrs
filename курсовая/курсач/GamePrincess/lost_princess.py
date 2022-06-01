from GamePrincess import *
from GamePrincess.FixUpdate import Loader
from GamePrincess.Player import Player
from GamePrincess.World import World
from GamePrincess.button import Button
from GamePrincess.creating.Flower import Flower
import GamePrincess.settings as conf


class Game:
    """Этот класс отвечает за саму игру"""

    def StartGame():
        print("Good")
        player = Player(100, conf.screen_height - 130)

        # Создаем цветок для отображения подсчета
        score_flower = Flower(conf.tile_size // 2, conf.tile_size // 2)
        conf.flower_group.add(score_flower)

        # Загружаем данные уровня и создаем мир
        if path.exists(f'.\GamePrincess\Resources\Data\level{conf.level}_data'):
            pickle_in = open(f'.\GamePrincess\Resources\Data\level{conf.level}_data', 'rb')
            conf.world_data = pickle.load(pickle_in)
        conf.world = World(conf.world_data)

        # Создаем кнопки
        restart_button = Button(conf.screen_width // 2 - 50, conf.screen_height // 2 + 100, Loader.restart_img)
        start_button = Button(conf.screen_width // 2 - 350, conf.screen_height // 2, Loader.start_img)
        exit_button = Button(conf.screen_width // 2 + 150, conf.screen_height // 2, Loader.exit_img)

        run = True
        while run:
            # обновляем
            conf.clock.tick(conf.fps)

            conf.screen.blit(Loader.bg_img, (0, 0))
            conf.screen.blit(Loader.moon_img, (100, 100))

            if conf.main_menu == True:
                if exit_button.draw(conf.screen):
                    run = False
                if start_button.draw(conf.screen):
                    conf.main_menu = False
            else:
                conf.world.draw(conf.screen)
               
                if conf.game_over == 0:
                    conf.enemy_group.update()
                    conf.platform_group.update()
                    # Обновляем скорость
                    # проверяем собрали ли цветок
                    if pygame.sprite.spritecollide(player, conf.flower_group, True):
                        conf.score += 1
                        Loader.flower_fx.play()
                    Loader.draw_text('X ' + str(conf.score), conf.font_score, Loader.white, conf.tile_size - 10, 10)

                conf.enemy_group.draw(conf.screen)
                conf.platform_group.draw(conf.screen)
                conf.lava_group.draw(conf.screen)
                conf.flower_group.draw(conf.screen)
                conf.exit_group.draw(conf.screen)

                conf.game_over = player.update(conf.game_over)

                # если игрок умер
                if conf.game_over == -1:
                    if restart_button.draw(conf.screen):
                        conf.world_data = []
                        conf.world = Loader.reset_level(conf.level, player)
                        conf.game_over = 0
                        conf.score = 0

                # Если игрок прошел уровень
                if conf.game_over == 1:
                    # Сбросить игру и перейти на следующий уровень
                    conf.level += 1
                    if conf.level <= conf.max_levels:
                        # Сбросить уровень
                        conf.world_data = []
                        conf.world = Loader.reset_level(conf.level, player)
                        conf.game_over = 0
                    else:
                        Loader.draw_text('YOU WIN!', conf.font, Loader.blue, (conf.screen_width // 2) - 140, conf.screen_height // 2)
                        if restart_button.draw(conf.screen):
                            conf.level = 1
                            # Сбросить уровень
                            conf.world_data = []
                            conf.world = Loader.reset_level(conf.level, player)
                            conf.game_over = 0
                            conf.score = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

        pygame.quit()
