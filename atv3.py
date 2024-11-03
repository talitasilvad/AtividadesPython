class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self, novoNome):
        self.nome = novoNome

    def alterarFome(self, novaFome):
        self.fome = novaFome

    def alterarSaude(self, novaSaude):
        self.saude = novaSaude

    def alterarIdade(self, novaIdade):
        self.idade = novaIdade   

    def retornarNome(self):
        return self.nome

    def retornarFome(self):
        return self.fome

    def retornarSaude(self):
        return self.saude

    def retornarIdade(self):
        return self.idade  

    def imprimir(self):
        print(f"Bichinho Virtual: {self.nome}")
        print(f"Fome: {self.fome}")
        print(f"Saúde: {self.saude}")
        print(f"Idade: {self.idade}")

tamagoshi1 = BichinhoVirtual("Tamagoshi", 0, 100, 0)
tamagoshi2 = BichinhoVirtual("Tamagoshi", 0, 100, 0)

tamagoshi1.alterarNome("Mel")
tamagoshi1.alterarFome(17)
tamagoshi1.alterarSaude(85)
tamagoshi1.alterarIdade(4)

tamagoshi2.alterarNome("Snow")
tamagoshi2.alterarFome(10)
tamagoshi2.alterarSaude(90)
tamagoshi2.alterarIdade(1)

tamagoshi1.imprimir()
print()
tamagoshi2.imprimir()   
                 
