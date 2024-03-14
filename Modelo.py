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



    #Funcion que comprueba si tienes o no comodines
    def comprobar_comodin(self, jugador: Jugador):
        if jugador.comodines == 0:
            return False
        else:
            return True
    #Usar comodin
    def usar_comodin(self, jugador: Jugador):
        jugador.comodines -= 1

    #Acctualizar el dinero segun la tirada
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

    #Funcion que realiza una tirada aleatoria
    def tirar(self, jugador: Jugador):
        valor = random.randint(0, 23)
        tirada = self.ruleta.GAJOS[valor]
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

    #Funcion para comprar vocal si hay o no dinero
    def comprar_vocal(self, vocal):
        if self.jugador.puntuacion >= 50:  #Precio de la vocal
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

    #Funcion que devuelve un valor dependiendo si la letra esta en el panel o no, o no es una letra
    def decir_letra(self, letra):
        try:
            if self.ruleta.consonantes[letra] == False:
                self.ruleta.consonantes[letra] = True
                return 1
            else:
                return 0
        except:
            return -1
    #Funcion que devuelve true o false si el jugador acierta o no el panel
    def resolver_panel(self, panel_jugador, panel):
        if panel_jugador.lower() == panel.lower():
            return True
        else:
            return False

    #Se leen los paneles del txt y se guardan en dos listas. una de pistas otra de paneles
    def leer_paneles_del_txt(self):
        stock_lines = [
        "CANCION POPULAR\n",
        "Melodia conocida y apreciada por un amplio público\n",
        "REVOLUCIÓN INDUSTRIAL\n",
        "Paso de la producción manual a la industrial\n",
        "SMARTPHONE\n",
        "Dispositivo móvil con funciones avanzadas\n"
        ]   

        with open('paneles.txt', 'r+') as archivo:
            try:
                todas_lineas = archivo.readlines()[5:]
                print(len(todas_lineas))
                if len(todas_lineas) < 4:
                    # Agregar líneas de stock al archivo
                    archivo.writelines(stock_lines)
                    todas_lineas.extend(stock_lines)

                for i, linea in enumerate(todas_lineas):
                    if i % 2 == 0: #Si son pistas
                        self.ruleta.pista.append(linea.strip())  
                    else:   #Si son paneles
                        self.ruleta.panel.append(linea.strip())  # Si son pistas

            except (IOError, FileNotFoundError):
                # En caso de error, agregar líneas de stock al archivo
                archivo.writelines(stock_lines)
                todas_lineas = stock_lines
                                  

            
    def lista_letras_dichas(self):
        consonantes = []
        vocales = []
        
        for letra in self.ruleta.consonantes:
            if self.ruleta.consonantes[letra]:  # Verifica si el valor es True
                consonantes.append(letra)
        for letra in self.ruleta.vocales:
            if self.ruleta.vocales[letra]:  # Verifica si el valor es True
                vocales.append(letra)
        letras = consonantes + vocales
        return consonantes.sort()