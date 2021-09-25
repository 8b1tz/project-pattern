from abc import ABCMeta, abstractmethod

class Pessoa:

    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

class StrategyComparacao(metaclass=ABCMeta):

    @abstractmethod
    def comparar(pessoa1, pessoa2):
        pass


class StrategyComparePorIdade(StrategyComparacao):
    def comparar(pessoa1, pessoa2):
        if(pessoa1.idade > pessoa2.idade):
            return f"{pessoa1.nome} é mais velha que {pessoa2.nome}"
        return f"{pessoa2.nome} é mais velha que {pessoa1.nome}"

class StrategyComparePorAltura(StrategyComparacao):
    def comparar(pessoa1, pessoa2):
        if (pessoa1.altura > pessoa2.altura):
            return f"{pessoa1.nome} é mais alta que {pessoa2.nome}"
        return f"{pessoa2.nome} é mais alta que {pessoa1.nome}"

class StrategyComparePorPeso(StrategyComparacao):
    def comparar(pessoa1, pessoa2):
        if (pessoa1.peso > pessoa2.peso):
            return f"{pessoa1.nome} é mais pesada que {pessoa2.nome}"
        return f"{pessoa2.nome} é mais pesada que {pessoa1.nome}"

class GeradorComparacao:

    def geradorComparacao(self, strategyComparacao):
        self.strategyComparacao  = strategyComparacao

    def gerarComparacao(pessoa1, pessoa2):
        return strategyComparacao.comparar(pessoa1, pessoa2)

def teste():
    geradorComparacao = GeradorComparacao(StrategyComparacao(StrategyComparePorAltura))

    pessoaA = Pessoa("jessica", 20, 70, 1.80)
    pessoaB = Pessoa("Joao", 40, 60, 1.90)

    geradorComparacao.gerarComparacao(pessoaA, pessoaB)


teste()
