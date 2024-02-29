#import matplotlib.pyplot as plt
import cv2
import numpy as np

from config.config import SIZE, NUMBER_OF_CELL, NUMBER_OF_TURN
from config.foods_name import FoodsName
from generation import Generation

def launch_simulation(number_of_turn, number_of_cell):
    foods = Generation.food_creation()
    cells = Generation.cell_creation(number_of_cell)
    
    for turn in range(number_of_turn):
        board = np.zeros((SIZE,SIZE,3))
        food_name = FoodsName.GLUCOSE
        for table_of_food in foods[food_name]:
            for food in table_of_food:
                board[food.pos[0], food.pos[1]] = food.color
        for cell in cells:
            cell.moving(foods)
            board[cell.pos[0], cell.pos[1]] = cell.color
        cv2.putText(board, f"turn {turn}", (20,20), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 1)
        cv2.WINDOW_NORMAL
        cv2.imshow("cells", board)
        cv2.waitKey(100)
          

launch_simulation(NUMBER_OF_TURN,NUMBER_OF_CELL)
cv2.waitKey(0)
