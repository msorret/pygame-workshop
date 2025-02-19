import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame

import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 300
GROUND_HEIGHT = HEIGHT - 40
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DINO_COLOR = (50, 168, 82)
CACTUS_COLOR = (200, 50, 50)
GRAVITY = 0.5
JUMP_STRENGTH = -10

# Screen Setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Run")
