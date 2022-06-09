import email


def Cliente():
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
        self.compras = []
    
    def comprar(self, livro):
        self.compras.append(livro)

    def remover(self,cliente):
        if cliente in self.nome:
            self.nome.remove(cliente)