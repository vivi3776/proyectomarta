from dataclasses import dataclass
@dataclass
class Ruleta:
    GAJOS: list
    consonantes = dict.fromkeys("bcdfghjklmnpqrstvwxyz", False)
    vocales = dict.fromkeys("aeiou", False)
    panel: list
    pista: list

    def __init__(self):
        self.panel = []
        self.pista = []

        self.GAJOS = [
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

