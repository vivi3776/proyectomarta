from Controlador import Controlador
from Modelo import Modelo
from vista import Vista

if __name__ == "__main__":
    juego = Controlador(modelo=Modelo(), vista=Vista())
    juego.inicio()

#TODO mostrar las letras que ya estaban dichas
#TODO hacer una tirada menos aleatoria
#TODO multiplicar el dinero x las letras q han aparecido
#TODO poner bien la clase ruleta