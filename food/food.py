import numpy as np

class Food():
    
    def __init__(self, pos, attraction, attraction_distance, concentration, color, food_name):
        self._pos = np.array(pos)
        self._attraction = attraction
        self._attraction_distance = attraction_distance
        self._concentration = concentration
        self._color = color
        self._food_name = food_name
        
    @property            
    def pos(self):
        return self._pos
    
    @property
    def attraction(self):
        return self._attraction
    
    @property
    def attraction_distance(self):
        return self._attraction_distance
    
    @property 
    def concentration(self):
        return self._concentration
    
    @concentration.setter
    def number_of_use(self, new_number_of_use):
        self._number_of_use = new_number_of_use
    
    @property
    def color(self):
        if(self._concentration > 0 ):
            return self._color
        else:
            return np.array((0.0,0.0,0.0))
    
    @property
    def food_name(self):
        return self._food_name
