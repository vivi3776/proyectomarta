from Modelo import Modelo
from vista import Vista


class Controlador:
    modelo: Modelo
    vista: Vista

    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    def menu(self):
        menu = self.vista.menu()

        if menu == 1:
            self.crear_jugador()
        elif menu == 2:
            pass
        elif menu == 3:
            pass
        elif menu == 4:
            self.vista.salir()

    def crear_jugador(self):
        jugador = self.vista.crear_jugador()
        if self.modelo.agregar_jugador(jugador):
            self.vista.jugador_creado()
        else:
            self.vista.jugador_no_creado()

        self.menu()

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

        elif return_vocal == 2:  # No se compro vocal ya dicha
            self.vista.letra_ya_dicha()

    def resolver_panel(self):
        panel = self.vista.resolver_panel()

        if self.modelo.resolver_panel(panel):
            self.vista.panel_correcto()
        else:
            self.vista.panel_incorrecto()


controlador = Controlador(modelo=Modelo(), vista=Vista())
controlador.menu()
