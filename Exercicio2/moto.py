from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, ligado, tipo):
        super().__init__(marca, modelo, ligado)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} - Tipo: {self.tipo}"


