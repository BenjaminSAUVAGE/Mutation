import numpy as np
from config.foods_name import FoodsName

from food.food import Food


class Iron(Food):
    
    def __init__(self, pos, concentration):
        super().__init__(
            pos = pos,
            attraction = 5,
            attraction_distance = 10,
            concentration = concentration,
            color = np.array((0.30, 0.08, 0.03)),
            food_name = FoodsName.GLUCOSE
        )