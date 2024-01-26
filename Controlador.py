from Modelo import Modelo
from vista import Vista
import time


class Controlador:
    modelo: Modelo
    vista: Vista

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def bienvenida(self):
        self.vista.bienvenida()

    def salir(self):
        self.vista.salir()

    def menu(self):
        menu = self.vista.menu()

        if menu == 1:  # Añadir jugador
            self.crear_jugador()
        elif menu == 2:  # Mostrar jugador
            pass
        elif menu == 3:  # Jugar
            pass
        elif menu == 4:  # Salir
            self.vista.salir()

    def crear_jugador(self):
        jugador = self.vista.crear_jugador()
        if self.modelo.agregar_jugador(jugador):
            self.vista.jugador_creado()
        else:
            self.vista.jugador_no_creado()

        self.menu()

    def mostrar_jugadores(self):
        pass

    def decir_letra(self):
        letra = self.vista.decir_letra()
        if self.modelo.decir_letra(letra):
            pass
        else:
            self.vista.letra_ya_dicha()

    def comprar_vocal(self):
        vocal = self.vista.comprar_vocal()
        return_vocal = self.modelo.comprar_vocal(vocal)
        if return_vocal == 0:  # No se compro vocal x dinero
            self.vista.no_hay_dinero()

        elif return_vocal == 1:  # Se ha comprado la vocal
            self.vista.vocal_comprada()

        elif return_vocal == 2:  # No se compra vocal ya dicha
            self.vista.letra_ya_dicha()

    def resolver_panel(self):
        panel = self.vista.resolver_panel()

        if self.modelo.resolver_panel(panel):
            self.vista.panel_correcto()
        else:
            self.vista.panel_incorrecto()

    def tirar(self):
        tirada = self.modelo.tirar()
        if tirada == "0":  # Quiebra
            self.vista.caer_quiebra()
        elif tirada == "1":  # Pierde turno
            self.vista.caer_pierde_turno

        elif tirada == "2":  # Comodin
            self.vista.caer_comodin

        elif tirada == "3":  # x2
            self.vista.caer_x2

        elif tirada == "4":  # /2
            self.vista.caer_e2

        else:  # Gajo normal
            self.vista.caer(tirada)

    def inicio(self):
        self.bienvenida()
        time.sleep(1)
        self.menu()


controlador = Controlador(modelo=Modelo(), vista=Vista())

controlador.tirar()
controlador.tirar()
