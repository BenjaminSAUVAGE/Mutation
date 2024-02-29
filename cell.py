import math
import types
from attr import NOTHING

import numpy as np
from config.foods_name import FoodsName
from organelles.movers.flagelle import Flagelle
from config.organelles_type import OrganellesTypes
from organelles.movers.mover import Mover
from organelles.sensors.glucose_sensor import GlucoseSensor

from config.config import SIZE
from config.sensors_chance import SENSOR_LIST
from organelles.organelle import Organelle
from organelles.sensors.lactose_sensor import LactoseSensor
from organelles.sensors.sensor import Sensor


class Cell:
      
    def __init__(self, color, pos):
        self.color = color
        self.pos = np.array(pos)
        self.life_duration = 100
        self.speed = 1
        self.energy = 100
        self.organelles: Organelle = {OrganellesTypes.SENSOR: [], 
                                      OrganellesTypes.MOVER: None}
        self._organelles_fill()
        
    def _organelles_fill(self):
        for sensor,chance in SENSOR_LIST:
            if(np.random.rand() < chance):
                self.organelles[OrganellesTypes.SENSOR].append(sensor())
        self.organelles[OrganellesTypes.MOVER] = Flagelle(2)
        
    def mutation(self):
        newCell = Cell(((self.color *np.random.rand(3)+1)/2), 
                       pos = (np.random.randint(0, SIZE), np.random.randint(0, SIZE)))
        return newCell
    
    
    def get_organelles(self):
        assert all(isinstance(organelle, Organelle) for organelle in self.organelles), "the list is not only composed of Organelle"
        for organelle in self.organelles:
            organelle.getCarac()


    def set_organelles(self, new_organelle):
        assert isinstance(new_organelle, Organelle), "the modification is not an Organelle"
        self.organelles.append(new_organelle)
    
    
    def sense(self, food_name):
        for sensor in self.organelles[OrganellesTypes.SENSOR]:
            if(sensor.what_can_be_sense == food_name):
                return sensor
        return Sensor("default", 0, 0, None)


    def distance_calculation(self, foods):
        dist = math.inf
        min_pos = (self.pos[0],self.pos[1])
        max_concentration = -math.inf
        attraction = -math.inf
        for food_name in FoodsName:
            table_of_food = foods[food_name]
            sensor_range = self.sense(food_name).range
            cell_pos = self.pos
            for x in range(0, sensor_range):
                for y in range(0, sensor_range):
                    food = table_of_food[min(cell_pos[0]+ x, SIZE-1)][min(cell_pos[1] + y, SIZE-1)]
                    if(max_concentration < food.concentration and attraction <= food.attraction):
                        max_concentration = food.concentration
                        attraction = food.attraction
                        dist = np.sqrt(np.sum(np.square(food.pos - cell_pos)))
                        min_pos = food.pos
                
        return dist, min_pos

    #To move the cell
    def moving(self, foods):
        """
        Move a cell to a position 
        :param foods: the list of food in the board
        :type foods: list
        """
        speed = 1 + self.organelles[OrganellesTypes.MOVER].speed 
        move_x = 0
        move_y = 0
        
        min_dist, min_pos = self.distance_calculation(foods)

        if(min_dist is math.inf):
            if(self.pos[0] >= 0 ):
                pos_x = (min(self.pos[0] + (np.random.randint(low = -1, high = 2) * speed), SIZE-1))
            else:
                pos_x = (max(self.pos[0] + (np.random.randint(low = -1, high = 2) * speed), -SIZE+1))
            if(self.pos[1] >= 0):
                pos_y = (min(self.pos[1] + (np.random.randint(low = -1, high = 2) * speed), SIZE-1))
            else:
                pos_y = (max(self.pos[1] + (np.random.randint(low = -1, high = 2) * speed), -SIZE+1))
            self.pos = (pos_x, pos_y)
            return
        
        speed_calcul = math.floor(min(speed, min_dist))
        if(min_pos[0] < 0):
            move_x = -speed_calcul
        elif(min_pos[0] > 0):
            move_x = speed_calcul
            
        if(min_pos[1] < 0):
            move_y = -speed_calcul
        elif(min_pos[1] > 0):
            move_y = speed_calcul
            
        self.pos = np.array((min(self.pos[0] + move_x, SIZE-1), min(self.pos[1] + move_y, SIZE-1)))
        
    
            
            