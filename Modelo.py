# from vista import Vista
from jugador import Jugador
from ruleta import Ruleta

import random


class Modelo:
    # vista: Vista
    jugador: Jugador
    ruleta: Ruleta
    jugadores: list[Jugador]

    def __init__(self):
        # self.vista = Vista()
        self.ruleta = Ruleta()
        self.jugadores = []
        self.jugador = Jugador(
            "Juan",
        )

    def agregar_jugador(self, jugador: Jugador):
        if jugador not in self.jugadores:
            self.jugadores.append(jugador)
            return True
        else:
            return False

    def mostrar_jugadores(self):
        for jugador in self.jugadores:
            print(jugador)

    def tirar(self):
        valor = random.randint(0, 23)
        tirada = self.ruleta.gajos[valor]
        if valor == 0:
            self.jugador.puntuacion = 0
            return "0"  # QUIEBRA
        elif valor == 1:
            self.jugador.puntuacion = 0
            return "1"  # PIERDE TURNO

        elif valor == 2:
            self.jugador.comodines += 1
            return "2"  # COMODIN
        elif valor == 3:  # x2
            self.jugador.puntuacion *= 2
            return "3"
        elif valor == 4:  # /2
            self.jugador.puntuacion /= 2
            return "4"
        else:
            self.jugador.puntuacion += int(tirada)
            return tirada

    def comprar_vocal(self, vocal):
        if self.jugador.puntuacion >= 50:
            if self.ruleta.letras[vocal] == False:
                self.ruleta.letras[vocal] = True
                self.jugador.puntuacion -= 50
                return 1
            else:
                return 2
        else:
            return 0

    def decir_letra(self, letra):
        if self.ruleta.letras[letra] == False:
            self.ruleta.letras[letra] = True
            return True
        else:
            return False

    def resolver_panel(self, panel):
        if panel == self.ruleta.panel:
            return True
        else:
            return False


juego = Modelo()
