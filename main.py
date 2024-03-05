from Controlador import Controlador
from Modelo import Modelo
from vista import Vista


juego = Controlador(modelo=Modelo(), vista=Vista())
juego.inicio()


#TODO cambir el modelo.mostrar_jugadores y ponerlo en vista