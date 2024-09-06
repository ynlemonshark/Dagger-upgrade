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


def roman_numeral(number):
    roman_numerals = ("I", "V", "X", "L", "C", "D", "M", "F")
    number_places = ([], [0], [0, 0], [0, 0, 0], [0, 1], [1],
                     [1, 0], [1, 0, 0], [1, 0, 0, 0], [0, 2])

    text = ""

    number_sequence = list(str(number))
    for index in range(len(number_sequence)):
        for place in number_places[int(number_sequence[index])]:
            text += roman_numerals[place + (len(number_sequence) - index - 1) * 2]

    return text
