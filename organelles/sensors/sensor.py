from config.organelles_type import OrganellesTypes
from organelles.organelle import Organelle


class Sensor(Organelle):
    
    def __init__(self, name, range, consumption_rate, what_can_be_sense):
        super().__init__(
         name = name,
         category = OrganellesTypes.SENSOR,
         consumption_rate = consumption_rate
        )
        self._range = range
        self._what_can_be_sense = what_can_be_sense

        
    @property
    def range(self):
        return self._range

    @range.setter
    def range(self, new_range):
        self._range = new_range

    @property
    def what_can_be_sense(self):
        return self._what_can_be_sense
    
    @property
    def consumption(self):
        return self._range * self._consumption_rate