from organelles.movers.mover import Mover


class Flagelle(Mover):
    
    
    def __init__(self, quantity):
        self._quantity = quantity
        super().__init__(
            name = f"{quantity}_flagelle{'s' if quantity > 1 else ''}",
            consumption_rate = 5,
            speed = 2 * self._quantity
        )
        
    @property
    def consumption(self):
        return self._quantity * self._consumption_rate
    
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, new_quantity):
        self._quantity = new_quantity