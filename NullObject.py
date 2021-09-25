
# Padrão : Null Object
# Aluna  : Ana Júlia Oliveira Lins - 20191370002

# Classe original Filme
class Filme:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano

    def get_nome(self):
        return self._nome
    def set_nome(self, new):
         self._nome = new

    def get_ano(self):
        return self._ano
    def set_ano(self, new):
        self._ano = new

# Classe que que tratará o null do atributo 'ano' da classe Filme
class FilmeNullObject(Filme):

    def get_ano(self):
        return "Ano não encontrado"


# Classe que será a criadora do Filme, o método criarFilme(self) 
# levará em consideração qual a classe deverá ser inicializada
class FilmeCriador:
    def __init__(self, nome = None, ano = None):
        self._nome = nome
        self._ano = ano

    def criarFilme(self):
        if self._ano != None :
            return Filme(self._nome, self._ano)

        return FilmeNullObject(self._nome, None)

# Aqui é o main que rodará o Factory para criar os filmes, 
# e deverá retornar:
#
# Moana  -  2016
# Mulan  -  Ano não encontrado
#
# Em vez de retornar um erro na impressão do Filme sem o ano
def main():

    filme = FilmeCriador("Moana", 2016).criarFilme()
    filmeNull = FilmeCriador("Mulan").criarFilme()

    print("--------------------------------------------------")
    print(filme.get_nome() , " - " , filme.get_ano())
    print(filmeNull.get_nome() , " - " , filmeNull.get_ano())
    print("--------------------------------------------------")
      
main()