import matplotlib.pyplot as plt
import numpy as np
from perlin_numpy import generate_fractal_noise_2d
from config.config import *
from config.foods_list import FOODS_LIST
from config.foods_name import FoodsName




board = np.zeros((SIZE,SIZE,3))
foods = dict()

for food, solubility, food_name in FOODS_LIST:
    foods[food_name] = []
    noise = generate_fractal_noise_2d(shape = (SIZE, SIZE), res = (RES, RES), octaves = OCTAVES, persistence = solubility)
    noise[noise < 0] = 0
    for x in range(noise.shape[0]):
        for y in range(noise.shape[1]):
            if(noise[x,y] > 0):
                foods[food_name].append(food((x,y), noise[x,y]))
food_name = FoodsName.GLUCOSE
for food in foods[food_name]:
    board[food.pos[0], food.pos[1]] = food.color   
plt.figure()
plt.imshow(board)
plt.show()

