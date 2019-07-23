#! python3
## This program will win any sized game of Minesweeper.

import pyautogui as pag
import random
import pprint

pag.FAILSAFE = True
pag.PAUSE = 0.5

unclickedpng = r"C:\my_python_scripts\MinesweeperBot\unclicked.png"
clicked_1 = r"c:\my_python_scripts\MinesweeperBot\clicked_1.png"
clicked_2 = r"C:\my_python_scripts\MinesweeperBot\clicked_2.png"
clicked_3 = r"C:\my_python_scripts\MinesweeperBot\clicked_3.png"
clicked_4 = r"C:\my_python_scripts\MinesweeperBot\clicked_4.png"
clicked_5 = r"C:\my_python_scripts\MinesweeperBot\clicked_5.png"
clicked_6 = r"C:\my_python_scripts\MinesweeperBot\clicked_6.png"
face = r"C:\my_python_scripts\MinesweeperBot\face.png"
flag = r"C:\my_python_scripts\MinesweeperBot\flag.png"
dead = r"C:\my_python_scripts\MinesweeperBot\gameover.png"
empty = r"C:\my_python_scripts\MinesweeperBot\emptyclicked.png"

unclicked = list(pag.locateAllOnScreen(unclickedpng))
board_left = unclicked[0][0]
board_top = unclicked[0][1]
board_right = unclicked[-1][0] + 16
board_bottom = unclicked[-1][1] + 16
board_width = board_right - board_left
board_height = board_bottom - board_top
board_space = (board_left, board_top, board_width, board_height)

def click_random():
    random_choice = random.choice(unclicked)
    pag.doubleClick(pag.center(random_choice))
    unclicked.remove(random_choice)

#Click 5 random blocks, hopefully until a decent sized open space is created in the grid.
for i in range(5):
    click_random()

#Scan the board and put all block types in their own lists. MAKE THIS INTO A FUNCTION??
pag.moveTo(board_left - 100)
empty_blocks = list(pag.locateAllOnScreen(empty))
ones = list(pag.locateAllOnScreen(clicked_1, region=(board_space)))
twos = list(pag.locateAllOnScreen(clicked_2, region=(board_space)))
threes = list(pag.locateAllOnScreen(clicked_3, region=(board_space)))
fours = list(pag.locateAllOnScreen(clicked_4, region=(board_space)))
fives = list(pag.locateAllOnScreen(clicked_5, region=(board_space)))
sixes = list(pag.locateAllOnScreen(clicked_6, region=(board_space)))

#Sanity check, print the amount of each type of block that is present.
pprint.pprint(str(len(empty_blocks)) + ' empty block(s)')
pprint.pprint(str(len(ones)) + ' ones')
pprint.pprint(str(len(twos)) + ' twos')
pprint.pprint(str(len(threes)) + ' threes')
pprint.pprint(str(len(fours)) + ' fours')
pprint.pprint(str(len(fives)) + ' fives')
pprint.pprint(str(len(sixes)) + ' sixes')
