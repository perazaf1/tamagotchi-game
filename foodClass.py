import pygame, os
from mainConst import action, screen, pixel_font
from abs_path import abs_path

pygame.init()

clicked_feed = False
coin_sound = pygame.mixer.Sound(abs_path('sounds/coin.ogg'))

class FoodMenu:
    def __init__(self, x, y, width, height, panel_path, box_path, food_1_path, food_2_path, food_3_path):
        # Initialize the attributes of the food menu
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Load and scale the panel image
        self.panel = pygame.transform.scale(pygame.image.load(panel_path), (self.width, self.height))
        self.panel_rect = self.panel.get_rect(center=(self.x, self.y))

        # Load and scale the box images for food items
        self.box_1 = pygame.transform.scale(pygame.image.load(box_path), (150, 150))
        self.box_2 = pygame.transform.scale(pygame.image.load(box_path), (150, 150))
        self.box_3 = pygame.transform.scale(pygame.image.load(box_path), (150, 150))

        self.normal_image = self.box_1

        # Set the positions of the boxes
        self.box_1_rect = self.box_1.get_rect(center=(self.x - 250, self.y))
        self.box_2_rect = self.box_2.get_rect(center=(self.x, self.y))
        self.box_3_rect = self.box_3.get_rect(center=(self.x + 250, self.y))

        # Load and scale the images for food items
        self.food_1 = pygame.transform.scale(pygame.image.load(food_1_path), (100, 100))
        self.food_2 = pygame.transform.scale(pygame.image.load(food_2_path), (75, 100))
        self.food_3 = pygame.transform.scale(pygame.image.load(food_3_path), (100, 100))

        # Set the positions of the food item images
        self.food_1_rect = self.food_1.get_rect(center=(self.x - 250, self.y))
        self.food_2_rect = self.food_2.get_rect(center=(self.x, self.y - 10))
        self.food_3_rect = self.food_3.get_rect(center=(self.x + 250, self.y))

        # Load and scale the exit icon
        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/iconCross_beige.png')), (40, 40))
        self.exit_rect = self.exit.get_rect(center=(75, 65))

    def blit_food_menu(self):
        # Draw the food menu if clicked_feed is True
        if clicked_feed:
            screen.blit(self.panel, self.panel_rect)

            screen.blit(self.box_1, self.box_1_rect)
            screen.blit(self.box_2, self.box_2_rect)
            screen.blit(self.box_3, self.box_3_rect)

            screen.blit(self.food_1, self.food_1_rect)
            screen.blit(self.food_2, self.food_2_rect)
            screen.blit(self.food_3, self.food_3_rect)

            screen.blit(self.exit, self.exit_rect)

    def hover(self, x, y):
        # Change the appearance of the box when hovered over and display relevant text
        if self.box_1_rect.collidepoint((x, y)):
            text = pixel_font.render('Price: $5 Effects: +3', True, (255, 255, 255))
            screen.blit(text, (20, 120))
            self.box_1 = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonSquare_blue.png')), (150, 150))
        else:
            self.box_1 = self.normal_image
        if self.box_2_rect.collidepoint((x, y)):
            text = pixel_font.render('Price: $10 Effects: +6', True, (255, 255, 255))
            screen.blit(text, (270, 120))
            self.box_2 = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonSquare_blue.png')), (150, 150))
        else:
            self.box_2 = self.normal_image
        if self.box_3_rect.collidepoint((x, y)):
            text = pixel_font.render('Price: $15 Effects: +10', True, (255, 255, 255))
            screen.blit(text, (480, 120))
            self.box_3 = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonSquare_blue.png')), (150, 150))
        else:
            self.box_3 = self.normal_image

    def pressed(self, x, y, event):
        # Process the button presses for purchasing food items
        if self.box_1_rect.collidepoint((x, y)) and event.type == pygame.MOUSEBUTTONDOWN:
            if action['satisfaction'] + 3 <= 100 and action['dollars'] - 5 >= 0:
                coin_sound.play()
                action['satisfaction'] += 3
                action['toilet'] -= 3
                action['dollars'] -= 5
        if self.box_2_rect.collidepoint((x, y)) and event.type == pygame.MOUSEBUTTONDOWN:
            if action['satisfaction'] + 6 <= 100 and action['dollars'] - 10 >= 0:
                coin_sound.play()
                action['satisfaction'] += 6
                action['toilet'] -= 6
                action['dollars'] -= 10
        if self.box_3_rect.collidepoint((x, y)) and event.type == pygame.MOUSEBUTTONDOWN:
            if action['satisfaction'] + 10 <= 100 and action['dollars'] - 15 >= 0:
                coin_sound.play()
                action['satisfaction'] += 10
                action['toilet'] -= 10
                action['dollars'] -= 15
