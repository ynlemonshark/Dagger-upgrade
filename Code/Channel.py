import pygame

# parameter
big_channels = (["Forge"], ["Combat"], ["Ability"], ["Encyclopedia"], ["Shop"], ["Dummy"], ["Dummy"], ["Endings"])

big_channel_button_first_topleft = (0, 700)
big_channel_button_size = (150, 100)
big_channel_button_icon_size = (75, 75)
big_channel_button_icon_position = (37.5, 12.5)
big_channel_button_selected = pygame.transform.scale(pygame.image.load("resources/big_channel_button/selected.png"),
                                                     big_channel_button_size)
big_channel_button_unselected = pygame.transform.scale(pygame.image.load("resources/big_channel_button/unselected.png"),
                                                     big_channel_button_size)

big_channel_button_rects = []
big_channel_button_icons = []
for index in range(len(big_channels)):
    big_channel_button_rects.append(pygame.Rect((big_channel_button_first_topleft[0]
                                                 + index * big_channel_button_size[0],
                                                 big_channel_button_first_topleft[1]),
                                                big_channel_button_size))
    big_channel_button_icons.append(pygame.transform.scale(
        pygame.image.load("resources/big_channel_button/{}.png".format(index)), big_channel_button_icon_size))


class ChannelClass:
    def __init__(self, start_channel):
        self.channel = start_channel

    def shift(self, shift_to):
        self.channel = shift_to


# variable
Channel = ChannelClass("Forge")


def big_channel_buttons_draw(surface):
    for index in range(len(big_channels)):
        if Channel.channel in big_channels[index]:
            surface.blit(big_channel_button_selected, big_channel_button_rects[index])
        else:
            surface.blit(big_channel_button_unselected, big_channel_button_rects[index])
        surface.blit(big_channel_button_icons[index],
                     (big_channel_button_rects[index].left + big_channel_button_icon_position[0],
                      big_channel_button_rects[index].top + big_channel_button_icon_position[1]))


def big_channel_button_click(position):
    for index in range(len(big_channels)):
        if big_channel_button_rects[index].collidepoint(position):
            Channel.shift(big_channels[index][0])
