#! python3
## This program will win any sized game of Minesweeper.

import pyautogui as pag
import random
import pprint

pag.FAILSAFE = True
pag.PAUSE = 0.025


top_corner = r"C:\my_python_scripts\MinesweeperBot\top_corner.png"
bottom_corner = r"C:\my_python_scripts\MinesweeperBot\bottom_corner.png"

board_left = int(pag.locateOnScreen(top_corner)[0]+9)
board_top = int(pag.locateOnScreen(top_corner)[1]+8)
board_right = int(pag.locateOnScreen(bottom_corner)[0]+9)
board_bottom = int(pag.locateOnScreen(bottom_corner)[1]+11)
board_width = board_right - board_left+1
board_height = board_bottom - board_top+1
board_space = (board_left, board_top, board_width, board_height)

#Mouse traces around the board, to demonstrate that it has successfully located
#the game. Then prints out the coordinates and width, height of the game.
#These numbers can be checked using the mouse_pos script.
#pag.moveTo(board_left, board_top)
#pag.moveTo(board_right, board_top, duration=0.5)
#pag.moveTo(board_right, board_bottom, duration=0.5)
#pag.moveTo(board_left, board_bottom, duration=0.5)
#pag.moveTo(board_left, board_top, duration=0.5)
print(board_space)

#Create the multi-D array to contain the position and type of each block.
class Block:
    Position = ()
    State = int()

Rows = int(board_height/16)
Columns = int(board_width/16)

Blocks = []
for i in range(int(Rows)):
    Blocks.append([])
    for j in range(Columns):
        Blocks[i].append([])
        Blocks[i][j] = Block()

        x = board_left + (16*j)
        y = board_top + (16*i)
        
        Blocks[i][j].Position = (x, y, 16, 16)
        Blocks[i][j].State = 0
        pag.moveTo(Blocks[i][j].Position)
        print(str(Blocks[i][j].Position) + str(Blocks[i][j].State))
