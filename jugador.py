from ruleta import ruleta

class Jugador:
    nombre: str
    puntuacion: float

    def __init__(self, nombre: str, puntuacion: float):
        self.nombre = nombre
        self.puntuacion = puntuacion

    def __str__(self):
        return f"Bievenido {self.nombre} empiezas con {self.puntuacion}"
    
    def tirar():
    pass
    
    def comprar_vocal():
    pass

    def decir_letra():

    def resolver_panel():
    pass



j1 = Jugador("Jorge", 5.0)
print(j1)
