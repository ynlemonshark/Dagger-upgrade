import pygame
import math
import random

# parameters
field_rect = pygame.Rect(600, 0, 600, 600)
field_image = pygame.transform.scale(pygame.image.load("resources/swords_field_frame.png"), field_rect.size)

# make button
make_button_rect = pygame.Rect(600, 600, 200, 200)
make_button_image = pygame.transform.scale(pygame.image.load("resources/sword_make_button.png"),
                                           (make_button_rect.width, make_button_rect.height * 2))

make_button_gage_rect = pygame.Rect(625, 725, 150, 30)
make_gage_color = (191, 0, 0)

size = (64, 64)

made_resistance = 1000

made_min_distance = 400
made_max_distance = 600

made_min_angle = 270
made_max_angle = 300


def info_import():
    file = open("Code/swords.txt", "r")
    swords_name = []
    while True:
        line = file.readline()
        line = line.replace("\n", "")
        if not line:
            break
        swords_name.append(line)

    file.close()
    return [swords_name]


def image_import(count):
    images = []
    for repeat in range(count):
        images.append(pygame.transform.scale(pygame.image.load("resources/swords/{}.png".format(repeat)), size))

    return images


data = info_import()
names = data[0]

images = image_import(len(names))

# variable
make_gage = 0
make_gage_max = 10

make_button_clicked = 0

made_swords = []


class MadeSword:
    def __init__(self):
        self.position = list(make_button_rect.center)
        self.speed = math.sqrt(2 * made_resistance * random.randint(made_min_distance, made_max_distance))
        self.time = 0
        self.direction = math.radians(random.randint(made_min_angle, made_max_angle))

    def move(self, fps):
        before_time = self.time
        self.time += 1 / fps
        distance = max((self.speed * self.time - made_resistance * (self.time ** 2) / 2) -
                       (self.speed * before_time - made_resistance * (before_time ** 2) / 2), 0)

        self.position[0] += distance * math.cos(self.direction)
        self.position[1] += distance * math.sin(self.direction)

    def draw(self, surface):
        surface.blit(images[0], (self.position[0] - size[0] / 2, self.position[1] - size[1] / 2))


def field_draw(surface):
    surface.blit(field_image, field_rect.topleft)


def make_button_draw(surface):
    surface.blit(make_button_image, make_button_rect.topleft,
                     ((0, make_button_rect.height * make_button_clicked), make_button_rect.size))
    pygame.draw.rect(surface, make_gage_color,
                     (make_button_gage_rect.topleft, (make_button_gage_rect.width * make_gage / make_gage_max,
                                                      make_button_gage_rect.height)))


def make_button_click_down(position):
    if make_button_rect.collidepoint(position):
        global make_gage
        global make_button_clicked
        make_gage += 1
        make_button_clicked = 1
        while make_gage >= make_gage_max:
            make_gage -= make_gage_max
            made_swords.append(MadeSword())


def make_button_click_up():
    global make_button_clicked
    make_button_clicked = 0


def made_calculation(fps):
    for index in range(len(made_swords)):
        made_swords[index].move(fps)


def made_drawing(surface):
    for index in range(len(made_swords)):
        made_swords[index].draw(surface)
