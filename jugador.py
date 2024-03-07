import random
from ruleta import Ruleta


class Jugador:
    __nombre: str
    __puntuacion: float
    __comodines: int

    def __init__(self, nombre: str, puntuacion: float = 100.00, comodines: int = 0):
        self.__nombre = nombre
        self.__puntuacion = puntuacion
        self.__comodines = comodines

    def __str__(self):
        return f"Bienvenido {self.nombre}, empiezas con {self.puntuacion}"

    def mostrar_puntuacion(self):
        return self.puntuacion
    
    #Getters y setters de nombre
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    
    @staticmethod
    def nombre_correcto(nombre: str) ->bool:
        if nombre.isalpha():
            return True
        else:
            return False
        

    #Getters y setters de puntuacion
    @property
    def puntuacion(self):
        return self.__puntuacion

    @puntuacion.setter
    def puntuacion(self, puntuacion):
        self.__puntuacion = puntuacion

    #Getters y setters de comodines
    @property
    def comodines(self):
        return self.__comodines

    @comodines.setter
    def comodines(self, comodines):
        self.__comodines = comodines

    

# Crear la instancia de Jugador
# j1 = Jugador("Jorge", 5.0)
