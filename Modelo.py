# from vista import Vista
from jugador import Jugador
from ruleta import Ruleta

import random

random.seed(1)


class Modelo:
    # vista: Vista
    jugador: Jugador
    ruleta: Ruleta
    jugadores: list[Jugador]

    def descubrir_panel(
        self, panel: str, panel_oculto: str, letra: str
    ):  # TODO NO FUNCIONA
        lista2 = list(panel_oculto)
        for posicion in range(len(panel)):
            if panel[posicion].lower() == letra.lower():
                lista2[posicion] = letra
        return lista2

    def generar_panel(self):
        numero = random.randint(1, len(self.ruleta.panel))
        pista = self.ruleta.pista[numero]
        panel = self.ruleta.panel[pista]

        panel_oculto = ""
        for letra in panel:
            if letra != " ":
                panel_oculto = panel_oculto + "_"
            else:
                panel_oculto = panel_oculto + " "

        return panel_oculto, panel

    def __init__(self):
        # self.vista = Vista()
        self.ruleta = Ruleta()
        self.jugadores = []
        self.jugador = Jugador(
            "Juan",
        )

    def agregar_jugador(self, nombre_jugador: str):
        jugador = Jugador(nombre_jugador)
        if jugador not in self.jugadores:
            self.jugadores.append(jugador)
            return True
        else:
            return False

    def mostrar_jugadores(self):
        for jugador in self.jugadores:
            print(jugador)

    def comprobar_comodin(self, jugador: Jugador):
        if jugador.comodines == 0:
            return False
        else:
            return True

    def usar_comodin(self, jugador: Jugador):
        jugador.comodines -= 1

    def actualizar_info(self, jugador: Jugador, valor):
        if valor == 0:
            self.jugador.puntuacion = 0
            # QUIEBRA
        elif valor == 1:
            self.jugador.puntuacion = 0
            # PIERDE TURNO

        elif valor == 2:
            jugador.comodines += 1
            # COMODIN
        elif valor == 3:  # x2
            jugador.puntuacion *= 2

        elif valor == 4:  # /2
            jugador.puntuacion /= 2

        else:
            jugador.puntuacion += int(valor)

    def tirar(self, jugador: Jugador):
        valor = random.randint(0, 23)
        tirada = self.ruleta.gajos[valor]
        if valor == 0:
            # self.jugador.puntuacion = 0
            return "0"  # QUIEBRA
        elif valor == 1:
            # self.jugador.puntuacion = 0
            return "1"  # PIERDE TURNO

        elif valor == 2:
            # jugador.comodines += 1
            return "2"  # COMODIN
        elif valor == 3:  # x2
            # jugador.puntuacion *= 2
            return "3"
        elif valor == 4:  # /2
            # jugador.puntuacion /= 2
            return "4"
        else:
            # jugador.puntuacion += int(tirada)
            return tirada

    def comprar_vocal(self, vocal):
        if self.jugador.puntuacion >= 50:
            try:
                if self.ruleta.vocales[vocal] == False:
                    self.ruleta.vocales[vocal] = True
                    self.jugador.puntuacion -= 50
                    return 1
                else:
                    return 2
            except:
                return -1
        else:
            return 0

    def decir_letra(self, letra):
        try:
            if self.ruleta.consonantes[letra] == False:
                self.ruleta.consonantes[letra] = True
                return 1
            else:
                return 0
        except:
            return -1

    def resolver_panel(self, panel_jugador, panel):
        if panel_jugador == panel:
            return True
        else:
            return False


# juego = Modelo()
