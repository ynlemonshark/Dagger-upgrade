import pygame

letters = (' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '.',
           ',', '?', '!', '“', '”', '‘', '’', ':', ';', '_', '+', '-', '×', '÷', '%', '(', ')', '/', )

colors = ("Black", "White", "Gray", "Red", "Orange", "Yellow", "Lime", "Green", "Mint", "Blue", "Navy",
          "Purple", "Pink", "Brown")


size = (9, 9)

image = pygame.transform.scale(pygame.image.load("Font/letter.png"), (size[0] * len(letters), size[1] * len(colors)))
void = pygame.image.load("Font/void.png")


def render(text, color, text_size):
    lines = text.upper().split("\n")
    color_lines = []

    lines_max_length = 0
    for index in range(len(lines)):
        lines[index] = list(lines[index])
        color_lines.append(color[:len(lines[index])])
        color = color[len(lines[index]):]
        if lines_max_length < len(lines[index]):
            lines_max_length = len(lines[index])

    surface = pygame.transform.scale(void, (size[0] * lines_max_length, size[1] * len(lines)))

    for line_index in range(len(lines)):
        for index in range(len(lines[line_index])):
            surface.blit(image, (index * size[0], line_index * size[1]),
                         (letters.index(lines[line_index][index]) * size[0],
                          color_lines[line_index][index] * size[1], size[0], size[1]))

    return pygame.transform.scale(surface, (text_size[0] * lines_max_length, text_size[1] * len(lines)))
