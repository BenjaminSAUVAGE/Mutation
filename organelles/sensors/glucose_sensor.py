from config.foods_name import FoodsName
from organelles.sensors.sensor import Sensor


class GlucoseSensor(Sensor):
    
    def __init__(self):
        super().__init__(
         name = "glucose_sensor",
         range = 5,
         consumption_rate = 5,
         what_can_be_sense = FoodsName.GLUCOSE
        )
        
