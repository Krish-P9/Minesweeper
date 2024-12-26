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
    easy_tile_size = 96
    normal_tile_size = 54
    hard_tile_size = 27
    tile_size = easy_tile_size #tile size set to easy for now 

    ''' Color variables '''
    hidden_color = (160, 160, 160)
    revealed_color = (96, 96, 96)
    BLACK = (0, 0, 0)

    '''Function to draw lines for grid'''
    def draw_grid(tile_size):

        ''' Draws Horizontal Lines '''
        for x in range(18 + tile_size, 882, tile_size):
            pygame.draw.line(screen, BLACK, (x, 80), (x, 944))
        ''' Draws Vertical Lines '''
        for y in range(80 + tile_size, 944, tile_size):
            pygame.draw.line(screen, BLACK, (18, y), (882, y))

    ''' Loop '''
    run = True
    while run:

        screen.fill((250, 250, 250)) #background color white
        pygame.draw.rect(screen, hidden_color, board) #draw board
        pygame.draw.rect(screen, BLACK, border, width = 5) #draw border
        draw_grid(tile_size) #draws lines for the grid

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


