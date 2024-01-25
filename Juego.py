from vista import Vista
from jugador import Jugador
from ruleta import Ruleta

import random


class Juego:
    vista: Vista
    jugador: Jugador
    ruleta: Ruleta

    def __init__(self):
        self.vista = Vista()
        self.ruleta = Ruleta()

    def tirar(self):
        valor = random.randint(0, 23)
        tirada = self.ruleta.gajos[random.randint(0, 23)]
        if valor <= 3:  # Es un gajo especial
            return f"Has caido en {tirada}"
        else:  # Es un gajo de dinero
            return f"Has caido en {tirada}"


juego = Juego()
print(juego.tirar())
