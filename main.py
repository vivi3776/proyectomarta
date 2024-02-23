from Controlador import Controlador
from Modelo import Modelo
from vista import Vista


juego = Controlador(modelo=Modelo(), vista=Vista())
juego.inicio()


#TODO revisar como se añade el dinero que se suma mal