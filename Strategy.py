from abc import ABCMeta, abstractmethod

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

class Comparacao(metaclass=ABCMeta):

    @abstractmethod
    def comparar(pessoa1, pessoa2):
        pass


class StrategyComparePorIdade(Comparacao):

    def comparar(pessoa1, pessoa2):
        if(pessoa1.idade > pessoa2.idade):
            return f"{pessoa1.nome} é mais velha que {pessoa2.nome}"
        return f"{pessoa2.nome} é mais velha que {pessoa1.nome}"

class StrategyComparePorAltura(Comparacao):

    def comparar(pessoa1, pessoa2):
        if (pessoa1.altura > pessoa2.altura):
            return f"{pessoa1.nome} é mais alta que {pessoa2.nome}"
        return f"{pessoa2.nome} é mais alta que {pessoa1.nome}"

class StrategyComparePorPeso(Comparacao):

    def comparar(pessoa1, pessoa2):
        if (pessoa1.peso > pessoa2.peso):
            return f"{pessoa1.nome} é mais pesada que {pessoa2.nome}"
        return f"{pessoa2.nome} é mais pesada que {pessoa1.nome}"


def teste():
    pessoaA = Pessoa("jessica", 20, 70, 1.80)
    pessoaB = Pessoa("Joao", 40, 60, 1.90)

    print(StrategyComparePorAltura.comparar(pessoaA, pessoaB))
    print(StrategyComparePorIdade.comparar(pessoaA,pessoaB))
    print(StrategyComparePorPeso.comparar(pessoaA, pessoaB))

teste()
