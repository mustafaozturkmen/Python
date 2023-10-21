import pygame


class Bird():
    pressed_time = 0
    unpressed_index = 0
    unpressed_time = 0
    bird_vel = 0
    bird_loc_x = 150
    bird_loc_y = 420
    bird_list = [
        [pygame.transform.scale(pygame.image.load("Assets/bluebird-{}flap.png".format(a)), (100, 60)) for a in
         ["up", "mid", "down"]],
        [pygame.transform.scale(pygame.image.load("Assets/redbird-{}flap.png".format(a)), (100, 60)) for a in
         ["up", "mid", "down"]],
        [pygame.transform.scale(pygame.image.load("Assets/yellowbird-{}flap.png".format(a)), (100, 60)) for a in
         ["up", "mid", "down"]]
    ]
    hit_box = pygame.Rect(bird_loc_x + 15, bird_loc_y + 10, 70, 40)

    def rotate_bird(self, selected, bird_index):
        rotated_bird = pygame.transform.rotate(self.bird_list[selected][bird_index], self.bird_vel * 2)
        return rotated_bird

    def handle_bird(self):
        if self.pressed_time > 4:
            if pygame.mouse.get_pressed()[0]:
                self.bird_vel += 7
                self.pressed_time = 0
                self.unpressed_time = 0
            elif pygame.key.get_pressed()[pygame.K_UP]:
                self.bird_vel += 7
                self.pressed_time = 0
                self.unpressed_time = 0
            elif pygame.key.get_pressed()[pygame.K_SPACE]:
                self.bird_vel += 7
                self.pressed_time = 0
                self.unpressed_time = 0
            else:
                self.unpressed_index += 1
                if self.unpressed_index == 4:
                    self.unpressed_index = 0
                    self.unpressed_time += 1
                    self.bird_vel -= self.unpressed_time
        else:
            self.pressed_time += 1
            self.unpressed_index += 1
            if self.unpressed_index == 4:
                self.unpressed_index = 0
                self.unpressed_time += 1
                self.bird_vel -= self.unpressed_time
        if self.bird_loc_y - self.bird_vel < 740:
            self.bird_loc_y -= self.bird_vel

    def display_bird(self, WIN, selected, bird_index):
        WIN.blit(self.rotate_bird(selected, bird_index), (self.bird_loc_x, self.bird_loc_y))
        self.handle_bird()
        self.hit_box = pygame.Rect(self.bird_loc_x + 15, self.bird_loc_y + 10, 70, 40)

    def is_alive(self, blocks):
        alive = True
        if self.bird_loc_y > 740:
            return False
        else:
            for block in blocks:
                if block.colliderect(self.hit_box):
                    alive = False
                    break
            return alive

    def set_beginning(self):
        self.bird_vel = 0
        self.unpressed_time = 0
        self.pressed_time = 0
        self.unpressed_index = 0
        self.bird_loc_x = 150
        self.bird_loc_y = 420
        self.hit_box = pygame.Rect(self.bird_loc_x + 15, self.bird_loc_y + 10, 70, 40)
