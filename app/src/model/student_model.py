# Este arquivo contém as estruturas de dados ou modelos.

class Student:
    def __init__(self, nome, idade, peso, altura, estado_saude):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.estado_saude = estado_saude
        self.imc = self.calculate_imc()

    def calculate_imc(self):
        return self.peso / (self.altura ** 2)