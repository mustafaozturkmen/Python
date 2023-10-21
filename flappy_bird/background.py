import pygame
import random


class Background():
    vel = 10
    back_png = pygame.transform.scale(pygame.image.load("Assets/background-day.png"), (800, 900))
    down_pattern = pygame.transform.scale(pygame.image.load("Assets/base.png"), (300, 100))
    down_pattern_list = [pygame.Rect(a*300, 800, 300, 100) for a in range(7)]
    down_block = pygame.transform.scale(pygame.image.load("Assets/pipe-green.png"), (150, 600))
    up_block = pygame.transform.flip(down_block, False, True)
    add_block_int = 0
    up_block_list = [
        pygame.Rect(1600, random.randint(-500, -200), 150, 600)
    ]
    down_block_list = [pygame.Rect(i.x, i.y + 900, 150, 600) for i in up_block_list]

    def display_background(self, WIN):
        for i in [0, 1]:
            WIN.blit(self.back_png, (i*800, 0))
        for block in self.down_block_list:
            WIN.blit(self.down_block, (block.x, block.y))
        for block in self.up_block_list:
            WIN.blit(self.up_block, (block.x, block.y))
        for down in self.down_pattern_list:
            WIN.blit(self.down_pattern, (down.x, down.y))
        self.handle_movement()

    def handle_movement(self):
        self.add_block_int += self.vel
        for block in self.up_block_list:
            block.x -= self.vel
            if block.x < -200:
                self.up_block_list.remove(block)
        for block in self.down_block_list:
            block.x -= self.vel
            if block.x < -200:
                self.down_block_list.remove(block)
        for down in self.down_pattern_list:
            down.x -= self.vel
            if down.x < -300:
                self.down_pattern_list.remove(down)
        if self.add_block_int % 600 == 0:
            random_loc = random.randint(-500, -200)
            self.up_block_list.append(pygame.Rect(1600, random_loc, 150, 600))
            self.down_block_list.append(pygame.Rect(1600, random_loc + 900, 150, 600))
        if self.add_block_int % 300 == 0:
            self.down_pattern_list.append(pygame.Rect(1800, 800, 300, 100))

    def set_beginning(self):
        self.up_block_list = [
            pygame.Rect(1600, random.randint(-500, -200), 150, 600)
        ]
        self.down_block_list = [pygame.Rect(i.x, i.y + 900, 150, 600) for i in self.up_block_list]
