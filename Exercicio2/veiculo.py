class Veiculo():
    def __init__(self, marca, modelo, ligado):
        self.marca = marca
        self.modelo = modelo
        self._ligado = False

    def __str__(self):
        return f"{self.marca} {self.modelo} - Status: {'Ligado' if self._ligado else 'Desligado'}"