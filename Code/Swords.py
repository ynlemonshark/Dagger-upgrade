import pygame
import math
import random

import Font.Font
import Font.tool

# parameters


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


def image_import(count, sword_size):
    images = []
    for repeat in range(count):
        images.append(pygame.transform.scale(pygame.image.load("resources/swords/{}.png".format(repeat)), sword_size))

    return images


size = (64, 64)

data = info_import()
names = data[0]

images = image_import(len(names), size)

field_rect = pygame.Rect(600, 0, 600, 600)
field_image = pygame.transform.scale(pygame.image.load("resources/swords_field_frame.png"), field_rect.size)

# make button
make_button_rect = pygame.Rect(600, 600, 600, 100)
make_button_image = pygame.transform.scale(pygame.image.load("resources/sword_make_button.png"),
                                           (make_button_rect.width, make_button_rect.height * 2))

make_button_gage_rect = pygame.Rect(800, 625, 375, 50)
make_gage_color = (191, 0, 0)

# upgrade slot
upgrade_slot_rect = pygame.Rect(0, 0, 200, 200)
upgrade_slot_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_slot.png"),
                                            upgrade_slot_rect.size)
upgrade_slot_sword_rect = pygame.Rect(36, 36, 128, 128)
upgrade_slot_sword_images = image_import(len(names), upgrade_slot_sword_rect.size)

upgrade_slot_information_rect = pygame.Rect(200, 0, 400, 200)
upgrade_slot_information_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_info_slot.png"),
                                                        upgrade_slot_information_rect.size)

upgrade_slot_made_min_distance = 700
upgrade_slot_made_max_distance = 900

upgrade_slot_made_min_angle = 0
upgrade_slot_made_max_angle = 30

upgrade_slot_information_text_topleft = (220, 20)
upgrade_slot_information_text_size = (18, 18)
upgrade_slot_information_name_color = 0

made_resistance = 1000

made_min_distance = 400
made_max_distance = 600

made_min_angle = 250
made_max_angle = 290

pick_distance = 40


# variable
make_gage = 0
make_gage_max = 10

make_button_clicked = 0

made_swords = []

swords = []

picking = False
picked_sword = 0
picked_position = (0, 0)

upgrade_slot = "empty"


class MadeSword:
    def __init__(self, rank, position, speed, direction):
        self.position = list(position)
        self.speed = math.sqrt(2 * made_resistance * speed)
        self.time = 0
        self.rank = rank
        self.direction = math.radians(direction)

    def move(self, fps):
        before_time = self.time
        self.time += 1 / fps
        distance = max((self.speed * self.time - made_resistance * (self.time ** 2) / 2) -
                       (self.speed * before_time - made_resistance * (before_time ** 2) / 2), 0)

        self.position[0] += distance * math.cos(self.direction)
        self.position[1] += distance * math.sin(self.direction)

    def draw(self, surface):
        surface.blit(images[self.rank], (self.position[0] - size[0] / 2, self.position[1] - size[1] / 2))


class Sword:
    def __init__(self, position, rank):
        self.position = position
        self.rank = rank

    def draw(self, surface):
        surface.blit(images[self.rank], (self.position[0] - size[0] / 2, self.position[1] - size[1] / 2))


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
            made_swords.append(MadeSword(0, list(make_button_rect.center),
                                         random.randint(made_min_distance, made_max_distance),
                                         random.randint(made_min_angle, made_max_angle)))


def make_button_click_up():
    global make_button_clicked
    make_button_clicked = 0


def made_calculation(fps):
    global made_swords
    global swords
    for index in range(len(made_swords)):
        before_position = list(made_swords[index].position)
        made_swords[index].move(fps)

        if before_position == made_swords[index].position:
            swords.append(Sword(made_swords[index].position, made_swords[index].rank))
            made_swords[index] = 0

    for repeat in range(made_swords.count(0)):
        made_swords.remove(0)


def made_draw(surface):
    for index in range(len(made_swords)):
        made_swords[index].draw(surface)


def draw(surface):
    for index in range(len(swords)):
        if not picking or not picked_sword == index:
            swords[index].draw(surface)


def pick(position):
    global picked_sword
    global picking
    global picked_position
    for index in range(len(swords)):
        distance = math.dist(swords[index].position, position)

        if distance <= pick_distance:
            if picking:
                if math.dist(swords[index].position, position) >= distance:
                    picked_sword = index
                    picking = True
                    picked_position = (position[0] - swords[index].position[0], position[1] - swords[index].position[1])

            else:
                picked_sword = index
                picking = True
                picked_position = (position[0] - swords[index].position[0], position[1] - swords[index].position[1])


def pick_down(position):
    global picking
    global upgrade_slot
    if picking:
        picking = False
        sword_rect = pygame.Rect((0, 0), size)
        sword_rect.center = (position[0] - picked_position[0], position[1] - picked_position[1])
        if field_rect.left <= sword_rect.left <= field_rect.right and \
           field_rect.left <= sword_rect.right <= field_rect.right and \
           field_rect.top <= sword_rect.top <= field_rect.bottom and \
           field_rect.top <= sword_rect.bottom <= field_rect.bottom:
            swords[picked_sword].position = sword_rect.center
        elif upgrade_slot_rect.collidepoint(position):
            if upgrade_slot != "empty":
                made_swords.append(MadeSword(upgrade_slot.rank, upgrade_slot_rect.center,
                                             random.randint(upgrade_slot_made_min_distance,
                                                            upgrade_slot_made_max_distance)
                                             , random.randint(upgrade_slot_made_min_angle,
                                                              upgrade_slot_made_max_angle)))
            upgrade_slot = swords[picked_sword]
            swords[picked_sword] = 0
            swords.remove(0)


def pick_draw(surface, mouse_pos):
    if picking:
        surface.blit(images[swords[picked_sword].rank],
                     (mouse_pos[0] - picked_position[0] - size[0] / 2, mouse_pos[1] - picked_position[1] - size[1] / 2))


def upgrade_slot_draw(surface):
    surface.blit(upgrade_slot_image, upgrade_slot_rect.topleft)
    surface.blit(upgrade_slot_information_image, upgrade_slot_information_rect.topleft)
    if not upgrade_slot == "empty":
        surface.blit(upgrade_slot_sword_images[upgrade_slot.rank], upgrade_slot_sword_rect.topleft)
        surface.blit(Font.Font.render(names[upgrade_slot.rank],
                                      Font.tool.filled_list(upgrade_slot_information_name_color,
                                                            len(names[upgrade_slot.rank])),
                                      upgrade_slot_information_text_size),
                     upgrade_slot_information_text_topleft)


def upgrade_slot_click(position):
    global upgrade_slot
    if upgrade_slot_rect.collidepoint(position):
        if upgrade_slot != "empty":
            made_swords.append(MadeSword(upgrade_slot.rank, upgrade_slot_rect.center,
                                         random.randint(upgrade_slot_made_min_distance,
                                                        upgrade_slot_made_max_distance)
                                         , random.randint(upgrade_slot_made_min_angle,
                                                          upgrade_slot_made_max_angle)))
            upgrade_slot = "empty"
