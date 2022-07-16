class Disciplina: #Classe da Disciplina.

  def __init__(self, nome):
    self.nome = nome

class Aluno: #Classe do Aluno.

  def __init__(self, nome):
    self.nome = nome
    self.disciplinas = [] #Sublista a qual contém as disciplinas do aluno.
    self.next = None

class Universidade: #Classe da Multilista

  def __init__(self):
    self.head = None

  def cadastrarAluno(self, nome): #Método para cadastrar um aluno.
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Aluno(nome)
    else:
      self.head = Aluno(nome)

  def buscarAluno(self, nome): #Método para buscar um aluno.
    aux = self.head
    while aux.next and aux.nome != nome:
      aux = aux.next
    return aux

  def cadastrarDisciplina(self, nomeAluno, nomeDisciplina): #Método para cadastrar uma disciplina.
    aluno = self.buscarAluno(nomeAluno)
    if aluno:
      aluno.disciplinas.append(Disciplina(nomeDisciplina))
    else:
      print("Aluno inexistente!")

  def relatorio(self): #Método para imprimir todos os alunos e todas as disciplinas de cada um.
    aux = self.head
    while aux:
      print(aux.nome,"\n-----------")
      for disciplina in aux.disciplinas:
        print(disciplina.nome)
      aux = aux.next
      print()

  def removerAluno(self, nome): #Método para remover um aluno.
    if self.head:
      aux = self.head
      if aux.nome == nome:
        self.head = aux.next
        del aux #Deletar caso o aluno esteja na primeira posição da lista (self.head)
      else:
        while aux and (aux.nome != nome): #Percorrimento na lista, caso o aluno não esteja na primeira posição.
          ant = aux
          aux = aux.next
        ant.next = aux.next
        del aux
    else:
      print("Não há nenhum aluno cadastrado no sistema ainda!")

  def removerDisciplina(self, nomeAluno, nomeDisciplina): #Método para remover uma disciplina.
    if self.head:
      aluno = self.buscarAluno(nomeAluno)
      if aluno:
        for disciplina in aluno.disciplinas:
          if disciplina.nome == nomeDisciplina:
            aluno.disciplinas.remove(disciplina)
    else:
      print("Não há nenhum aluno cadastrado no sistema ainda!")

uepb = Universidade()
uepb.cadastrarAluno("Júnior")
uepb.cadastrarAluno("Rebeca")
uepb.cadastrarAluno("João")
uepb.cadastrarAluno("Ana")
uepb.cadastrarDisciplina("Júnior","Estrutura de Dados")
uepb.cadastrarDisciplina("Rebeca","Estrutura de Dados")
uepb.cadastrarDisciplina("Rebeca","Algoritmos")
uepb.cadastrarDisciplina("João", "Paradigmas de Linguagem de Programação")
uepb.cadastrarDisciplina("Ana", "Sistemas de Informação")
uepb.relatorio()

print("-="*10)
print()

uepb.removerDisciplina("Rebeca", "Algoritmos")
uepb.removerAluno("João")
uepb.relatorio()
