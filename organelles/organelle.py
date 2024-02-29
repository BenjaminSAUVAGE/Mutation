class Organelle():
    
    def __init__(self, name, category, consumption_rate):
        self._name = name
        self._category = category
        self._consumption_rate = consumption_rate
        
    @property
    def category(self):
        return self._category
    
    @property
    def name(self):
        return self._name
