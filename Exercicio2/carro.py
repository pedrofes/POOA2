from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, ligado, portas):
        super().__init__(marca, modelo, ligado)
        self.portas = portas

    def __str__(self):
        return f"{super().__str__()} - Portas: {self.portas}"

    #def __str__(self):
        #parte_pai = super().__str__()
        #return f'{parte_pai}. O carro também possui {self.portas} portas.'