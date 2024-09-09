import pygame
import sys
from pygame.locals import QUIT, Rect

import Font.Font

import Code.Swords
import Code.Coin
import Code.Channel


def setting_import():
    settings_file = open("setting.txt", "r")
    settings = {}
    while True:
        line = settings_file.readline()
        line.replace("\n", "")
        if line:
            line = line.split(":")
            settings[line[0]] = int(line[1])
        else:
            break

    return settings


setting = setting_import()

Display_width = setting["Display_width"]
Display_height = setting["Display_height"]

Surface_width = 1200
Surface_height = 800

display_ratio_x = Display_width / Surface_width
display_ratio_y = Display_height / Surface_height

FPS = setting["FPS"]

pygame.init()
DISPLAY = pygame.display.set_mode((Display_width, Display_height))
SURFACE = pygame.Surface((Surface_width, Surface_height))
FPSCLOCK = pygame.time.Clock()


def main():
    global DISPLAY
    gameStart = True
    fullScreen = False

    Code.Channel.background_init((Surface_width, Surface_height))
    while True:
        pygame_events = pygame.event.get()
        for pygame_event in pygame_events:
            if pygame_event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif pygame_event.type == pygame.KEYUP:
                if pygame_event.key == pygame.K_F1:
                    if fullScreen:
                        DISPLAY = pygame.display.set_mode((Display_width, Display_height))
                    else:
                        DISPLAY = pygame.display.set_mode((Display_width, Display_height), pygame.FULLSCREEN)
                    fullScreen = not fullScreen

            elif pygame_event.type == pygame.MOUSEBUTTONDOWN:
                event_pos = (pygame_event.pos[0] / display_ratio_x, pygame_event.pos[1] / display_ratio_y)
                if Code.Channel.Channel.channel == "Forge":
                    Code.Swords.make_button_click_down(event_pos)
                    Code.Swords.pick(event_pos)
                    Code.Swords.upgrade_slot_click(event_pos)
                    Code.Swords.upgrade_button_click(event_pos, Code.Coin.amount)
                    Code.Swords.sell_button_click(event_pos, Code.Coin.amount)
                Code.Channel.big_channel_button_click(event_pos)

            elif pygame_event.type == pygame.MOUSEBUTTONUP:
                event_pos = (pygame_event.pos[0] / display_ratio_x, pygame_event.pos[1] / display_ratio_y)
                if Code.Channel.Channel.channel == "Forge":
                    Code.Swords.make_button_click_up()
                    Code.Swords.pick_down(event_pos)

        # calculation
        mouse_pos = pygame.mouse.get_pos()
        mouse_pos = (mouse_pos[0] / display_ratio_x, mouse_pos[1] / display_ratio_y)

        Code.Swords.made_calculation(FPS)
        Code.Swords.upgrade_gage_calculation(FPS)
        Code.Swords.upgrade_effect_calculation(FPS)

        # draw

        SURFACE.fill((255, 0, 0))
        Code.Channel.background_draw(SURFACE)
        if Code.Channel.Channel.channel == "Forge":
            Code.Swords.field_draw(SURFACE)
            Code.Swords.make_button_draw(SURFACE)
            Code.Swords.draw(SURFACE)
            Code.Swords.sell_button_draw(SURFACE)
            Code.Swords.upgrade_slot_draw(SURFACE, Code.Coin.amount.amount)
            Code.Swords.pick_draw(SURFACE, mouse_pos)
            Code.Swords.made_draw(SURFACE)
            Code.Swords.upgrade_effect_draw(SURFACE)
            Code.Coin.forge_draw(SURFACE)
        Code.Channel.big_channel_buttons_draw(SURFACE)

        DISPLAY.blit(pygame.transform.scale(SURFACE, (Display_width, Display_height)), (0, 0))

        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == "__main__":
    main()
