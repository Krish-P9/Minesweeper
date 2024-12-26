'''
Minesweeper by Krish Patel
Personal Project
Created December 2024
'''

import pygame
from hupper import start_reloader #not needed for this project, auto updates GUI as changes are made

def main():
    pygame.init()

    ''' Window Setup '''
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 950
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Krish Minesweeper")

    board = pygame.Rect((18, 80, 864, 864)) #board for the game
    border = pygame.Rect((13, 75, 874, 874)) #border for game
    # tile_size = 

    #Color variables
    hidden_color = (160, 160, 160)
    revealed_color = (96, 96, 96)
    BLACK = (0, 0, 0)

    ''' Loop '''
    run = True
    while run:

        screen.fill((250, 250, 250)) #background color white
        pygame.draw.rect(screen, hidden_color, board)
        pygame.draw.rect(screen, BLACK, border, width = 5)

        ''' Event Handler '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

'''Refreshes the GUI as you code, also not needed for project'''
if __name__ == "__main__":
    reloader = start_reloader('test.main')
    main()








'''
Minesweeper by Krish Patel
Personal Project
Created December 2024
'''

import pygame
from hupper import start_reloader #not needed for this project, auto updates GUI as changes are made

def main():
    pygame.init()

    ''' Window Setup '''
    SCREEN_WIDTH = 720
    SCREEN_HEIGHT = 810
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Krish Minesweeper")

    board = pygame.Rect((10, 100, 700, 700)) #board for the game
    border = pygame.Rect((5, 95, 710, 710)) #border for game
    # tile_size = 

    #Color variables
    hidden_color = (160, 160, 160)
    revealed_color = (96, 96, 96)
    BLACK = (0, 0, 0)

    ''' Loop '''
    run = True
    while run:

        screen.fill((250, 250, 250)) #background color white
        pygame.draw.rect(screen, hidden_color, board)
        pygame.draw.rect(screen, BLACK, border, width = 5)

        ''' Event Handler '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()

'''Refreshes the GUI as you code, also not needed for project'''
if __name__ == "__main__":
    reloader = start_reloader('main.main')
    main()
