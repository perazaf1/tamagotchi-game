import pygame, os
from abs_path import abs_path

# Initialize Pygame
pygame.init()

# Set the width and height for the Tamagotchi images
width = 150
height = 150

# Dictionary to store the initial values of different actions
action = {'satisfaction': 200, 'toilet': 200, 'boredom': 200, 'health': 200, 'dollars': 250}

# Set the screen size for the Pygame window
screen = pygame.display.set_mode((800, 500))

# Load the pixel font with a size of 27
pixel_font = pygame.font.Font(abs_path('font/Kanit-Black.ttf'), 27)

# Load and scale the Tamagotchi jump animation frames
tamagotchiJump = [
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-0.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-1.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-2.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-3.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-4.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-5.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-6.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation/tamagotchi-7.png')), (width, height))
]

# Load and scale the second set of Tamagotchi jump animation frames
tamagotchiJump2 = [
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-0.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-1.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-2.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-3.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-4.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-5.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-6.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 2/tamagotchi-7.png')), (width, height))
]

# Load and scale the third set of Tamagotchi jump animation frames
tamagotchiJump3 = [
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-0.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-1.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-2.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-3.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-4.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-5.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-6.png')), (width, height)),
    pygame.transform.scale(pygame.image.load(abs_path('images/sprites/tamagotchi animation 3/tamagotchi-7.png')), (width, height))
]
