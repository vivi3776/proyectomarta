class Ruleta:
    gajos: list
    letras: dict
    panel: dict
    pista: list

    def __init__(self):
        self.panel = {
            "CANCIÓN POPULAR": "Melodía conocida y apreciada por un amplio público",
            "REVOLUCIÓN INDUSTRIAL": "Paso de la producción manual a la industrial.",
            "SMARTPHONE": "Dispositivo móvil con funciones avanzadas",
        }
        self.pista = ["CANCIÓN POPULAR", "REVOLUCIÓN INDUSTRIAL", "SMARTPHONE"]

        self.letras = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", False)
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
