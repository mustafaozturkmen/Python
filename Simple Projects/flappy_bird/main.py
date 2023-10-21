import time
import pygame
import sys
import random
from background import Background
from menu import Menu
from bird import Bird


WIN = pygame.display.set_mode((1600, 900))
Bird = Bird()
BackGround = Background()
Menu = Menu()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(30)
        if Menu.started:
            if Menu.start_game_index == 21:
                BackGround.display_background(WIN)
                Bird.display_bird(WIN, Menu.selected_bird, Menu.bird_index)
                Menu.handle_bird()
                if not(Bird.is_alive(BackGround.down_block_list)):
                    Menu.death = True
                    Menu.started = False
                    Menu.start_game_index = 0
                    BackGround.set_beginning()
                    Bird.set_beginning()
                elif not(Bird.is_alive(BackGround.up_block_list)):
                    Menu.death = True
                    Menu.started = False
                    Menu.start_game_index = 0
                    BackGround.set_beginning()
                    Bird.set_beginning()
            else:
                Menu.start_game(WIN)
        elif Menu.go_option:
            Menu.display_options(WIN)
        elif Menu.death:
            Menu.display_death(WIN)
        else:
            Menu.display_beginning(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()
