import pygame

import Font.Font
import Font.tool

# parameters
forge_coin_frame_rect = pygame.Rect(600, 0, 300, 50)
forge_coin_frame_image = pygame.transform.scale(pygame.image.load("resources/forge_coin_frame.png"),
                                                forge_coin_frame_rect.size)


class Coin:
    def __init__(self, start_coin):
        self.amount = start_coin

    def plus(self, amount):
        self.amount += amount

    def minus(self, amount):
        self.amount -= amount


# variable

amount = Coin(100)
coin_number_size = (18, 18)
coin_number_color = 0
coin_number_icon_size = (18, 18)
coin_number_icon_image = pygame.transform.scale(pygame.image.load("resources/coin.png"), coin_number_icon_size)
coin_number_between_space = 10


def coin_number(number):
    number_text = Font.Font.render(str(number), Font.tool.filled_list(coin_number_color, len(str(number))),
                                   coin_number_size)
    number_text_rect = number_text.get_rect()

    surface = pygame.transform.scale(Font.tool.void,
                                     (number_text_rect.width + coin_number_icon_size[0] + coin_number_between_space,
                                      coin_number_icon_size[1]))

    surface.blit(coin_number_icon_image, (0, 0))
    surface.blit(number_text, (coin_number_icon_size[0] + coin_number_between_space, 0))

    return surface


def forge_draw(surface):
    surface.blit(forge_coin_frame_image, forge_coin_frame_rect.topleft)

    text = coin_number(amount.amount)
    text_rect = text.get_rect()
    text_rect.center = forge_coin_frame_rect.center
    surface.blit(text, text_rect.topleft)

