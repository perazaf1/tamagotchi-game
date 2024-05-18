import random
import os
import time
import pygame
import foodClass
import panelClass
import playClass
import statisticsClass
from buttonClass import Button
from mainConst import action, tamagotchiJump, pixel_font,screen
from abs_path import abs_path


pygame.init()
clicked_shop = False
coin_sound = pygame.mixer.Sound(abs_path('sounds/coin.ogg'))

class ShopMenu:
    def __init__(self, x, y, width, height, panel_path, box_path, shop_1_path, shop_2_path, shop_3_path):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.panel = pygame.transform.scale(pygame.image.load(panel_path), (self.width, self.height))
        self.panel_rect = self.panel.get_rect(center=(self.x, self.y))

        self.box_1 = pygame.transform.scale(pygame.image.load(box_path), (150, 150))
        self.box_2 = pygame.transform.scale(pygame.image.load(box_path), (150, 150))
        self.box_3 = pygame.transform.scale(pygame.image.load(box_path), (150, 150))

        self.normal_image = self.box_1

        self.box_1_rect = self.box_1.get_rect(center=(self.x - 250, self.y))
        self.box_2_rect = self.box_2.get_rect(center=(self.x, self.y))
        self.box_3_rect = self.box_3.get_rect(center=(self.x + 250, self.y))

        self.shop_1 = pygame.transform.scale(pygame.image.load(shop_1_path), (100, 100))
        self.shop_2 = pygame.transform.scale(pygame.image.load(shop_2_path), (75, 100))
        self.shop_3 = pygame.transform.scale(pygame.image.load(shop_3_path), (100, 100))

        self.shop_1_rect = self.shop_1.get_rect(center=(self.x - 250, self.y))
        self.shop_2_rect = self.shop_2.get_rect(center=(self.x, self.y - 10))
        self.shop_3_rect = self.shop_3.get_rect(center=(self.x + 250, self.y))

        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/iconCross_beige.png')), (40, 40))
        self.exit_rect = self.exit.get_rect(center=(75, 65))

        self.purchased_items = []

    def bilt_shop_menu(self):
        if clicked_shop :
            screen.blit(self.panel, self.panel_rect)

            screen.blit(self.box_1, self.box_1_rect)
            screen.blit(self.box_2, self.box_2_rect)
            screen.blit(self.box_3, self.box_3_rect)

            screen.blit(self.shop_1, self.shop_1_rect)
            screen.blit(self.shop_2, self.shop_2_rect)
            screen.blit(self.shop_3, self.shop_3_rect)

            screen.blit(self.exit, self.exit_rect)
    
    def hover(self,x,y):
        if self.box_1_rect.collidepoint((x,y)):
            text = pixel_font.render('Prix : 10$ Effets : +2',True, (255,255,255))
            screen.blit(text,(20,120))
            self.box_1 = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonSquare_blue.png')),(150,150))
        else:
            self.box_1 = self.normal_image
        if self.box_2_rect.collidepoint((x, y)):
            text = pixel_font.render('Prix: 20 $ Effets: +8', True, (255, 255, 255))
            screen.blit(text, (270, 120))
            self.box_2 = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonSquare_blue.png')), (150, 150))
        else:
            self.box_2 = self.normal_image
        if self.box_3_rect.collidepoint((x, y)):
            text = pixel_font.render('Prix: 25 $ Effets: +10', True, (255, 255, 255))
            screen.blit(text, (480, 120))
            self.box_3 = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/buttonSquare_blue.png')), (150, 150))
        else:
            self.box_3 = self.normal_image

    def pressed(self,x,y,event):
        if self.box_1_rect.collidepoint((x, y)) and event.type == pygame.MOUSEBUTTONDOWN:
            if action['satisfaction'] + 2 <+ 100 and action['dollars'] - 10 >=0:
                coin_sound.play()
                action['satisfaction'] += 2
                action['boredom'] -= 2
                action['dollars'] -= 10
                self.purchased_items.append((self.shop_1, 10))
        if self.box_2_rect.collidepoint((x, y)) and event.type == pygame.MOUSEBUTTONDOWN:
            if action['satisfaction'] + 8 <= 100 and action['dollars'] - 20 >= 0:
                coin_sound.play()
                action['satisfaction'] += 8
                action['boredom'] -= 6
                action['dollars'] -= 20
                self.purchased_items.append((self.shop_2, 20))
        if self.box_3_rect.collidepoint((x, y)) and event.type == pygame.MOUSEBUTTONDOWN:
            if action['satisfaction'] + 10 <= 100 and action['dollars'] - 25 >= 0:
                coin_sound.play()
                action['satisfaction'] += 10
                action['boredom'] -= 10
                action['dollars'] -= 25
                self.purchased_items.append((self.shop_3, 25))
    
    def draw_purchased_items(self,x,y):
        offset = 50
        for item, _ in self.purchased_items:
            screen.blit(item,(x + offset,y))
            offset += 50



