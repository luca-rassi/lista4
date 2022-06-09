from impostos import Imposto

class Livros():
    def __init__(self):
        self.livros = []

    def inserir(self, livro):
        self.livros.append(livro)

    def consultar_autor(self, autor):
        livros_do_autor = []
        for livro in self.livros:
            if livro.autor == autor:
                livros_do_autor.append(livro)
        return livros_do_autor

    def remover(self,livro):
        if livro in self.livros:
            self.livros.remove(livro)

    def imposto(self,livro):
        livro.imposto = Imposto.calcular_imposto(livro.preco_venda,livro.preco.Compra)
