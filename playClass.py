import pygame, os
import time
from mainConst import action, tamagotchiJump, pixel_font, screen
from abs_path import abs_path

pygame.init()

animCount = 0  # Animation counter for tamagotchi animation
timeCount = 60  # Initial time count for the game timer
scoreCount = 0  # Initial score count
seconds = 1  # Timer for seconds
clicked_play = False  # Boolean to track if the play button is clicked

class Play:
    def __init__(self):
        self.x = 400
        self.y = 560
        self.width = 180
        self.height = 180
        # Load and scale the background image
        self.background = [pygame.transform.scale(pygame.image.load(abs_path('images/backgrounds/game.jpg')),(1080,720))]
        # Load and scale the exit icon
        self.exit = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/iconCross_beige.png')), (40, 40))
        self.exit_rect = self.exit.get_rect(center=(40, 40))

    def blit_play(self):
        global animCount
        if clicked_play:
            # Animation logic
            if animCount + 1 >= len(self.background) * 7:
                animCount = 0
                screen.blit(self.background[0], (0, 0))
                screen.blit(tamagotchiJump[0], (self.x, self.y))
            else:
                screen.blit(self.background[animCount // 7], (0, 0))
                screen.blit(tamagotchiJump[animCount // 7], (self.x, self.y))
                animCount += 1

        # Render and blit the time and score onto the screen
        time_left = pixel_font.render(f'Temps: {timeCount}', True, (230, 255, 255))
        score = pixel_font.render(f'Score: {scoreCount}', True, (255, 255, 255))
        screen.blit(score, (900, 70))
        screen.blit(time_left, (900, 100))
        screen.blit(self.exit, self.exit_rect)

    def check_time(self, game_time):
        global clicked_play, timeCount, scoreCount, seconds
        t_time = time.time() - game_time
        if seconds < t_time:
            timeCount -= 1
            seconds += 1
        if timeCount == 0:
            action['dollars'] += scoreCount // 2
            if action['satisfaction'] + 15 > 100:
                score = 100 - action['satisfaction']
                action['satisfaction'] += score
            else:
                action['satisfaction'] += 15
            action['satisfaction'] -= 2
            clicked_play = False
            timeCount = 60
            seconds = 1
            scoreCount = 0
            pygame.mixer.music.unload()
            pygame.mixer.music.load(abs_path('sounds/bgMusic.ogg'))
            pygame.mixer.music.play(loops=-1)

    def control(self, keys):
        if keys[pygame.K_LEFT] and self.x > 1:
            self.x -= 9
        if keys[pygame.K_RIGHT] and self.x < 800 - self.width:
            self.x += 9

class Basket(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Load and scale the basket image
        self.basket = pygame.transform.scale(pygame.image.load(abs_path('images/sprites/basket.png')), (180 // 2, 180 // 3))
        self.rect = self.basket.get_rect(center=(480, 580))

    def blit_basket(self):
        screen.blit(self.basket, self.rect)

    def control(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 35:
            self.rect.x -= 9
        if keys[pygame.K_RIGHT] and self.rect.x < 690:
            self.rect.x += 9

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, speed, filename, group):
        pygame.sprite.Sprite.__init__(self)
        # Load and scale the coin image
        self.image = pygame.transform.scale(pygame.image.load(filename), (30, 30))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed
        self.add(group)

    def update(self, height):
        if self.rect.y < height - 20:
            self.rect.y += self.speed
        else:
            self.kill()
