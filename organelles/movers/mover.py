from organelles.organelle import Organelle
from config.organelles_type import OrganellesTypes

class Mover(Organelle):
    
    def __init__(self, name, speed, consumption_rate):
        super().__init__(
            name = name,
            category = OrganellesTypes.MOVER,
            consumption_rate = consumption_rate
        )
        self._speed = speed
    
    @property
    def speed(self):
        return self._speed