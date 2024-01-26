class Vista:
    def bienvenida():
        print("----------------------------")
        print("--- RULETA DE LA SUERTE ---")
        print("----------------------------")

    def menu():
        print("1. Añadir jugador")
        print("2. Mostrar jugadores")
        print("3. Jugar")
        print("4. Salir")
        opcion = int(input(""))
        return opcion

    def crear_jugador():
        print("Dime el nombre del nuevo jugador")
        jugador = input("")
        return jugador

    def decir_letra():
        print("Di una letra! ")
        letra = input("")
        return letra

    def comprar_vocal():
        print("Qué vocal quieres comprar?")
        vocal = input("")
        return vocal

    def resolver_panel():
        print("Escribe el  panel correcto")
        panel = input("")
        return panel


vista = Vista
vista.bienvenida()
