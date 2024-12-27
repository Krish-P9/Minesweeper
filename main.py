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
    pygame.display.set_caption("Minesweeper - Krish Patel")

    '''Constant Variables'''
    hidden_color = (160, 160, 160) #color for hidden tiles
    revealed_color = (96, 96, 96) #color for revealed tiles
    BLACK = (0, 0, 0) #black as RGB
    WHITE = (250, 250, 250) #white as RGB
    FONT = pygame.font.SysFont('Consolas', 50)


    def play(mode):

        board = pygame.Rect((18, 80, 864, 864)) #board for the game
        border = pygame.Rect((13, 75, 874, 874)) #border for game
        #clock = pygame.time.Clock() #delete
        #FPS = 10 #delete

        match mode:
            case 'easy': difficulty = ["Easy", 96, 9, 10]
            case 'medium': difficulty = ["Medium", 54, 16, 40]
            case 'hard': difficulty = ["Hard", 27, 32, 150]
       
        #Dependent on difficulty set
        tile_size = difficulty[1]
        size = difficulty[2]
        matrix = np.full((size, size), "H_")
        mine_num = difficulty[3]
        tiles_left = size * size - mine_num

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
            while count < mine_num: 
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
                state = first_char + second_char
                matrix[ycoord, xcoord] = state #updates matrix
                print(matrix) #delete
                reveal(xpos, ypos, second_char, xcoord, ycoord) #calls reveal() which insertes image if needed


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
        def reveal(xpos, ypos, second_char, xcoord, ycoord):

            nonlocal tiles_left
            pygame.draw.rect(screen, (revealed_color), (xpos, ypos, (tile_size - 1), (tile_size - 1))) #changes tile color to revealed

            #determines which image to insert based on the number under the hidden tile
            match second_char:
                case '0':
                    blank_tile(xcoord, ycoord)
                    tiles_left -= 1
                case 'M': 
                    screen.blit(mine, (xpos, ypos))
                    pygame.display.update()
                    game_over(False)
                case '1': 
                    screen.blit(one, (xpos, ypos))
                    tiles_left = tiles_left - 1
                case '2': 
                    screen.blit(two, (xpos, ypos))
                    tiles_left -= 1
                case '3': 
                    screen.blit(three, (xpos, ypos))
                    tiles_left -= 1
                case '4': 
                    screen.blit(four, (xpos, ypos))
                    tiles_left -= 1
                case '5': 
                    screen.blit(five, (xpos, ypos))
                    tiles_left -= 1
                case '6': 
                    screen.blit(six, (xpos, ypos))
                    tiles_left -= 1
                case '7': 
                    screen.blit(seven, (xpos, ypos))
                    tiles_left -= 1
                case '8': 
                    screen.blit(eight, (xpos, ypos))
                    tiles_left -= 1

            if tiles_left == 0:
                game_over(True)
            print(tiles_left)

        '''Reveals surround tiles around the blank tile'''
        def blank_tile(xcoord, ycoord):

            coord_list = [(xcoord - 1, ycoord + 1), (xcoord, ycoord + 1), (xcoord + 1, ycoord + 1), (xcoord + 1, ycoord), (xcoord + 1, ycoord - 1),(xcoord, ycoord -1), (xcoord - 1, ycoord -1 ), (xcoord - 1, ycoord)]
            print(type(coord_list))
            for j in range(8):
                x = coord_list[j][0]
                y = coord_list[j][1]
                if (0 <= x < size) & (0 <= y < size):
                    x = x * tile_size + 20
                    y = y * tile_size + 82
                    coord = (x, y)
                    left_click(coord)

        def display_text(text, color, font, x, y):

            text = font.render(text, True, color)
            screen.blit(text, (x, y))

        '''Game is over'''
        def game_over(win):

            if win == False:
                pygame.time.delay(1000)
                screen.fill(WHITE)
                display_text(f'Game Over! You Lose', BLACK, FONT, 170, 450)
                pygame.display.update()
            elif win == True:
                pygame.time.delay(1000)
                screen.fill(WHITE)
                display_text(f'Congratulations! You Win', BLACK, FONT, 130, 450)
                pygame.display.update()
            
            pygame.time.delay(2000)
            main_menu()


        populate_board() #populates board with mines and numbers, doesnt actually go here
        screen.fill(WHITE) #background color white
        pygame.draw.rect(screen, hidden_color, board) #draw board
        pygame.draw.rect(screen, BLACK, border, width = 5) #draw border
        draw_grid(tile_size) #draws lines for the grid


        ''' Loop '''
        run = True
        while run:

            # Event Handler
            for event in pygame.event.get():
                # Checks if left or right button on mouse clicked and calls respective function
                if pygame.mouse.get_pressed()[0]: #left click
                    coord = pygame.mouse.get_pos()
                    left_click(coord)
                elif pygame.mouse.get_pressed()[2]: #right click
                    coord = pygame.mouse.get_pos()
                    right_click(coord)

                if event.type == pygame.QUIT: #Exits window
                    run = False


            pygame.display.update()

        pygame.quit()


    def main_menu():
        not_scaled_easy = pygame.image.load("icons/EasyButton.png").convert_alpha()
        not_scaled_normal = pygame.image.load("icons/MediumButton.png").convert_alpha()
        not_scaled_hard = pygame.image.load("icons/HardButton.png").convert_alpha()

        screen.fill(WHITE)
        title_font = pygame.font.SysFont('Consolas', 100)
        subtitle_font = pygame.font.SysFont('Consolas', 60)
        reg_font = pygame.font.SysFont('Consolas', 30)
        title = "Minesweeper"
        subtitle = "By Krish Patel"
        easy_info = "9 x 9 grid"
        easy_info2 = "10 mines"
        medium_info = "16 x 16 grid"
        medium_info2 = "40 mines"
        hard_info = "32 x 32 grid"
        hard_info2 = "150 mines"
        title = title_font.render(title, True, BLACK)
        subtitle = subtitle_font.render(subtitle, True, BLACK)
        easy_info = reg_font.render(easy_info, True, BLACK)
        easy_info2 = reg_font.render(easy_info2, True, BLACK)
        medium_info = reg_font.render(medium_info, True, BLACK)
        medium_info2 = reg_font.render(medium_info2, True, BLACK)
        hard_info = reg_font.render(hard_info, True, BLACK)
        hard_info2 = reg_font.render(hard_info2, True, BLACK)
        screen.blit(title, (150, 200))
        screen.blit(subtitle, (230, 330))
        screen.blit(easy_info, (70, 600))
        screen.blit(easy_info2, (80, 650))
        screen.blit(medium_info, (350, 600))
        screen.blit(medium_info2, (380, 650))
        screen.blit(hard_info, (650, 600))
        screen.blit(hard_info2, (680, 650))

        '''Button Class'''
        class Button():
            def __init__(self, x, y, image, scale):
                width = image.get_width()
                height = image.get_height()
                self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
                self.rect = self.image.get_rect()
                self.rect.topleft = (x, y)
                self.clicked = False

            def draw(self):
              
                action = False
                pos = pygame.mouse.get_pos() #gets position of the mouse

                if self.rect.collidepoint(pos):
                    if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                        action = True

                #draws button on screen
                screen.blit(self.image, (self.rect.x, self.rect.y)) 

                return action


        easy_button = Button(30, 650, not_scaled_easy, 0.2)
        normal_button = Button(330, 650, not_scaled_normal, 0.2)
        hard_button = Button(630, 655, not_scaled_hard, 0.2)

        '''Loop'''
        run = True
        while run:

            #Buttons
            if easy_button.draw():
                play('easy')
            if normal_button.draw():
                play('medium')
            if hard_button.draw():
                play('hard')

            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Exits window
                        run = False
            pygame.display.update()


    main_menu()
'''Refreshes the GUI as you code, also not needed for project'''
if __name__ == "__main__":
    reloader = start_reloader('main.main')
    main()


