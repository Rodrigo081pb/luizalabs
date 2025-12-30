class Animal():
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie

    def fazer_som(self):
        pass
    
    def latido(self):
        return "Au Au"
    
    def miado(self):
        return "Miau"

class Mamifero(Animal): 
    def __init__(self, nome, especie, patas=4):
        super().__init__(nome, especie)
        self.patas = patas

    
class Cachorro(Animal, Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Cachorro")
        self.raca = raca

    def fazer_som(self):
        return self.latido()
    
class Gato(Animal, Mamifero):
    def __init__(self, nome, raca):
        super().__init__(nome, especie="Gato")
        self.raca = raca

    def fazer_som(self):
        return self.miado()
    
dog = Cachorro("Rex", "Labrador")
print(f"{dog.nome} diz: {dog.fazer_som()}")

cat = Gato("Mimi", "Siamês")
print(f"{cat.nome} diz: {cat.fazer_som()}")
