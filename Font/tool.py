import pygame
from math import log10
void = pygame.image.load("Font/void.png")


def filled_list(fill_with, count):
    list_to_fill = []
    for repeat in range(count):
        list_to_fill.append(fill_with)

    return list_to_fill


def number_suffix(number):
    suffixes = ("", "K", "M", "G", "T", "P", "E", "Z", "Y")
    text = str(number // (1000 ** int(log10(number) // 3)))
    text += suffixes[int(log10(number) // 3)]

    return text
