import pygame, os
from mainConst import screen, pixel_font
from abs_path import abs_path

pygame.init()

class Button:
    def __init__(self, x, y, width, height, path, text=None):
        # Initialize button attributes
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        # Load and scale button image
        self.image = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))
        self.normal_image = self.image
        # Set the position of the button rectangle
        self.rect = self.image.get_rect(center=(self.x, self.y))

        # Render button text
        self.btn_text = pixel_font.render(self.text, True, (255, 255, 255))
        self.btn_text_rect = self.btn_text.get_rect()
        self.btn_text_rect.center = self.rect.center

    def blit_btn(self):
        # Blit the button image and text onto the screen
        screen.blit(self.image, self.rect)
        screen.blit(self.btn_text, self.btn_text_rect)

    def hover(self, x, y):
        # Change button appearance when hovered over
        if self.rect.collidepoint((x, y)):
            self.image = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonLong_blue.png')), (self.width, self.height))
        else:
            self.image = self.normal_image
