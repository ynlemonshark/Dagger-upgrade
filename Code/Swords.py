import pygame

field_rect = pygame.Rect(600, 0, 600, 600)
field_image = pygame.transform.scale(pygame.image.load("resources/swords_field_frame.png"), field_rect.size)
