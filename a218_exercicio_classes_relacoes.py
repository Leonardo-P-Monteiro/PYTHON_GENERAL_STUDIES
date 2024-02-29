class Car:
    def __init__(self, model):
        self._model = model
        self._engine = None
        self._manufacturer = None

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def engine(self):
        return self._engine
    
    @engine.setter
    def engine(self, engine):
        self._engine = engine
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self, manufacturer):
        self._manufacturer = manufacturer

class Engine:
    def __init__(self, model):
        self._model = model
    
    @property
    def engine (self):
        return self._model

class Manufacturer:
    def __init__(self, brand):
        self._brand = brand
    
    @property
    def brand (self):
        return self._brand
    
label_1 = Manufacturer('Fiat')
label_2 = Manufacturer('Gurgel')
engine_1 = Engine('AP')
engine_2 = Engine('VHT')
car_1 = Car('Uno')
car_1.manufacturer = label_1
car_1.engine = engine_1

###########
#print(car_1.model)
print(car_1.model)
print(car_1.manufacturer.brand)
print(car_1.engine.engine)
