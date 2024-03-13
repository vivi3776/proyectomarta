

class Vista:
    def bienvenida(self):
        print("")
        print("--------------------------------------------------------")
        print("---                RULETA DE LA SUERTE               ---")
        print("--------------------------------------------------------")
        print("")

    def error_menu(self):
        print("-----------ERROR-----------")
        print("Escribe una opción correcta")

    def error_jugadores(self):
        print("-------------------------ERROR-----------------------")
        print("")
        print("Debes añadir al menos dos jugadores")
        print("")

    def error_vocal_consonante(self):
        print("Escribe un carácter correcto")

    def menu_inicio(self):
        print("1. Añadir jugador")
        print("2. Mostrar jugadores")
        print("3. Jugar")
        print("4. Salir")
        print("")
        try:
            opcion = int(input(""))
            return opcion
        except:
            return 6

    def menu_jugador(self, jugador, pista, panel):
        print("")
        print("---------------------------------------------------------------------")
        print("")
        print("")
        print(f"                        {pista.upper()}")
        print("")
        print("")
        print(f"           {panel}           ")
        print("")
        print("")
        print(f"Turno de: [{jugador}]")
        print("")
        print("")
        print("Qué quieres hacer?")
        print("1. Tirar")
        print("2. Comprar vocal")
        print("3. Resolver panel")
        print("4. Ver Comodines")
        print("5. Ver dinero actual")
        print("")
        print("---------------------------------------------------------------------")
        print("")

        try:
            opcion = int(input(""))
            return opcion
        except:
            return 6

    def mostrar_comodines(self, comodines):
        print(f"Tus comodines actuales son: {comodines}")

    def mostrar_dinero(self, dinero):
        print(f"Tu dinero acumulado es: {dinero}€")

    def siguiente_jugador(self, jugador):
        print("-------------------------------")
        print(f"Ahora es el turno de {jugador}")
        print("-------------------------------")

    def salir(self):
        print("-------------------------")
        print("--- Gracias por jugar ---")
        print("-------------------------")

    def quieres_usar_comodin(self):
        print("Tienes un comodín!")
        print("Quieres usarlo? s/n")
        opcion = input("")
        return opcion

    def usar_comodin(self):
        print("Has usado un comodín")
        print("Sigues jugando")

    def no_usar_comodin(self):
        print("No usas el comodin")
        print("Pierdes el turno")

    def crear_jugador(self):
        print("")
        print("Dime el nombre del nuevo jugador")
        print("")
        jugador = input("")
        return jugador

    def jugador_creado(self):
        print("")
        print("Has añadido al jugador con éxito")
        print("")

    def jugador_no_creado(self):
        print("")
        print("Ese jugador ya existe!")
        print("")

    def decir_letra(self):
        print("¡Dime una letra!")
        letra = input("")
        return letra.lower()

    def no_hay_dinero(self):
        print("No tienes suficiente dinero para comprar vocal!")

    def letra_ya_dicha(self):
        print("Lo sentimos, ya has dicho esa letra!")

    def vocal_comprada(self):
        print("Vocal comprada con éxito")

    def comprar_vocal(self):
        print("Qué vocal quieres comprar?")
        vocal = input("")
        return vocal.lower()

    def resolver_panel(self):
        print("Escribe el  panel correcto")
        panel = input("")
        return panel

    def letra_no_en_panel(self):
        print("La letra no estaba en el panel!")
        print("Pierdes el turno!")

    def letra_en_panel(self):
        print("La letra estaba en el panel!")

    def panel_correcto(self):
        print("Has acertado el panel! Felicidades")

    def panel_incorrecto(self):
        print("Has fallado! Prueba otra vez")

    def caer_quiebra(self):
        print("Mala suerte!")
        print("Has caido en quiebra!")
        print("Pierdes tu turno y tu dinero")

    def caer_pierde_turno(self):
        print("Mala suerte!")
        print("Has caido en Pierde Turno")
        print("Pierdes tu turno")

    def caer_comodin(self):
        print("Enhorabuena!")
        print("Has caido en Comodin")
        print("Recibes un comodin")

    def caer_x2(self):
        print("Enhorabuena!")
        print("Has caido en X2")
        print("Duplicas tu dinero")

    def caer_e2(self):
        print("Mala suerte!")
        print("Has caido en 1/2")
        print("Pierdes la mitad del dinero")

    def caer(self, gajo):
        print(f"Has caido en: {gajo}")

    def panel(self, panel):
        print("")
        print(f"El panel es \n{panel}")
        print("")
    
    def no_hay_jugadores(self):
        print("")
        print("No hay jugadores actualmente")
        print("")
    
    def mostrar_jugadores(self, jugadores):
        print("")
        #Muestra los jugadores
        if len(jugadores) == 0:
            print("No hay jugadores actualmente")
        else:
            print("Los jugadores son:")
            for jugador in jugadores:
                print(f"- {jugador.nombre} -")
        print("")