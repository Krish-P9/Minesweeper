'''
Minesweeper by Krish Patel
Personal Project
Created December 2024
'''

import pygame

pygame.init()

# Window Setup
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Krish Minesweeper")

# Loop
run = True
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()
