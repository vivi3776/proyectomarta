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

    def __init__(self):
        # self.vista = Vista()
        self.ruleta = Ruleta()
        self.jugadores = []
        self.jugador = Jugador(
            "Juan",
        )

    def descubrir_panel(
        self, panel: str, panel_oculto: str, letra: str
    ):  
        #Compara la letra dicha con el panel y si la tiene lo coloca en la poscion del panel oculto
        lista2 = list(panel_oculto)
        for posicion in range(len(panel)):
            if panel[posicion].lower() == letra.lower():
                lista2[posicion] = letra
        e = ""
        for i in range(len(lista2)):
            e = e + lista2[i]
        return str(e)

    def generar_panel(self):
        #Genera un panel aleatorio de los disponibles
        numero = random.randint(1, len(self.ruleta.panel))
        pista = self.ruleta.pista[numero]
        panel = self.ruleta.panel[numero]

        panel_oculto = ""
        for letra in panel:
            if letra != " ":
                panel_oculto = panel_oculto + "_"
            else:
                panel_oculto = panel_oculto + " "

        return panel_oculto, panel, pista

    def agregar_jugador(self, nombre_jugador: str):
        jugador = Jugador(nombre_jugador)
        #Comprueba si hay un jugador con ese nombre si no lo hay lo añade
        if jugador not in self.jugadores:
            self.jugadores.append(jugador)
            return True
        else:
            return False

    def mostrar_jugadores(self):
        print("")
        #Muestra los jugadores
        if len(self.jugadores) == 0:
            print("No hay jugadores actualmente")
        else:
            print("Los jugadores son:")
            for jugador in self.jugadores:
                print(f"- {jugador.nombre} -")
        print("")

    def comprobar_comodin(self, jugador: Jugador):
        if jugador.comodines == 0:
            return False
        else:
            return True

    def usar_comodin(self, jugador: Jugador):
        jugador.comodines -= 1

    def actualizar_info(self, jugador: Jugador, valor):
        if int(valor) == 0:
            self.jugador.puntuacion = 0
            # QUIEBRA
        elif int(valor) == 1:
            self.jugador.puntuacion = 0
            # PIERDE TURNO

        elif int(valor) == 2:
            jugador.comodines += 1
            # COMODIN
        elif int(valor) == 3:  # x2
            jugador.puntuacion = jugador.puntuacion * 2

        elif int(valor) == 4:  # /2
            jugador.puntuacion = jugador.puntuacion / 2

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

    def leer_paneles_del_txt(self):
        with open('paneles.txt', 'r') as archivo:

            todas_lineas = archivo.readlines()[4:]

            for i, linea in enumerate(todas_lineas):
                if i % 2 == 0: #Si son paneles
                    self.ruleta.pista.append(linea.strip())  
                else:
                    self.ruleta.panel.append(linea.strip())  # Si son pistas

