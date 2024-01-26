letras = {letra: False for letra in "abcdefghijklmnopqrstuvwxyz"}


class Ruleta:
    gajos: list
    letras: dict
    panel: str

    def __init__(self):
        self.panel = "paris"
        self.letras = dict.fromkeys("abcdefghijklmnopqrstuvwxyz", False)
        self.gajos = [
            "QUIEBRA",
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
