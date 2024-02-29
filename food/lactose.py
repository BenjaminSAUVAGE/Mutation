import numpy as np
from config.foods_name import FoodsName

from food.food import Food


class Lactose(Food):
    
    def __init__(self, pos, concentration):
        super().__init__(
            pos = pos,
            attraction = 3,
            attraction_distance = 10,
            concentration = concentration,
            color = np.array((1.0, 0.24, 0.71)),
            food_name = FoodsName.LACTOSE
        )
