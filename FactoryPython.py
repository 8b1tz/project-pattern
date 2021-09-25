from abc import ABCMeta, abstractstaticmethod

class IFuncionario(metaclass = ABCMeta):
    @abstractstaticmethod
    def Funcionario_Metodo():
        "xpto"

class Vendedor(IFuncionario):

    def __init__(self):
        self.nome = 'Nome do vendedor'

    def Funcionario_Metodo(self):
        print('eu sou um vendedor')

class Faxineiro(IFuncionario):

    def __init__(self):
        self.nome = 'Nome do faxineiro'

    def Funcionario_Metodo(self):
        print('eu sou um faxineiro')

class Gerente(IFuncionario):

    def __init__(self):
        self.nome = 'Nome do gerente'

    def Funcionario_Metodo(self):
        print('eu sou um Gerente')

class FuncionarioFactory:

    @staticmethod
    def cadastrar_funcionario(funcionario_func):
        if funcionario_func == "Vendedor":
            return Vendedor()
        if funcionario_func == "Faxineiro":
            return Faxineiro()
        if funcionario_func == "Gerente":
            return Gerente()
        print('tipo invalido!')
        return -1

def main():
    funcionario_func = input("Qual a função do funcionario cadastrado?: ")
    funcionario = FuncionarioFactory.cadastrar_funcionario(funcionario_func)
    funcionario.Funcionario_Metodo()

main()
