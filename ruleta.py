class Ruleta:
    gajos: list
    consonantes = dict.fromkeys("bcdfghjklmnpqrstvwxyz", False)
    vocales = dict.fromkeys("aeiou", False)
    panel: dict
    pista: list

    def __init__(self):
        self.panel = {
            "CANCIÓN POPULAR": "Melodía conocida y apreciada por un amplio publico",
            "REVOLUCIÓN INDUSTRIAL": "Paso de la producción manual a la industrial",
            "SMARTPHONE": "Dispositivo movil con funciones avanzadas",
        }
        self.pista = ["CANCIÓN POPULAR", "REVOLUCIÓN INDUSTRIAL", "SMARTPHONE"]

        self.gajos = [
            "QUIEBRA",  # quiebra
            "PIERDE TURNO",
            "COMODIN",
            "X2",
            "/2",
            "100",
            "50",
            "100",
            "150",
            "150",
            "100",
            "50",
            "100",
            "200",
            "50",
            "150",
            "50",
            "150",
            "100",
            "150",
            "100",
            "50",
            "100",
            "200",
        ]
