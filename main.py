'''
Minesweeper by Krish Patel
Personal Project
Created December 2024
'''

import pygame
import numpy as np
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

    #Dependent on difficulty set
    tile_size = easy_tile_size #tile size set to easy for now 
    matrix = np.full((9,9), 'H', dtype = str) #matrix that represents the state of the game, size for easy mode for now
    max_x = 8
    max_y = 8 #max x and y value for coordinate of tiles, set to easy for now

    hidden_color = (160, 160, 160) #color for hidden tiles
    revealed_color = (96, 96, 96) #color for revealed tiles
    BLACK = (0, 0, 0) #black as RGB

    '''Function to draw lines for grid'''
    def draw_grid(tile_size):

        # Draws Horizontal Lines
        for x in range(18 + tile_size, 882, tile_size):
            pygame.draw.line(screen, BLACK, (x, 80), (x, 944))
        # Draws Vertical Lines
        for y in range(80 + tile_size, 944, tile_size):
            pygame.draw.line(screen, BLACK, (18, y), (882, y))


    screen.fill((250, 250, 250)) #background color white
    pygame.draw.rect(screen, hidden_color, board) #draw board
    pygame.draw.rect(screen, BLACK, border, width = 5) #draw border
    draw_grid(tile_size) #draws lines for the grid


    def left_click(coord):

        #create variable valid to see if click is valid

        xcoord = (coord[0] - 18) // tile_size
        ycoord = (coord[1] - 80) // tile_size

        # print(str(xcoord) + ", " + str(ycoord)) # delete

        if not(0 <= xcoord <= max_x) or (not(0 <= ycoord <= max_y)): #checks if the coordinate of the click is on the board
            pass
        elif matrix[xcoord, ycoord] == 'H':
            print("Revealed")
        

    def get_coord(coord):
            pass


    ''' Loop '''
    run = True
    while run:

        # screen.fill((250, 250, 250)) #background color white
        # pygame.draw.rect(screen, hidden_color, board) #draw board
        # pygame.draw.rect(screen, BLACK, border, width = 5) #draw border
        # draw_grid(tile_size) #draws lines for the grid

        # Event Handler
        for event in pygame.event.get():
            # Checks if left or right button on mouse clicked and calls respective function
            if pygame.mouse.get_pressed()[0]: #left click
                print("left click") #delete
                # print(str(pygame.mouse.get_pos())) #delete
                coord = pygame.mouse.get_pos()
                left_click(coord)
            elif pygame.mouse.get_pressed()[2]: #right click
                print("right click") # delete
                # print(str(pygame.mouse.get_pos())) # delete
                coord = pygame.mouse.get_pos()
                #call right click function

            if event.type == pygame.QUIT: #Exits window
                run = False

        pygame.display.update()

    pygame.quit()




'''Refreshes the GUI as you code, also not needed for project'''
if __name__ == "__main__":
    reloader = start_reloader('main.main')
    main()


