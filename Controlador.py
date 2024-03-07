from Modelo import Modelo
from vista import Vista
from os import system
import time


class Controlador:
    modelo: Modelo
    vista: Vista
    orden_jugador: int  # Se trata del jugador que empezará

    #Constructor
    def __init__(self, modelo, vista, orden_jugador=0):
        self.modelo = modelo
        self.vista = vista
        self.orden_jugador = orden_jugador

    def bienvenida(self):#Funcion que da la bienvenida
        self.vista.bienvenida()

    #Funcion que cierra el juego
    def salir(self):
        self.vista.salir()

    #Creacion del menú de inicio del juego
    def menu_inicio(self):
        b_menu = True
        while b_menu:
            self.bienvenida()
            menu = self.vista.menu_inicio()
            if menu == 1:  # Añadir jugador
                b_menu = False
                self.crear_jugador()
                
            elif menu == 2:  # Mostrar jugador
                self.modelo.mostrar_jugadores()
                time.sleep(2)
                system("cls")
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

    #Creacion del menu del jugador una vez que se inicia el juego
    def menu_jugador(self, pista, panel):
        jugador = self.modelo.jugadores[self.orden_jugador]
        b_menu = True

        while b_menu:
            menu = self.vista.menu_jugador(jugador.nombre,pista, panel)

            if menu > 5:
                self.vista.error_menu()
                time.sleep(2)
                system("cls")

            else:
                b_menu = False

        return menu

    #Funcion para usar un comodin
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

    #Funcion para crear un jugador
    def crear_jugador(self):
        jugador = self.vista.crear_jugador()
        if self.modelo.agregar_jugador(jugador):
            self.vista.jugador_creado()
        else:
            self.vista.jugador_no_creado()
            
        time.sleep(2)
        system("cls")
        self.menu_inicio()

    #Funcion que muestra la lista de todos los jugadores creados
    def mostrar_jugadores(self):
        # TODO MOSTRAR JUGADORES
        pass
    
    #Funcion para decir y comprobar una letra 
    def decir_letra(self):
        letra = self.vista.decir_letra()
        if self.modelo.decir_letra(letra) == 1:
            return letra
        elif self.modelo.decir_letra(letra) == 0:
            self.vista.letra_ya_dicha()
            return ""
        else:
            self.vista.error_vocal_consonante()
            return ""

    #Funcion para comprar una vocal
    def comprar_vocal(self):
        vocal = self.vista.comprar_vocal()
        return_vocal = self.modelo.comprar_vocal(vocal)
        if return_vocal == 0:  # No se compro vocal x dinero
            self.vista.no_hay_dinero()

        elif return_vocal == 1:  # Se ha comprado la vocal
            self.vista.vocal_comprada()
            return vocal

        elif return_vocal == 2:  # No se compra vocal ya dicha
            self.vista.letra_ya_dicha()
        else:
            self.vista.error_vocal_consonante()

        return ""

    #Funcion para resolver un panel
    def resolver_panel(self, panel):
        panel_jugador = self.vista.resolver_panel()

        if self.modelo.resolver_panel(panel_jugador, panel):
            self.vista.panel_correcto()
            return True
        else:
            self.vista.panel_incorrecto()
            return False

    #Funcion para que el jugador tire a la ruleta y caiga en un gajo
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

            else:
                self.siguiente_jugador()

        elif tirada == "2":  # Comodin
            self.vista.caer_comodin()

        elif tirada == "3":  # x2
            self.vista.caer_x2()
            time.sleep(1)

        elif tirada == "4":  # /2
            self.vista.caer_e2()
            time.sleep(1)

        else:  # Gajo normal
            self.vista.caer(tirada)
            time.sleep(1)
        return tirada

    #Funcion que combina la bienvenida con el menu de inicio
    def inicio(self):
        self.bienvenida()
        time.sleep(1)
        system("cls")
        self.menu_inicio()
    
    #Funcion que hace funcionar el paso de jugadores
    def siguiente_jugador(self):
        self.orden_jugador = (self.orden_jugador + 1) % len(self.modelo.jugadores)
        jugador = self.modelo.jugadores[self.orden_jugador]
        self.vista.siguiente_jugador(jugador.nombre)

    #Funcion que hace que un el juego funcione
    def jugar(self):
        jugar = True
        if len(self.modelo.jugadores) >= 2:
            time.sleep(0.5)
            system("cls")
            self.modelo.leer_paneles_del_txt()
            panel_oculto, panel, pista = self.modelo.generar_panel()    #Caracteristicas del panel generado
            while jugar:
                time.sleep(1)
                system("cls")
                jugador = self.modelo.jugadores[self.orden_jugador]
                menu = self.menu_jugador(pista, panel_oculto)
                if menu == 1:  # TIrar
                    tirar = self.tirar()
                    letra = self.decir_letra()
                    if letra != "":
                        panel_oculto_2 = str(
                            self.modelo.descubrir_panel(panel, panel_oculto, letra)
                        )
                        if (
                            panel_oculto == panel_oculto_2
                        ):  # La letra no estaba en el panel
                            self.vista.letra_no_en_panel()
                            time.sleep(1)
                            self.siguiente_jugador()
                        else:  # La letra estaba en el panel y sigues jugando
                            self.modelo.actualizar_info(jugador, tirar)

                            panel_oculto = panel_oculto_2
                            self.vista.letra_en_panel()
                            time.sleep(1)
                            self.vista.panel(panel_oculto)  # TODO pedir por comodin

                    else:  # Letra ya dichaa
                        self.siguiente_jugador()
                elif menu == 2:  # Comprar voccal
                    vocal = self.comprar_vocal()

                    if vocal != "":
                        panel_oculto = str(
                            self.modelo.descubrir_panel(panel, panel_oculto, vocal)
                        )
                elif menu == 3:  # Resolver
                    if self.resolver_panel(panel):
                        time.sleep(3)
                        jugar = False
                    else:
                        self.siguiente_jugador()
                elif menu == 4:  # Ver comodines
                    self.vista.mostrar_comodines(jugador.comodines)
                elif menu == 5:  # Dinero
                    self.vista.mostrar_dinero(jugador.puntuacion)

        else:
            self.vista.error_jugadores()
            time.sleep(2)
            system("cls")
            self.menu_inicio()

        self.vista.salir()


