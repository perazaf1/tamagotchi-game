import pygame, os
from mainConst import screen, pixel_font
from abs_path import abs_path

pygame.init()
clicked_help = False  # Boolean to track if help is clicked


class Panel:
    def __init__(self, x, y, width, height, path, text_1=None, text_2=None, text_3=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_1 = text_1
        self.text_2 = text_2
        self.text_3 = text_3
        # Load and scale the panel image
        self.image = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
        # Load and scale the exit icon
        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/iconCross_beige.png')), (40, 40))
        self.exit_rect = self.exit.get_rect(center=(175, 65))
        
        # Render the first text
        self.first_text = pixel_font.render(self.text_1, True, (255, 255, 255))
        self.first_text_rect = self.first_text.get_rect(center=(400, 200))

        # Render the second text
        self.second_text = pixel_font.render(self.text_2, True, (255, 255, 255))
        self.second_text_rect = self.second_text.get_rect(center=(400, 250))

        # Render the third text
        self.third_text = pixel_font.render(self.text_3, True, (255, 255, 255))
        self.third_text_rect = self.third_text.get_rect(center=(400, 400))

    def blit_panel(self):
        if clicked_help:
            # Blit the panel image onto the screen
            screen.blit(self.image, self.image_rect)
            # Blit the first text onto the screen
            screen.blit(self.first_text, self.first_text_rect)
            # Blit the second text onto the screen
            screen.blit(self.second_text, self.second_text_rect)
            # Blit the third text onto the screen
            screen.blit(self.third_text, self.third_text_rect)
            # Blit the exit icon onto the screen
            screen.blit(self.exit, self.exit_rect)
