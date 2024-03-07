from Controlador import Controlador
from Modelo import Modelo
from vista import Vista

if __name__ == "__main__":
    juego = Controlador(modelo=Modelo(), vista=Vista())
    juego.inicio()

#TODO cambir el modelo.mostrar_jugadores y ponerlo en vista
#TODO mostrar las letras que ya estaban dichas