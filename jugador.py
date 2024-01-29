import random
from ruleta import Ruleta


class Jugador:
    nombre: str
    puntuacion: float
    comodines: int

    def __init__(self, nombre: str, puntuacion: float = 100, comodines: int = 0):
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.comodines = comodines

    def __str__(self):
        return f"Bienvenido {self.nombre}, empiezas con {self.puntuacion}"

    def mostrar_puntuacion(self):
        return self.puntuacion


# Crear la instancia de Jugador
j1 = Jugador("Jorge", 5.0)
