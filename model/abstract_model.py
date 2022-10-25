from abc import ABCMeta #
class AbstractModel(metaclass=ABCMeta): #Se define una clase abstracta llamada abstract Modelo
    def __init__(self,data):
        for key, value in data.items():
            setattr(self, key, value)