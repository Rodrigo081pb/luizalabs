# cor, valor , ano, aro | pedalar, frear, trocar marcha

class Bicicleta:
    def __init__(self, cor, valor, ano, aro, buzina):
        self.cor = cor
        self.valor = valor
        self.ano = ano
        self.aro = aro
        self.buzina = buzina
        self.marcha = 1

    def tocar_buzina(self):
        return "bibiiiii"
    
    def pedalar(self):
        return "A bicicleta está pedalando."

    def frear(self):
        return "A bicicleta está freando."

    def trocar_marcha(self, nova_marcha):
        if 1 <= nova_marcha <= 21:
            self.marcha = nova_marcha
            return f"Marcha trocada para {self.marcha}."
        else:
            return "Marcha inválida. Escolha entre 1 e 21."
        
bicicleta1 = Bicicleta("vermelha", 1200.00, 2020, 26, "bibiiiii")