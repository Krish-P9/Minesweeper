'''
Minesweeper by Krish Patel
Personal Project
Created December 2024
'''

import pygame
import numpy as np
import random
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

    #switch case to check which difficulty chosen, then set the values for difficulty
    #difficulty = ["Easy", 96, 9, 8, 10]
    #...

    easy_tile_size = 96, 9, 10
    normal_tile_size = 54, 16, 40
    hard_tile_size = 27, 32, 150

    difficulty = ["Easy", 96, 9, 10] #stores values for certain difficulty, ["difficulty", tile_size, size of matrix, max x and y value, number of mines]
    # difficulty = ["Hard", 27, 32, 150]

    #Dependent on difficulty set
    tile_size = difficulty[1]
    size = difficulty[2]
    matrix = np.full((size, size), "H_")
    mine_num = difficulty[3]

    # tile_size = easy_tile_size #tile size set to easy for now 
    # matrix = np.full((9,9), 'H', dtype = str) #matrix that represents the state of the game, size for easy mode for now
    # max_x = 8
    # max_y = 8 #max x and y value for coordinate of tiles, set to easy for now

    '''Color and Icon Variables'''
    hidden_color = (160, 160, 160) #color for hidden tiles
    revealed_color = (96, 96, 96) #color for revealed tiles
    BLACK = (0, 0, 0) #black as RGB
    #images not scaled
    not_scaled_mine = pygame.image.load("icons/Mine.png").convert_alpha()
    not_scaled_flag = pygame.image.load("icons/Flag.png").convert_alpha()
    not_scaled_one = pygame.image.load("icons/1.png").convert_alpha()
    not_scaled_two = pygame.image.load("icons/2.png").convert_alpha()
    not_scaled_three = pygame.image.load("icons/3.png").convert_alpha()
    not_scaled_four = pygame.image.load("icons/4.png").convert_alpha()
    not_scaled_five = pygame.image.load("icons/5.png").convert_alpha()
    not_scaled_six = pygame.image.load("icons/6.png").convert_alpha()
    not_scaled_seven = pygame.image.load("icons/7.png").convert_alpha()
    not_scaled_eight = pygame.image.load("icons/8.png").convert_alpha()
    #images scaled to appropriate size
    mine = pygame.transform.scale(not_scaled_mine, (tile_size, tile_size))
    flag = pygame.transform.scale(not_scaled_flag, (tile_size, tile_size))
    one = pygame.transform.scale(not_scaled_one, (tile_size, tile_size))
    two = pygame.transform.scale(not_scaled_two, (tile_size, tile_size))
    three = pygame.transform.scale(not_scaled_three, (tile_size, tile_size))
    four = pygame.transform.scale(not_scaled_four, (tile_size, tile_size))
    five = pygame.transform.scale(not_scaled_five, (tile_size, tile_size))
    six = pygame.transform.scale(not_scaled_six, (tile_size, tile_size))
    seven = pygame.transform.scale(not_scaled_seven, (tile_size, tile_size))
    eight = pygame.transform.scale(not_scaled_eight, (tile_size, tile_size))


    '''Draws lines for grid'''
    def draw_grid(tile_size):

        # Draws Horizontal Lines
        for x in range(18 + tile_size, 882, tile_size):
            pygame.draw.line(screen, BLACK, (x, 80), (x, 944))
        # Draws Vertical Lines
        for y in range(80 + tile_size, 944, tile_size):
            pygame.draw.line(screen, BLACK, (18, y), (882, y))


    '''Populates board with mines and appropriate numbers'''
    def populate_board():
        '''Mines'''
        count = 0 #number of mines already on board

        #loop to randomly place the mines on the board
        while count < mine_num + 1: 
            val = random.randint(0, size * size - 1)
            minex = val // size #x value of mine going to be placed
            miney = val % size #y value of mine going to be placed
            minex_pos = minex * tile_size + 19
            miney_pos = miney * tile_size + 81
            if matrix[miney, minex] != "HM":
                matrix[miney, minex] = "HM"
                screen.blit(mine, (minex_pos, miney_pos))
                count += 1

        '''Numbers'''

        for row in range(size):
            for col in range(size):

                number = 0
                top = False
                bottom = False
                right = False
                left = False

                #checks if tile around position exists
                if 0 <= (row - 1):
                    top = True
                if 0 <= (col - 1):
                    left = True
                if (row + 1) < size:
                    bottom = True
                if (col + 1) < (size):
                    right = True

                if matrix[col, row] == "HM": #mine found at position
                    continue

                if not(top): pass #checks if position above doenst exist
                elif(matrix[col, row - 1] == "HM"): #check above for mine
                    number += 1
                if not(top & right): pass
                elif (matrix[col + 1, row - 1] == "HM"): # check top right
                    number += 1
                if not(right): pass
                elif (matrix[col + 1, row] == "HM"): #check right
                    number += 1
                if not(bottom & right): pass
                elif (matrix[col + 1, row + 1] == "HM"): #check bottom right
                    number += 1
                if not(bottom): pass
                elif (matrix[col, row + 1] == "HM"): #check below
                    number += 1
                if not(bottom & left): pass
                elif (matrix[col - 1, row + 1] == "HM"): # check bottom left
                    number += 1
                if not(left): pass
                elif (matrix[col - 1, row] == "HM"): #check left
                    number += 1
                if not(top & left): pass
                elif (matrix[col - 1, row - 1] == "HM"): #check top left
                    number += 1

                #position of icon #delete
                numx_pos = col * tile_size + 81
                numy_pos = row * tile_size + 19

                matrix[col, row] = "H" + str(number)


        print(matrix)


    '''Left Click'''
    def left_click(coord):

        xcoord = (coord[0] - 18) // tile_size #x coordinate of the tile clicked
        ycoord = (coord[1] - 80) // tile_size #y coordinate of the tile clicked
        xpos = xcoord * tile_size + 19 #x position
        ypos = ycoord * tile_size + 81 #y position

        state = matrix[ycoord, xcoord] #gets state of the tile
        first_char = state[0] #stores value of first letter, shows if tile is hidden, revealed or flagged
        second_char = state[1] #stores the second character

        if not(0 <= xcoord < size) or (not(0 <= ycoord < size)): #checks if the coordinate of the click is on the board
            pass
        elif first_char == 'H': #if tile is hidden, turn it to revealed
            first_char = "R"
            pygame.draw.rect(screen, (revealed_color), (xpos, ypos, (tile_size - 1), (tile_size - 1))) #changes tile color to revealed
            reveal(xpos, ypos, second_char) #calls reveal() which insertes image if needed
            state = first_char + second_char
            matrix[ycoord, xcoord] = state #updates matrix
            print(matrix) #delete

    '''Right Click'''
    def right_click(coord):

        xcoord = (coord[0] - 18) // tile_size #x coordinate of the tile clicked
        ycoord = (coord[1] - 80) // tile_size #y coordinate of the tile clicked
        xpos = xcoord * tile_size + 19 #x position
        ypos = ycoord * tile_size + 81 #y position

        state = matrix[ycoord, xcoord] #gets state of the tile
        first_char = state[0] #stores value of first letter, shows if tile is hidden, revealed or flagged
        second_char = state[1] #stores the second character

        #checks if the tile is hidden, then flags it, or if it flagged, then unflags it
        if first_char == "H": 
            first_char = "F"
            screen.blit(flag, (xpos, ypos))
        elif first_char == "F":
            first_char = "H"
            pygame.draw.rect(screen, (hidden_color), (xpos, ypos, (tile_size - 1), (tile_size - 1)))

        state = first_char + second_char
        matrix[ycoord, xcoord] = state #updates matrix 
        print(matrix) # delete


    '''Reveals what the tile is when clicked'''
    def reveal(xpos, ypos, second_char):

        match second_char:
            case '_': pass
            case 'M': 
                screen.blit(mine, (xpos, ypos))
                print("Game Over")
            case '1': screen.blit(one, (xpos, ypos))
            case '2': screen.blit(two, (xpos, ypos))
            case '3': screen.blit(three, (xpos, ypos))
            case '4': screen.blit(four, (xpos, ypos))
            case '5': screen.blit(five, (xpos, ypos))
            case '6': screen.blit(six, (xpos, ypos))
            case '7': screen.blit(seven, (xpos, ypos))
            case '8': screen.blit(eight, (xpos, ypos))
        

    #populate_board() actually goes here
    screen.fill((250, 250, 250)) #background color white
    pygame.draw.rect(screen, hidden_color, board) #draw board
    pygame.draw.rect(screen, BLACK, border, width = 5) #draw border
    populate_board() #populates board with mines and numbers, doesnt actually go here
    draw_grid(tile_size) #draws lines for the grid
    
    
    ''' Loop '''
    run = True
    while run:
        #delete
        # screen.fill((250, 250, 250)) #background color white
        # pygame.draw.rect(screen, hidden_color, board) #draw board
        # pygame.draw.rect(screen, BLACK, border, width = 5) #draw border
        # draw_grid(tile_size) #draws lines for the grid

        # Event Handler
        for event in pygame.event.get():
            # Checks if left or right button on mouse clicked and calls respective function
            if pygame.mouse.get_pressed()[0]: #left click
                # print("left click") #delete
                # print(str(pygame.mouse.get_pos())) #delete
                coord = pygame.mouse.get_pos()
                left_click(coord)
            elif pygame.mouse.get_pressed()[2]: #right click
                # print("right click") # delete
                # print(str(pygame.mouse.get_pos())) # delete
                coord = pygame.mouse.get_pos()
                right_click(coord)

            if event.type == pygame.QUIT: #Exits window
                run = False

        pygame.display.update()

    pygame.quit()




'''Refreshes the GUI as you code, also not needed for project'''
if __name__ == "__main__":
    reloader = start_reloader('main.main')
    main()


