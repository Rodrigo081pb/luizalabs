class Veiculo:
    def __init__(self, cor, rodas, ano, modelo, cavalos, preco, marca, placa):
        self.cor = cor
        self.rodas = rodas
        self.ano = ano
        self.modelo = modelo
        self.cavalos = cavalos
        self.preco = preco
        self.marca = marca
        self.placa = placa

    def ligar(self):
        print("Ligando...")

    def desligar(self):
        print("Desligando...")
        
class Moto(Veiculo):
    pass

moto = Moto("Vermelha", 2, 2020, "Honda CB500", 50, 25000, "Honda", "XYZ-1234")
moto.ligar()

class Carro(Veiculo):
    pass


