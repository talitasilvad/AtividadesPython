class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos=0):
        for _ in range(anos):
            self.idade += 1
            if self.idade < 21:
                self.altura += 0.5

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, cm):
        self.altura += cm

pessoa = Pessoa("Carlos", 18, 80, 170)
pessoa.envelhecer(11)
pessoa.engordar(12)    
pessoa.emagrecer(4)   
pessoa.crescer(0)

print(f"Nome: {pessoa.nome}")
print(f"Idade: {pessoa.idade} anos")
print(f"Peso: {pessoa.peso} kg")
print(f"Altura: {pessoa.altura} cm")
