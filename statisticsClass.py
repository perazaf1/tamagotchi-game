import pygame, os
from mainConst import screen, pixel_font
from abs_path import abs_path

pygame.init()
clicked_statistics = False  # Boolean to track if the statistics button is clicked

class Statistics:
    def __init__(self, x, y, width, height, path, text_lg=None, text_name=None, text_days=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text_lg = text_lg  # Text for logika
        self.text_name = text_name  # Text for name
        self.text_days = text_days  # Text for days
        # Load and scale the background image for statistics
        self.image = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))
        self.image_rect = self.image.get_rect(center=(self.x, self.y))
        # Load and scale the exit icon
        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/iconCross_beige.png')), (40, 40))
        self.exit_rect = self.exit.get_rect(center=(75, 65))
        # Load and scale the logika image
        self.logika_image = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/dollar.png')), (60, 60))
        # Render the logika text
        self.logiki_text = pixel_font.render(self.text_lg, True, (255, 255, 255))
        self.logiki_text_rect = self.logiki_text.get_rect(center=(810, 75))
        # Render the name text
        self.name_text = pixel_font.render(self.text_name, True, (255, 255, 255))
        self.name_text_rect = self.name_text.get_rect(center=(600, 200))
        # Render the days text
        self.days_text = pixel_font.render(self.text_days, True, (255, 255, 255))
        self.days_text_rect = self.days_text.get_rect(center=(600, 250))

    def blit_statistics(self):
        if clicked_statistics:
            # Blit the statistics panel and its contents to the screen
            screen.blit(self.image, self.image_rect)
            screen.blit(self.logiki_text, self.logiki_text_rect)
            screen.blit(self.name_text, self.name_text_rect)
            screen.blit(self.days_text, self.days_text_rect)
            screen.blit(self.exit, self.exit_rect)
            screen.blit(self.logika_image, (620, 45))
