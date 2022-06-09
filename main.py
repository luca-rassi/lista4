from collections import namedtuple
from livros import Livros

def main():            
    Livro = namedtuple('livro', 'titulo autor genero edicao editor preco_Venda preco_Compra imposto')

    livro = Livros()
    livro.inserir(Livro('Orgulho e Preconceito', 'Jane Austen', 'Romance', '4','xist classsics', 55, 35, 0.1))
    livro.inserir(Livro('1984', 'George Orwell', 'Romance/Ficção', '8','companhia das letras', 40, 15, 0.1))
    livro.inserir(Livro('Admiravel mundo novo', 'Aldous Huxley', 'Ficção', '2','biblioteca azul', 45, 25, 0.1))
    livro.inserir(Livro('A revolução dos bichos', 'George Orwell', 'Ficção', '5','companhia das letras', 45, 20, 0.1))
    livro.inserir(Livro('A planta de Ferro', 'George Orwell', 'Ficção', '3','companhia das letras', 40, 20, 0.1))
    livro.inserir(Livro('Harry Potter e a Pedra filosofal', 'J K Rolling', 'Fantasia', '4','companhia das letras', 30, 10, 0.1))
    livro.inserir(Livro('Harry Potter e a Câmera Secreta', 'J K Rolling','Fantasia', '4','companhia das letras', 30, 10, 0.1))
    livro.inserir(Livro('Harry Potter e o prisioneiro de Askaban', 'J K Rolling','Fantasia', '4','companhia das letras', 30, 10, 0.1))
    livro.inserir(Livro('Harry Potter e a cálice de fogo', 'J K Rolling','Fantasia', '4','companhia das letras', 30, 10, 0.1))
    livro.inserir(Livro('Harry Potter e a ordem da Fenix', 'J K Rolling','Fantasia', '4','companhia das letras', 35, 10, 0.1))
    livro.inserir(Livro('Harry Potter e o enigma do príncipe', 'J K Rolling','Fantasia', '4','companhia das letras', 35, 10, 0.1))


    #print(livro.consultar_autor('George Orwell'))
    #print(livro.consultar_autor('Aldous Huxley'))

    
    for livro in livro.consultar_autor('Jane Austen'):
            print(livro.titulo)
            print('preço: ',livro.preco_Venda)


                  
main()