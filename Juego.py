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
        self.jugador = Jugador("Juan", 50)

    def tirar(self):
        valor = random.randint(0, 23)
        tirada = self.ruleta.gajos[random.randint(0, 23)]
        if valor <= 3:  # Es un gajo especial
            return f"Has caido en {tirada}"
        else:  # Es un gajo de dinero
            self.jugador.puntuacion += int(tirada)
            return f"Has caido en {tirada},  ahora tienes {self.jugador.puntuacion}"

    def comprar_vocal(self, vocal):
        if self.jugador.puntuacion >= 50:
            if self.ruleta.letras[vocal] == False:
                self.ruleta.letras[vocal] = True
                self.jugador.puntuacion -= 50
                return f"Has comprado la letra {vocal} ahora tienes {self.jugador.puntuacion}"
            else:
                return f"No has comprado"
        else:
            return f"No tienes suficiente dinero"

    def decir_letra(self, letra):
        if self.ruleta.letras[letra] == False:
            self.ruleta.letras[letra] = True
            return f"Has dicho la letra {letra}"
        else:
            return f"Esa letra ya esta dicha"


juego = Juego()
print(juego.decir_letra("b"))
print(juego.decir_letra("c"))
