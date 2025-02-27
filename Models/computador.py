
class Computador:
    def __init__(self, id: int, nome: str, ramTotal: float, ramLivre: float, qtdProcessadores: int, armazTotal: float, armazLivre: float) -> None:
        self.id = id
        self.nome = nome
        self.ramTotal = ramTotal
        self.ramLivre = ramLivre
        self.qtdProcessadores = qtdProcessadores
        self.armazTotal = armazTotal
        self.armazLivre = armazLivre