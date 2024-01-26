class Vista:
    def bienvenida(self):
        print("----------------------------")
        print("--- RULETA DE LA SUERTE ---")
        print("----------------------------")

    def menu(self):
        print("1. Añadir jugador")
        print("2. Mostrar jugadores")
        print("3. Jugar")
        print("4. Salir")
        opcion = int(input(""))
        return opcion

    def salir(self):
        print("-------------------------")
        print("--- Gracias por jugar ---")
        print("-------------------------")

    def crear_jugador(self):
        print("Dime el nombre del nuevo jugador")
        jugador = input("")
        return jugador

    def jugador_creado(self):
        print("Has añadido al jugador con éxito")

    def jugador_no_creado(self):
        print("Ese jugador ya existe!")

    def decir_letra(self):
        print("¡Dime una letra!")
        letra = input("")
        return letra

    def no_hay_dinero(self):
        print("No tienes suficiente dinero para comprar vocal!")

    def letra_ya_dicha(self):
        print("Lo sentimos, ya has dicho esa letra!")

    def vocal_comprada(self):
        print("Vocal comprada con éxito")

    def comprar_vocal(self):
        print("Qué vocal quieres comprar?")
        vocal = input("")
        return vocal

    def resolver_panel(self):
        print("Escribe el  panel correcto")
        panel = input("")
        return panel

    def panel_correcto(self):
        print("Has acertado el panel! Felicidades")

    def panel_incorrecto(self):
        print("Has fallado! Prueba otra vez")
