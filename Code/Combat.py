import pygame

import Font.Font
import Font.tool

setup_button_rect = pygame.Rect(650, 400, 450, 50)
setup_button_image = pygame.transform.scale(pygame.image.load("resources/combat_setup_button.png"),
                                            setup_button_rect.size)
setup_text = Font.Font.render("setup", Font.tool.filled_list(0, len("setup")), (27, 27))
setup_text_rect = setup_text.get_rect()
setup_text_rect.center = setup_button_rect.center

combat_setup_slot_size = (150, 150)
combat_setup_slot_toplefts = ((650, 50), (800, 50), (950, 50), (650, 200), (800, 200), (950, 200))
combat_setup_slot_image = pygame.transform.scale(pygame.image.load("resources/combat_setup_slot.png"),
                                                 combat_setup_slot_size)
combat_setup_slot_number_text_topleft = (30, 30)
combat_setup_slot_number_texts = []
for index in range(len(combat_setup_slot_toplefts)):
    combat_setup_slot_number_texts.append(Font.Font.render(str(index + 1),
                                                           Font.tool.filled_list(0, len(str(index + 1))),
                                                           (90, 90)))
    combat_setup_slot_number_texts[index].set_alpha(63)

setup_name_frame_rect = pygame.Rect(0, 0, 1200, 50)
setup_name_frame_image = pygame.transform.scale(pygame.image.load("resources/setup_name_frame.png"),
                                                setup_name_frame_rect.size)
setup_name_frame_text = Font.Font.render("Setup", Font.tool.filled_list(0, 5), (36, 36))
setup_name_frame_text_topleft = (510, 9)


def combat_setup_button_draw(surface):
    surface.blit(setup_button_image, setup_button_rect.topleft)
    surface.blit(setup_text, setup_text_rect.topleft)


def combat_setup_slot_draw(surface):
    for index in range(len(combat_setup_slot_toplefts)):
        surface.blit(combat_setup_slot_image, combat_setup_slot_toplefts[index])
        surface.blit(combat_setup_slot_number_texts[index],
                     (combat_setup_slot_toplefts[index][0] + combat_setup_slot_number_text_topleft[0],
                      combat_setup_slot_toplefts[index][1] + combat_setup_slot_number_text_topleft[1]))


def combat_setup_button_click(position, channel):
    if setup_button_rect.collidepoint(position):
        channel.shift("Setup")


def setup_name_frame_draw(surface):
    surface.blit(setup_name_frame_image, setup_name_frame_rect.topleft)
    surface.blit(setup_name_frame_text, setup_name_frame_text_topleft)

