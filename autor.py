from livros import Livros

class Autores():
    def __init__(self,nome,email,titulos):
        self.nome = nome
        self.email = email
        self.titulos.append(titulos)
    
    def acrescentar_livro(self,titulo):
        count = 0
        for livro in self.livros:
            if livro.nome == titulo:
                count =+ count
        if count == 0:
            self.titulos.append(titulo)    