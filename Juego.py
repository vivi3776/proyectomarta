# from vista import Vista
from jugador import Jugador
from ruleta import Ruleta

import random


class Juego:
    # vista: Vista
    jugador: Jugador
    ruleta: Ruleta
    jugadores: list[Jugador]

    def __init__(self):
        # self.vista = Vista()
        self.ruleta = Ruleta()
        self.jugadores = []
        self.jugador = Jugador("Juan", 50)

    def agregar_jugador(self, jugador: Jugador):
        if jugador not in self.jugadores:
            self.jugadores.append(jugador)
        else:
            raise Exception("Este jugador ya existe")

    def mostrar_jugadores(self):
        for jugador in self.jugadores:
            print(jugador)

    def tirar(self):
        valor = random.randint(0, 23)
        tirada = self.ruleta.gajos[valor]
        if valor == 0:
            return f"Has caido en QUIEBRA"  # QUIEBRA
        elif valor == 1:
            return f"Has caido en PIERDE TURNO"  # PIERDE TURNO
        elif valor == 2:
            return f"Has caido en COMODIN"  # COMODIN
        elif valor == 3:
            return f"Has caido en x2"
        elif valor == 4:
            return f"Has caido en /2"
        else:
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

    def resolver_panel(self, panel):
        if panel == self.ruleta.panel:
            return f"Has acertado"
        else:
            return f"Has fallado"


juego = Juego()
