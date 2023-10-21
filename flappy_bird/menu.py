import pygame


class Menu():
    down = pygame.transform.scale(pygame.image.load("Assets/base.png"), (300, 100))
    flag = pygame.transform.scale(pygame.image.load("Assets/pngegg.png"), (600, 200))
    flag_movement = (500, 100)
    game_over = pygame.transform.scale(pygame.image.load("Assets/gameover.png"), (600, 200))
    flag_index = 0
    back = pygame.transform.scale(pygame.image.load("Assets/background-day.png"), (800, 900))
    start = pygame.transform.scale(pygame.image.load("Assets/start.png"), (100, 100))
    start_button = pygame.Rect(675, 625, 100, 100)
    option = pygame.transform.scale(pygame.image.load("Assets/menu.png"), (100, 100))
    option_button = pygame.Rect(825, 625, 100, 100)
    back_button = pygame.transform.scale(pygame.image.load("Assets/back.png"), (100, 100))
    bird_list = [
        [pygame.transform.scale(pygame.image.load("Assets/bluebird-{}flap.png".format(a)), (100, 60)) for a in
         ["up", "mid", "down"]],
        [pygame.transform.scale(pygame.image.load("Assets/redbird-{}flap.png".format(a)), (100, 60)) for a in
         ["up", "mid", "down"]],
        [pygame.transform.scale(pygame.image.load("Assets/yellowbird-{}flap.png".format(a)), (100, 60)) for a in
         ["up", "mid", "down"]]
    ]
    selected_bird = 0
    bird_index = 0
    bird_index1 = 0
    start_game_index = 0
    death = False
    started = False
    go_option = False

    def display_beginning(self, WIN):
        for i in range(2):
            WIN.blit(self.back, (i*800, 0))
        WIN.blit(self.flag, self.flag_movement)
        WIN.blit(self.bird_list[self.selected_bird][self.bird_index], (750, 420))
        WIN.blit(self.start, (675, 625))
        WIN.blit(self.option, (825, 625))
        self.handle_flag()
        self.handle_bird()
        self.start_button_fun()
        self.option_button_fun()

    def display_options(self, WIN):
        for i in range(2):
            WIN.blit(self.back, (i*800, 0))
        WIN.blit(self.flag, self.flag_movement)
        WIN.blit(self.back_button, (750, 625))
        x, y = (580, 400)
        for a in range(3):
            if a == self.selected_bird:
                WIN.blit(pygame.transform.scale(self.bird_list[a][self.bird_index], (150, 90)), (x - 25, y - 15))
            else:
                WIN.blit(self.bird_list[a][self.bird_index], (x, y))
            x += 170
        self.handle_flag()
        self.handle_bird()
        self.select_bird()
        self.back_button_fun()

    def display_death(self, WIN):
        WIN.blit(self.game_over, (500, 150))
        WIN.blit(self.start, (675, 625))
        WIN.blit(self.option, (825, 625))
        self.start_button_fun()
        self.option_button_fun()

    def select_bird(self):
        x, y = (580, 400)
        for a in range(3):
            if pygame.Rect(x, y, 100, 60).collidepoint(pygame.mouse.get_pos()):
                if pygame.mouse.get_pressed()[0]:
                    self.selected_bird = a
            x += 170

    def handle_flag(self):
        flag_list = range(-10, 11)
        if self.flag_index != 20:
            i, j = self.flag_movement
            j += flag_list[self.flag_index]
            self.flag_movement = (i, j)
            self.flag_index += 1
        else:
            i, j = self.flag_movement
            j += flag_list[self.flag_index]
            self.flag_movement = (i, j)
            self.flag_index = 0

    def handle_bird(self):
        if self.bird_index1 < 4:
            self.bird_index = 0
            self.bird_index1 += 1
        elif self.bird_index1 < 8:
            self.bird_index = 1
            self.bird_index1 += 1
        elif self.bird_index1 < 12:
            self.bird_index = 2
            self.bird_index1 += 1
        else:
            self.bird_index = 1
            self.bird_index1 = 0

    def start_button_fun(self):
        if self.start_button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.started = True

    def option_button_fun(self):
        if self.option_button.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.go_option = True

    def back_button_fun(self):
        if pygame.Rect(750, 625, 100 ,100).collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.go_option = False
                self.death = False

    def start_game(self, WIN):
        if self.start_game_index != 20:
            for i in range(2):
                WIN.blit(self.back, (i * 800, 0))
            WIN.blit(self.bird_list[self.selected_bird][self.bird_index], (750 - self.start_game_index*30, 420))
            for j in range(7):
                WIN.blit(self.down, (j*300, 900 - self.start_game_index*5))
            self.start_game_index += 1
        elif self.start_game_index == 20:
            for i in range(2):
                WIN.blit(self.back, (i * 800, 0))
            WIN.blit(self.bird_list[self.selected_bird][self.bird_index], (750 - self.start_game_index*30, 420))
            for j in range(7):
                WIN.blit(self.down, (j*300, 900 - self.start_game_index*5))
            self.start_game_index += 1
        self.handle_bird()
