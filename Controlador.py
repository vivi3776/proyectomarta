from Modelo import Modelo
from vista import Vista
from os import system
import time


class Controlador:
    modelo: Modelo
    vista: Vista
    orden_jugador: int  # Se trata del jugador q empezará

    def __init__(self, modelo, vista, orden_jugador=0):
        self.modelo = modelo
        self.vista = vista
        self.orden_jugador = orden_jugador

    def bienvenida(self):
        self.vista.bienvenida()

    def salir(self):
        self.vista.salir()

    def menu_inicio(self):
        b_menu = True
        while b_menu:
            menu = self.vista.menu_inicio()
            if menu == 1:  # Añadir jugador
                b_menu = False
                self.crear_jugador()
            elif menu == 2:  # Mostrar jugador
                b_menu = False
                self.modelo.mostrar_jugadores()
            elif menu == 3:  # Jugar
                self.jugar()
                b_menu = False
            elif menu == 4:  # Salir
                b_menu = False
                self.vista.salir()
            else:
                self.vista.error_menu()
                time.sleep(2)
                system("cls")

    def menu_jugador(self):
        b_menu = True

        while b_menu:
            menu = self.vista.menu_jugador()

            if menu != 5:  # Tirar
                b_menu = False

            else:
                self.vista.error_menu()
                time.sleep(2)
                system("cls")

        return menu

    def usar_comodin(self, jugador):
        comprobar_comodin = self.modelo.comprobar_comodin(jugador)
        if comprobar_comodin:
            b_comodin = True
            while b_comodin:
                opcion = self.vista.quieres_usar_comodin()
                if opcion == "s":
                    b_comodin = False
                    self.vista.usar_comodin()
                    return True

                elif opcion == "n":
                    b_comodin = False
                    self.vista.no_usar_comodin()
                    return False

    def crear_jugador(self):
        jugador = self.vista.crear_jugador()
        if self.modelo.agregar_jugador(jugador):
            self.vista.jugador_creado()
        else:
            self.vista.jugador_no_creado()

        self.menu_inicio()

    def mostrar_jugadores(self):
        # TODO MOSTRAR JUGADORES
        pass

    def decir_letra(self):
        letra = self.vista.decir_letra()
        if self.modelo.decir_letra(letra):
            return letra
        else:
            self.vista.letra_ya_dicha()
            return ""

    def comprar_vocal(self):
        vocal = self.vista.comprar_vocal()
        return_vocal = self.modelo.comprar_vocal(vocal)
        if return_vocal == 0:  # No se compro vocal x dinero
            self.vista.no_hay_dinero()

        elif return_vocal == 1:  # Se ha comprado la vocal
            self.vista.vocal_comprada()

        elif return_vocal == 2:  # No se compra vocal ya dicha
            self.vista.letra_ya_dicha()

    def resolver_panel(self, panel):
        panel_jugador = self.vista.resolver_panel()

        if self.modelo.resolver_panel(panel_jugador, panel):
            self.vista.panel_correcto()
            return True
        else:
            self.vista.panel_incorrecto()
            return False

    def tirar(self):
        jugador = self.modelo.jugadores[self.orden_jugador]
        tirada = self.modelo.tirar(jugador)
        if tirada == "0":  # Quiebra
            self.vista.caer_quiebra()
            if self.usar_comodin(jugador):
                self.vista.usar_comodin()
                self.modelo.usar_comodin(jugador)
            else:
                jugador.puntuacion == 0  # TODO usar otra forma de reiniciar stats
                self.siguiente_jugador()

        elif tirada == "1":  # Pierde turno
            self.vista.caer_pierde_turno
            if self.usar_comodin(jugador):
                self.vista.usar_comodin
                self.modelo.usar_comodin(jugador)
                return False
            else:
                self.siguiente_jugador()
                return False

        elif tirada == "2":  # Comodin
            self.vista.caer_comodin()
            return True

        elif tirada == "3":  # x2
            self.vista.caer_x2()
            time.sleep(1)
            return True

        elif tirada == "4":  # /2
            self.vista.caer_e2()
            time.sleep(1)
            return True

        else:  # Gajo normal
            self.vista.caer(tirada)
            time.sleep(1)
            return True

    def inicio(self):
        self.bienvenida()
        time.sleep(1)
        self.menu_inicio()

    def jugar(self):
        jugar = True
        if len(self.modelo.jugadores) >= 2:
            panel_oculto, panel = self.modelo.generar_panel()
            self.vista.panel(panel_oculto)
            while jugar:
                jugador = self.modelo.jugadores[self.orden_jugador]
                menu = self.menu_jugador()
                if menu == 1:  # TIrar
                    if self.tirar():
                        letra = self.decir_letra()
                        if letra != "":
                            panel_oculto_2 = self.modelo.descubrir_panel(
                                panel, panel_oculto, letra
                            )
                            if (
                                panel_oculto == panel_oculto_2
                            ):  # La letra no estaba en el panel
                                self.vista.letra_no_en_panel()
                                time.sleep(1)
                                self.siguiente_jugador()
                            else:  # La letra estaba en el panel y sigues jugando
                                panel_oculto = panel_oculto_2
                                self.vista.letra_en_panel()
                                time.sleep(1)
                                self.vista.panel(panel_oculto)  # TODO pedir por comodin

                        else:  # Letra ya dichaa
                            self.siguiente_jugador()

                elif menu == 2:  # Resolver
                    if self.resolver_panel(panel):
                        time.sleep(3)
                        jugar = False
                    else:
                        self.siguiente_jugador()
                elif menu == 3:  # Ver comodines
                    self.vista.mostrar_comodines(jugador.comodines)
                elif menu == 4:  # Dinero
                    self.vista.mostrar_dinero(jugador.puntuacion)

        else:
            self.vista.error_jugadores
            time.sleep(2)
            system("cls")
            self.menu_inicio()

        self.vista.salir()

    def siguiente_jugador(self):
        self.orden_jugador = (self.orden_jugador + 1) % len(self.modelo.jugadores)
        jugador = self.modelo.jugadores[self.orden_jugador]
        self.vista.siguiente_jugador(jugador.nombre)


controlador = Controlador(modelo=Modelo(), vista=Vista())
controlador.inicio()
