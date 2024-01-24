import random
from ruleta import Ruleta


class Jugador:
    nombre: str
    puntuacion: float
    ruleta: Ruleta

    def __init__(self, nombre: str, puntuacion: float):
        self.nombre = nombre
        self.puntuacion = puntuacion
        self.ruleta = Ruleta()

    def __str__(self):
        return f"Bienvenido {self.nombre}, empiezas con {self.puntuacion}"

    def tirar(self):
        nueva_tirada = random.choice(self.ruleta.gajos)
        return f"La ruleta ha parado en {nueva_tirada}"

    def comprar_vocal(self, vocal):
        precio_vocal = 50.0
        if self.puntuacion >= precio_vocal:
            if self.ruleta.letras[vocal] == False:
                self.ruleta.letras[vocal] = True
                return "Se compra"
        else:
            return "No se compra"
        pass

    def decir_letra(self):
        pass

    def resolver_panel(self):
        pass


# Crear la instancia de Jugador sin necesidad de pasar la lista de ruleta
j1 = Jugador("Jorge", 5.0)

print(j1.comprar_vocal("e"))
