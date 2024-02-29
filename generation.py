import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import generate_fractal_noise_2d

from cell import Cell
from config.config import *
from config.foods_list import FOODS_LIST
from config.foods_name import FoodsName

class Generation() :
    
    @staticmethod
    def food_creation():
        foods = dict()

        for food, solubility, food_name in FOODS_LIST:
            foods[food_name] = [[food((x,y), 0) for x in range(SIZE)] for y in range(SIZE)]
            noise = generate_fractal_noise_2d(shape = (SIZE, SIZE), res = (RES, RES), octaves = OCTAVES, persistence = solubility)
            noise[noise < 0] = 0
            for x in range(noise.shape[0]):
                for y in range(noise.shape[1]):
                    if(noise[x,y] > 0):
                        foods[food_name][x][y] = food((x,y), noise[x,y])
        return foods
    
    @staticmethod
    def cell_creation(number_of_cell):
        cells = []
        for _ in range(number_of_cell):
            color = np.array((1.0,0.2,0.2))
            pos = (np.random.randint(0,SIZE-1), np.random.randint(0,SIZE-1))
            cells.append(Cell(color, pos))
        return np.array(cells)
