class Livro:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
        self.livros = []
        self.next = None

class Biblioteca:
    def __init__(self):
        self.head = None

    def cadastrarAluno(self, nome, matricula):
        if (self.head):
            aux = self.head
            while (aux.next):
                aux = aux.next
            aux.next = Aluno(nome, matricula)
        else:
            self.head = Aluno(nome, matricula)

    def buscarAluno(self, nome, matricula):
        aux = self.head
        while aux and (aux.nome != nome or aux.matricula != matricula):
            aux = aux.next
        return aux

    def cadastrarLivro(self, titulo, ano, nome, matricula):
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
            aluno.livros.append(Livro(titulo, ano))
        else:
            print("Este aluno não está cadastrado no sistema!")

    def listarLivros(self, nome, matricula):
        aluno = self.buscarAluno(nome, matricula)
        print("--- Livros ---")
        if aluno:
            for livro in aluno.livros:
                print(livro.titulo, "-", livro.ano)
        else:
            print("Este aluno não está cadastrado no sistema!")
        print()

    def relatorio(self):
        aux = self.head
        while (aux):
            print(aux.nome, "-", aux.matricula, "\n-------------------------")
            for livro in aux.livros:
                print(livro.titulo)
                print(" ", livro.ano)
            aux = aux.next
            print()

    def removerAluno(self, nome, matricula):
        if self.head:
            aux = self.head
            if aux.nome == nome and aux.matricula == matricula:
              self.head = aux.next
              del aux
            else:
              while aux and (aux.nome != nome or aux.matricula != matricula):
                  ant = aux
                  aux = aux.next
              ant.next = None
              del aux
        else:
            print("Não há nenhum aluno cadastrado no sistema ainda!")

    def removerLivro(self, nome, matricula, titulo, ano):
      if self.head:
        aluno = self.buscarAluno(nome, matricula)
        if aluno:
          for livro in aluno.livros:
            if livro.titulo == titulo and livro.ano == ano:
              aluno.livros.remove(livro)
      else:
        print("Não há nenhum aluno cadastrado no sistema ainda!")

bibli = Biblioteca()
bibli.cadastrarAluno("Júnior", 3)
bibli.cadastrarAluno("Miguel", 5)
bibli.cadastrarLivro("LOTR", 1955, "Júnior", 3)
bibli.cadastrarLivro("PHP", 2004, "Júnior", 3)
bibli.cadastrarLivro("HP", 1998, "Miguel", 5)
bibli.relatorio()
bibli.removerAluno("Júnior", 3)
bibli.relatorio()
