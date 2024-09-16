import pygame
import math
import random

import Font.Font
import Font.tool

# parameters


def info_import():
    file = open("Code/swords.txt", "r")
    swords_name = []
    swords_price = []
    swords_success = []
    swords_fail = []
    swords_destroy = []
    swords_upgrade_cost = []
    while True:
        line = file.readline()
        line = line.replace("\n", "")
        if not line:
            break
        line = line.split(",")
        swords_name.append(line[0])
        swords_price.append(int(line[1]))
        swords_success.append(int(line[2]))
        swords_fail.append(int(line[3]))
        swords_destroy.append(int(line[4]))
        swords_upgrade_cost.append(int(line[5]))

    file.close()
    return (swords_name, swords_price, swords_success, swords_fail, swords_destroy, swords_upgrade_cost)


def image_import(count, sword_size):
    images = []
    for repeat in range(count):
        images.append(pygame.transform.scale(pygame.image.load("resources/swords/{}.png".format(repeat)), sword_size))

    return images


size = (64, 64)

data = info_import()
names = data[0]
prices = data[1]
success_chance = data[2]
fail_chance = data[3]
destroy_chance = data[4]
upgrade_cost = data[5]

images = image_import(len(names), size)

field_rect = pygame.Rect(600, 50, 600, 550)
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

upgrade_slot_chance_size = (200, 50)

upgrade_slot_chance_success_rect = pygame.Rect((0, 200), upgrade_slot_chance_size)
upgrade_slot_chance_fail_rect = pygame.Rect((200, 200), upgrade_slot_chance_size)
upgrade_slot_chance_destroy_rect = pygame.Rect((400, 200), upgrade_slot_chance_size)

upgrade_slot_chance_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_chance.png"),
                                                   upgrade_slot_chance_size)

upgrade_slot_chance_success_text_color = 6
upgrade_slot_chance_fail_text_color = 2
upgrade_slot_chance_destroy_text_color = 3

upgrade_slot_chance_text_size = (18, 18)

upgrade_button_rect = pygame.Rect(400, 250, 200, 75)
upgrade_button_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_button.png"),
                                              upgrade_button_rect.size)
upgrade_button_image_enable = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_button_enable.png"),
                                                     upgrade_button_rect.size)

upgrade_button_text = Font.Font.render("upgrade", Font.tool.filled_list(0, 7), (18, 18))
upgrade_button_text_rect = upgrade_button_text.get_rect()
upgrade_button_text_rect.center = (upgrade_button_rect.left + 100, upgrade_button_rect.top + 25)

upgrade_button_cost_text = "cost:{}"
upgrade_button_cost_text_size = (9, 9)
upgrade_button_cost_text_center = (500, 300)

upgrade_gage_rect = pygame.Rect(0, 250, 400, 75)
upgrade_gage_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_gage.png"), upgrade_gage_rect.size)

upgrade_gage_inside_rect = pygame.Rect(0, 260, 400, 55)
upgrade_gage_color_success = (67, 224, 0)
upgrade_gage_color_fail = (128, 128, 128)
upgrade_gage_color_destroy = (224, 0, 0)

upgrade_gage_resistance = 200

upgrade_gage_cursor_size = (25, 75)
upgrade_gage_cursor_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_cursor.png"),
                                                   upgrade_gage_cursor_size)

upgrade_effect_rect = pygame.Rect(0, 0, 600, 325)
upgrade_effect_success_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_effect_success.png"),
                                                      upgrade_effect_rect.size)
upgrade_effect_fail_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_effect_fail.png"),
                                                   upgrade_effect_rect.size)
upgrade_effect_destroy_image = pygame.transform.scale(pygame.image.load("resources/sword_upgrade_effect_destroy.png"),
                                                      upgrade_effect_rect.size)

upgrade_effect_time = 800

# sell button
sell_button_rect = pygame.Rect(0, 625, 600, 75)
sell_button_image = pygame.transform.scale(pygame.image.load("resources/sword_sell_button.png"),
                                           sell_button_rect.size)
sell_button_enable_image = pygame.transform.scale(pygame.image.load("resources/sword_sell_button_enable.png"),
                                                  sell_button_rect.size)

sell_button_sell_text = Font.Font.render("sell", Font.tool.filled_list(0, 4), (27, 27))
sell_button_sell_text_rect = sell_button_sell_text.get_rect()
sell_button_sell_text_rect.center = sell_button_rect.center

sell_button_price_text = "sell:{}"
sell_button_price_text_color = 0
sell_button_price_text_size = (27, 27)

# setup
setup_name_frame_rect = pygame.Rect(0, 0, 1200, 50)
setup_name_frame_image = pygame.transform.scale(pygame.image.load("resources/setup_name_frame.png"),
                                                setup_name_frame_rect.size)
setup_name_frame_text = Font.Font.render("Setup", Font.tool.filled_list(0, 5), (36, 36))
setup_name_frame_text_topleft = (510, 9)

setup_exit_button_rect = pygame.Rect(0, 600, 1200, 100)
setup_exit_button_image = pygame.transform.scale(pygame.image.load("resources/setup_exit_button.png"),
                                                 setup_exit_button_rect.size)
setup_exit_button_text = Font.Font.render("exit", (0, 0, 0, 0), (72, 72))
setup_exit_button_topleft = (460, 618)

setup_slot_size = (200, 200)
setup_slot_toplefts = ((0, 50), (200, 50), (400, 50), (0, 250), (200, 250), (400, 250))
setup_slot_image = pygame.transform.scale(pygame.image.load("resources/setup_slot.png"), setup_slot_size)

setup_slot_sword_topleft = (36, 36)

setup_slot_made_min_distance = 600
setup_slot_made_max_distance = 630
setup_slot_made_min_angle = 0
setup_slot_made_max_angle = 20

setup_slot_reset_button_rect = pygame.Rect(0, 450, 600, 150)
setup_slot_reset_button_image = pygame.transform.scale(pygame.image.load("resources/setup_reset_button.png"),
                                                       setup_slot_reset_button_rect.size)
setup_slot_reset_button_enable_image = pygame.transform.scale(
    pygame.image.load("resources/setup_reset_button_enable.png"), setup_slot_reset_button_rect.size)
setup_slot_reset_button_text = Font.Font.render("setup reset", Font.tool.filled_list(0, 11), (36, 36))
setup_slot_reset_button_text_rect = setup_slot_reset_button_text.get_rect()
setup_slot_reset_button_text_rect.center = setup_slot_reset_button_rect.center

made_resistance = 1000

made_min_distance = 400
made_max_distance = 550

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

upgrading = False
upgrade_gage = 0
upgrade_gage_speed = 0
upgrade_gage_time = 0
upgrade_gage_life = 0

upgrade_effect_type = 0
upgrade_effect_delay = 0

setup_slots = ["empty", "empty", "empty", "empty", "empty", "empty"]


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

    def rank_up(self):
        self.rank += 1


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


def pick_down(position, channel):
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
        elif not upgrading and upgrade_slot_rect.collidepoint(position) and channel == "Forge":
            if upgrade_slot != "empty":
                made_swords.append(MadeSword(upgrade_slot.rank, upgrade_slot_rect.center,
                                             random.randint(upgrade_slot_made_min_distance,
                                                            upgrade_slot_made_max_distance)
                                             , random.randint(upgrade_slot_made_min_angle,
                                                              upgrade_slot_made_max_angle)))
            upgrade_slot = swords[picked_sword]
            swords[picked_sword] = 0
            swords.remove(0)

        elif channel == "Setup":
            for index in range(len(setup_slot_toplefts)):
                if pygame.Rect(setup_slot_toplefts[index], setup_slot_size).collidepoint(position):
                    if setup_slots[index] != "empty":
                        made_swords.append(MadeSword(setup_slots[index].rank,
                                                     (setup_slot_toplefts[index][0] + setup_slot_size[0] / 2,
                                                      setup_slot_toplefts[index][1] + setup_slot_size[1] / 2),
                                                     random.randint(setup_slot_made_min_distance,
                                                                    setup_slot_made_max_distance)
                                                     , random.randint(setup_slot_made_min_angle,
                                                                      setup_slot_made_max_angle)))
                    setup_slots[index] = swords[picked_sword]
                    swords[picked_sword] = 0
                    swords.remove(0)


def pick_draw(surface, mouse_pos):
    if picking:
        surface.blit(images[swords[picked_sword].rank],
                     (mouse_pos[0] - picked_position[0] - size[0] / 2, mouse_pos[1] - picked_position[1] - size[1] / 2))


def upgrade_slot_draw(surface, coin):
    surface.blit(upgrade_slot_image, upgrade_slot_rect.topleft)
    surface.blit(upgrade_slot_information_image, upgrade_slot_information_rect.topleft)

    surface.blit(upgrade_slot_chance_image, upgrade_slot_chance_success_rect.topleft)
    surface.blit(upgrade_slot_chance_image, upgrade_slot_chance_fail_rect.topleft)
    surface.blit(upgrade_slot_chance_image, upgrade_slot_chance_destroy_rect.topleft)

    surface.blit(upgrade_button_image, upgrade_button_rect.topleft)
    surface.blit(upgrade_button_text, upgrade_button_text_rect.topleft)

    surface.blit(upgrade_gage_image, upgrade_gage_rect.topleft)
    if not upgrade_slot == "empty":
        surface.blit(upgrade_slot_sword_images[upgrade_slot.rank], upgrade_slot_sword_rect.topleft)
        surface.blit(Font.Font.render(names[upgrade_slot.rank],
                                      Font.tool.filled_list(upgrade_slot_information_name_color,
                                                            len(names[upgrade_slot.rank])),
                                      upgrade_slot_information_text_size),
                     upgrade_slot_information_text_topleft)

        # - chance -
        text_string = "success:{}".format(success_chance[upgrade_slot.rank])
        text_image = Font.Font.render(text_string,
                                      Font.tool.filled_list(upgrade_slot_chance_success_text_color, len(text_string))
                                      , upgrade_slot_chance_text_size)
        text_image_rect = text_image.get_rect()
        text_image_rect.center = upgrade_slot_chance_success_rect.center
        surface.blit(text_image, text_image_rect.topleft)

        text_string = "fail:{}".format(fail_chance[upgrade_slot.rank])
        text_image = Font.Font.render(text_string,
                                      Font.tool.filled_list(upgrade_slot_chance_fail_text_color, len(text_string))
                                      , upgrade_slot_chance_text_size)
        text_image_rect = text_image.get_rect()
        text_image_rect.center = upgrade_slot_chance_fail_rect.center
        surface.blit(text_image, text_image_rect.topleft)

        text_string = "destroy:{}".format(destroy_chance[upgrade_slot.rank])
        text_image = Font.Font.render(text_string,
                                      Font.tool.filled_list(upgrade_slot_chance_destroy_text_color, len(text_string))
                                      , upgrade_slot_chance_text_size)
        text_image_rect = text_image.get_rect()
        text_image_rect.center = upgrade_slot_chance_destroy_rect.center
        surface.blit(text_image, text_image_rect.topleft)
        # - chance -

        if not upgrading and upgrade_cost[upgrade_slot.rank] <= coin:
            surface.blit(upgrade_button_image_enable, upgrade_button_rect.topleft)
            surface.blit(upgrade_button_text, upgrade_button_text_rect.topleft)

        upgrade_button_cost_string = upgrade_button_cost_text.format(str(upgrade_cost[upgrade_slot.rank]))
        upgrade_button_cost_text_image = Font.Font.render(upgrade_button_cost_string,
                                                          Font.tool.filled_list(0, len(upgrade_button_cost_string)),
                                                          upgrade_button_cost_text_size)
        upgrade_button_cost_text_rect = upgrade_button_cost_text_image.get_rect()
        upgrade_button_cost_text_rect.center = upgrade_button_cost_text_center
        surface.blit(upgrade_button_cost_text_image, upgrade_button_cost_text_rect.topleft)

        pygame.draw.rect(surface, upgrade_gage_color_success,
                         (upgrade_gage_inside_rect.topleft,
                          (upgrade_gage_inside_rect.width * success_chance[upgrade_slot.rank] / 100,
                           upgrade_gage_inside_rect.height)))
        pygame.draw.rect(surface, upgrade_gage_color_fail,
                         ((upgrade_gage_inside_rect.left +
                           upgrade_gage_inside_rect.width * success_chance[upgrade_slot.rank] / 100,
                           upgrade_gage_inside_rect.top),
                          (upgrade_gage_inside_rect.width * fail_chance[upgrade_slot.rank] / 100,
                           upgrade_gage_inside_rect.height)))
        pygame.draw.rect(surface, upgrade_gage_color_destroy,
                         ((upgrade_gage_inside_rect.left +
                           upgrade_gage_inside_rect.width * success_chance[upgrade_slot.rank] / 100 +
                           upgrade_gage_inside_rect.width * fail_chance[upgrade_slot.rank] / 100,
                           upgrade_gage_inside_rect.top),
                          (upgrade_gage_inside_rect.width * destroy_chance[upgrade_slot.rank] / 100,
                           upgrade_gage_inside_rect.height)))

        if upgrading:
            extra_distance = upgrade_gage_speed ** 2 / 2 / upgrade_gage_resistance - \
                             (upgrade_gage_life - upgrade_gage_time) *\
                             (upgrade_gage_speed - upgrade_gage_time * upgrade_gage_resistance) / 2
            if extra_distance < 100:
                surface.blit(upgrade_gage_cursor_image,
                             (upgrade_gage_inside_rect.left + upgrade_gage_inside_rect.width -
                              (extra_distance / 100 * upgrade_gage_inside_rect.width) - upgrade_gage_cursor_size[0] / 2,
                              upgrade_gage_rect.top))
            else:
                surface.blit(upgrade_gage_cursor_image,
                             (upgrade_gage_inside_rect.left +
                              ((extra_distance - 100) / 100 * upgrade_gage_inside_rect.width) - upgrade_gage_cursor_size[0] / 2,
                              upgrade_gage_rect.top))


def upgrade_slot_click(position):
    global upgrade_slot
    if upgrade_slot_rect.collidepoint(position):
        if upgrade_slot != "empty" and not upgrading:
            made_swords.append(MadeSword(upgrade_slot.rank, upgrade_slot_rect.center,
                                         random.randint(upgrade_slot_made_min_distance,
                                                        upgrade_slot_made_max_distance)
                                         , random.randint(upgrade_slot_made_min_angle,
                                                          upgrade_slot_made_max_angle)))
            upgrade_slot = "empty"


def upgrade_button_click(position, coin):
    global upgrading
    global upgrade_gage
    global upgrade_gage_speed
    global upgrade_gage_time
    global upgrade_gage_life
    if upgrade_button_rect.collidepoint(position) and not upgrading and upgrade_slot != "empty"\
            and upgrade_cost[upgrade_slot.rank] <= coin.amount:
        upgrading = True
        coin.minus(upgrade_cost[upgrade_slot.rank])

        upgrade_gage = random.randint(0, 99)

        upgrade_gage_time = 0
        upgrade_gage_speed = math.sqrt(2 * upgrade_gage_resistance * (upgrade_gage + 100))

        upgrade_gage_life = upgrade_gage_speed / upgrade_gage_resistance


def upgrade_gage_calculation(fps):
    global upgrade_gage_time
    global upgrading
    global upgrade_slot

    global upgrade_effect_type
    global upgrade_effect_delay
    if upgrading:
        upgrade_gage_time += 1 / fps
        if upgrade_gage_time >= upgrade_gage_life:
            upgrading = False

            if upgrade_gage < success_chance[upgrade_slot.rank]:
                upgrade_slot.rank_up()
                upgrade_effect_type = 0
                upgrade_effect_delay = upgrade_effect_time
            elif upgrade_gage - success_chance[upgrade_slot.rank] < fail_chance[upgrade_slot.rank]:
                upgrade_effect_type = 1
                upgrade_effect_delay = upgrade_effect_time
            else:
                upgrade_slot = "empty"
                upgrade_effect_type = 2
                upgrade_effect_delay = upgrade_effect_time


def upgrade_effect_draw(surface):
    if upgrade_effect_type == 0:
        upgrade_effect_success_image.set_alpha(255 * upgrade_effect_delay / upgrade_effect_time)
        surface.blit(upgrade_effect_success_image, upgrade_effect_rect.topleft)
    if upgrade_effect_type == 1:
        upgrade_effect_fail_image.set_alpha(255 * upgrade_effect_delay / upgrade_effect_time)
        surface.blit(upgrade_effect_fail_image, upgrade_effect_rect.topleft)
    if upgrade_effect_type == 2:
        upgrade_effect_destroy_image.set_alpha(255 * upgrade_effect_delay / upgrade_effect_time)
        surface.blit(upgrade_effect_destroy_image, upgrade_effect_rect.topleft)


def upgrade_effect_calculation(fps):
    global upgrade_effect_delay
    if upgrade_effect_delay:
        upgrade_effect_delay -= 1000 / fps


def sell_button_draw(surface):
    if upgrade_slot == "empty":
        surface.blit(sell_button_image, sell_button_rect.topleft)
        surface.blit(sell_button_sell_text, sell_button_sell_text_rect.topleft)

    else:
        if not upgrading:
            surface.blit(sell_button_enable_image, sell_button_rect.topleft)
        else:
            surface.blit(sell_button_image, sell_button_rect.topleft)
        price_text = sell_button_price_text.format(prices[upgrade_slot.rank])
        text = Font.Font.render(price_text,
                                Font.tool.filled_list(sell_button_price_text_color, len(price_text)),
                                sell_button_price_text_size)
        text_rect = text.get_rect()
        text_rect.center = sell_button_rect.center

        surface.blit(text, text_rect.topleft)


def sell_button_click(position, coin):
    global upgrade_slot
    if not upgrading and upgrade_slot != "empty":
        if sell_button_rect.collidepoint(position):
            coin.plus(prices[upgrade_slot.rank])
            upgrade_slot = "empty"


def setup_name_frame_draw(surface):
    surface.blit(setup_name_frame_image, setup_name_frame_rect.topleft)
    surface.blit(setup_name_frame_text, setup_name_frame_text_topleft)


def setup_exit_button_draw(surface):
    surface.blit(setup_exit_button_image, setup_exit_button_rect.topleft)
    surface.blit(setup_exit_button_text, setup_exit_button_topleft)


def setup_exit_button_click(position, channel):
    if setup_exit_button_rect.collidepoint(position):
        channel.shift("Combat")


def setup_slots_draw(surface):
    for index in range(len(setup_slot_toplefts)):
        surface.blit(setup_slot_image, setup_slot_toplefts[index])
        if setup_slots[index] != "empty":
            surface.blit(upgrade_slot_sword_images[setup_slots[index].rank],
                         (setup_slot_toplefts[index][0] + setup_slot_sword_topleft[0],
                          setup_slot_toplefts[index][1] + setup_slot_sword_topleft[1]))


def setup_slot_click(position):
    for index in range(len(setup_slot_toplefts)):
        if pygame.Rect(setup_slot_toplefts[index], setup_slot_size).collidepoint(position):
            if setup_slots[index] != "empty":
                made_swords.append(MadeSword(setup_slots[index].rank,
                                             (setup_slot_toplefts[index][0] + setup_slot_size[0] / 2,
                                              setup_slot_toplefts[index][1] + setup_slot_size[1] / 2),
                                             random.randint(setup_slot_made_min_distance,
                                                            setup_slot_made_max_distance)
                                             , random.randint(setup_slot_made_min_angle,
                                                              setup_slot_made_max_angle)))
                setup_slots[index] = "empty"


def setup_reset():
    for index in range(len(setup_slots)):
        if setup_slots[index] != "empty":
            made_swords.append(MadeSword(setup_slots[index].rank,
                                         (setup_slot_toplefts[index][0] + setup_slot_size[0] / 2,
                                          setup_slot_toplefts[index][1] + setup_slot_size[1] / 2),
                                         random.randint(setup_slot_made_min_distance,
                                                        setup_slot_made_max_distance)
                                         , random.randint(setup_slot_made_min_angle,
                                                          setup_slot_made_max_angle)))
            setup_slots[index] = "empty"


def setup_reset_button_draw(surface):
    surface.blit(setup_slot_reset_button_enable_image, setup_slot_reset_button_rect.topleft)
    if setup_slots.count("empty") == len(setup_slots):
        surface.blit(setup_slot_reset_button_image, setup_slot_reset_button_rect.topleft)
    surface.blit(setup_slot_reset_button_text, setup_slot_reset_button_text_rect.topleft)


def setup_reset_button_click(position):
    if setup_slot_reset_button_rect.collidepoint(position):
        setup_reset()
