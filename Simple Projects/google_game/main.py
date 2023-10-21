import sys
import pygame
import random

pygame.font.init()
FONT = pygame.font.SysFont('comicsans', 100)
GAME_OVER = pygame.USEREVENT + 1
pygame.display.set_caption("MUSTAFA")
WIDTH, HEIGHT = 1600, 900
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SKY = (135, 206, 235)
CLOUD = pygame.transform.scale(pygame.image.load("Assets/big_cloud.png"), (150, 150))
cloud_list = [pygame.Rect(a*360 + random.randint(0,50), random.randint(47,77), 150, 150) for a in range(6)]
cloud_vel = 4
GROUNDS = [
    pygame.transform.scale(pygame.image.load("Assets/tile46.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load("Assets/tile23.png"), (150, 150)),
    pygame.transform.scale(pygame.image.load("Assets/tile22.png"), (150, 150))
]
ground_list = [pygame.Rect(a*450, 750, 150, 150) for a in range(5)]
BLOCKS = [
    pygame.transform.scale(pygame.image.load("Assets/trees2_1.png"), (120, 200)),#565
    pygame.transform.scale(pygame.image.load("Assets/rocks1_5.png"), (180, 200)),#635
    pygame.transform.scale(pygame.image.load("Assets/rocks1_3.png"), (180, 200)),#635
    pygame.transform.scale(pygame.image.load("Assets/rocks1_6.png"), (180, 200)),#655
    pygame.transform.scale(pygame.image.load("Assets/trees2_3.png"), (180, 200)),#620
]
block_list = [
    (0, pygame.Rect(2100, 565, 100, 200)),
    (1, pygame.Rect(2800, 635, 100, 200)),
    (2, pygame.Rect(3500, 635, 90, 200))
]


def set_beginning(c):
    c.loc_x = 160
    c.loc_y = 650
    c.ground_vel = 14
    c.level = 0
    a = [
        (0, pygame.Rect(2100, 565, 100, 200)),
        (1, pygame.Rect(2800, 635, 100, 200)),
        (2, pygame.Rect(3500, 635, 90, 200))
    ]
    return a


def is_alive(block_list, c):
    for i, block in block_list:
        if block.colliderect(c.hit_box):
            draw_text = FONT.render("""Game Over{}""".format(int(c.point)), 1, (30, 30, 30))
            WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() /
                                 2, HEIGHT / 2 - draw_text.get_height() / 2))
            pygame.display.update()
            block_list = set_beginning(c)
            pygame.time.delay(3000)


def draw_objects(ground_list, cloud_list, block_list, c):
    for cloud in cloud_list:
        WIN.blit(CLOUD, (cloud.x, cloud.y))
    c.point += 0.3
    draw_text = FONT.render(str(int(c.point)), 1, (100, 70, 100))
    WIN.blit(draw_text, (1530 - draw_text.get_width(), 50))
    for ground in ground_list:
        WIN.blit(GROUNDS[0], (ground.x, ground.y))
        WIN.blit(GROUNDS[1], (ground.x + 150, ground.y))
        WIN.blit(GROUNDS[2], (ground.x + 300, ground.y))
    for i, block in block_list:
        if i == 0:
            WIN.blit(BLOCKS[0], (block.x - 10, block.y - 10))
        elif i == 1:
            WIN.blit(BLOCKS[1], (block.x - 35, block.y - 50))
        elif i == 2:
            WIN.blit(BLOCKS[2], (block.x - 60, block.y - 50))
        elif i == 3:
            WIN.blit(BLOCKS[3], (block.x - 25, block.y - 50))
        elif i == 4:
            WIN.blit(BLOCKS[4], (block.x - 25, block.y - 35))


def handle_movement(ground_list, cloud_list, block_list, c):
    for cloud in cloud_list:
        cloud.x -= cloud_vel
        if cloud.x < -360:
            cloud_list.remove(cloud)
            cloud_list.append(pygame.Rect(1780 + random.randint(0, 50), random.randint(47, 77), 150, 150))
    for ground in ground_list:
        ground.x -= c.ground_vel
        if ground.x < -450:
            ground_list.remove(ground)
            ground_list.append(pygame.Rect(ground_list[3].x + 450, 750, 150, 150))
    for i, block in block_list:
        block.x -= c.ground_vel
        if block.x < -300:
            c.level += 1
            if c.level == 6:
                c.level = 0
                if c.ground_vel < 24:
                    c.ground_vel += 2
            block_list.remove((i, block))
            a = random.randint(0, 4)
            if a == 0:
                block_list.append((a, pygame.Rect(random.randint(1850, 2000), 565, 100, 200)))
            elif a == 1:
                block_list.append((a, pygame.Rect(random.randint(1850, 2000), 635, 100, 200)))
            elif a == 2:
                block_list.append((a, pygame.Rect(random.randint(1850, 2000), 635, 90, 200)))
            elif a == 3:
                block_list.append((a, pygame.Rect(random.randint(1850, 2000), 655, 130, 200)))
            elif a == 4:
                block_list.append((a, pygame.Rect(random.randint(1850, 2000), 620, 105, 200)))


class Character():
    point = 0
    level = 0
    ground_vel = 14
    fall = False
    loc_x = 160
    loc_y = 650
    hit_box = pygame.Rect(loc_x + 17, loc_y + 7, 75, 90)
    self = None
    DUST_INDEX = 0
    RUN_FRAME_INDEX = 0
    JUMP_ANIMATION = [pygame.transform.scale(i, (100, 100)) for i in
                      [pygame.image.load("Assets/Jump (32x32).png"), pygame.image.load("Assets/Fall (32x32).png")]]
    JUMP_INDEX = 0

    def get_frame(self, start, size, img, col):
        frames = []
        for i in range(col):
            location = (start[0] + size[0]*i, 0)
            frames.append(pygame.transform.scale(img.subsurface(pygame.Rect(location, size)), (100, 100)))
        return frames

    RUN_FRAMES = get_frame(self, (0, 0), (32, 32), pygame.image.load("Assets/Run (32x32).png"), 8)
    FALL_DUST = get_frame(self, (0, 0), (32, 32), pygame.image.load("Assets/Double_Jump_Dust_5.png"), 5)

    def display_dust(self):
        if self.fall:
            if self.DUST_INDEX < 4:
                WIN.blit(pygame.transform.scale(self.FALL_DUST[self.DUST_INDEX], (70, 70)), (180, 700))
                self.DUST_INDEX += 1
            else:
                WIN.blit(pygame.transform.scale(self.FALL_DUST[self.DUST_INDEX], (70, 70)), (180, 700))
                self.DUST_INDEX = 0
                self.fall = False

    def display_run(self):
        if self.JUMP_INDEX == 0:
            if self.RUN_FRAME_INDEX != 8:
                WIN.blit(self.RUN_FRAMES[self.RUN_FRAME_INDEX], (self.loc_x, self.loc_y))
            else:
                self.RUN_FRAME_INDEX = 0
                WIN.blit(self.RUN_FRAMES[self.RUN_FRAME_INDEX], (self.loc_x, self.loc_y))
            self.RUN_FRAME_INDEX += 1
        else:
            self.display_jump()
        self.hit_box = pygame.Rect(self.loc_x + 17, self.loc_y + 7, 75, 90)

    def display_jump(self):
        self.hit_box = pygame.Rect(self.loc_x + 17, self.loc_y + 7, 75, 90)
        if self.JUMP_INDEX < 12:
            WIN.blit(self.JUMP_ANIMATION[0], (self.loc_x, self.loc_y))
            self.loc_y -= 2 * ((6 - self.JUMP_INDEX/2) ** 2)
            self.JUMP_INDEX += 1
        elif self.JUMP_INDEX < 24:
            WIN.blit(self.JUMP_ANIMATION[1], (self.loc_x, self.loc_y))
            self.loc_y += 2 * ((6 - self.JUMP_INDEX/2) ** 2)
            self.JUMP_INDEX += 1
        else:
            WIN.blit(self.JUMP_ANIMATION[1], (self.loc_x, self.loc_y))
            self.loc_y += 2 * ((6 - self.JUMP_INDEX/2) ** 2)
            self.JUMP_INDEX = 0
            self.fall = True


def main():
    run = True
    clock = pygame.time.Clock()
    c = Character()
    while run:
        clock.tick(24)
        WIN.fill(SKY)
        handle_movement(ground_list, cloud_list, block_list, c)
        draw_objects(ground_list, cloud_list, block_list, c)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            c.display_jump()
        else:
            c.display_run()
        c.display_dust()
        is_alive(block_list, c)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == '__main__':
    main()
