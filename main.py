from Controlador import Controlador
from Modelo import Modelo
from vista import Vista

if __name__ == "__main__":
    juego = Controlador(modelo=Modelo(), vista=Vista())
    juego.inicio()

#TODO mostrar las letras que ya estaban dichas
#TODO hacer una tirada menos aleatoria
    #TODO cambiar el txt para que si esta vacio 1 no pete y 2 añadir paneles de ejemplo