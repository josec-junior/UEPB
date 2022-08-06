class Disciplina:

  def __init__(self, nome):
    self.nome = nome

class Aluno:

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula
    self.disciplinas = []

class Universidade:

  def __init__(self, nome):
    self.nome = nome
    self.alunos = []
    self.next = None

class Multilista:

  def __init__(self):
    self.head = None

  def cadastrarUniversidade(self, nome):
    if self.head:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Universidade(nome)
    else:
      self.head = Universidade(nome)
  
  def buscarUniversidade(self, nome):
    aux = self.head
    while aux and aux.nome != nome:
      aux = aux.next
    return aux
  
  def cadastrarAluno(self, nomeAluno, matricula, nomeUniversidade):
    buscaUniversidade = self.buscarUniversidade(nomeUniversidade)
    if buscaUniversidade:
      aluno = Aluno(nomeAluno, matricula)
      buscaUniversidade.alunos.append(aluno)
      print("Aluno cadastrado com sucesso!")
    else:
      print("Universidade inexistente!")
  
  def buscarAluno(self, nomeAluno, matricula, nomeUniversidade):
    buscaUniversidade = self.buscarUniversidade(nomeUniversidade)
    if buscaUniversidade:
      for aluno in buscaUniversidade.alunos:
        if aluno.nome == nomeAluno and aluno.matricula == matricula:
          return aluno
    return False

  def cadastrarDisciplina(self, nomeDisciplina, nomeAluno, matricula, nomeUniversidade):
    buscaAluno = self.buscarAluno(nomeAluno, matricula, nomeUniversidade)
    if buscaAluno:
      disciplina = Disciplina(nomeDisciplina)
      buscaAluno.disciplinas.append(disciplina)
      print("Disciplina cadastrada com sucesso!")
    else:
      print("Aluno inexistente!")

  def buscarDisciplina(self, nomeDisciplina, nomeAluno, matricula, nomeUniversidade):
    buscaAluno = self.buscarAluno(nomeAluno, matricula, nomeUniversidade)
    if buscaAluno:
      for disciplina in buscaAluno.disciplinas:
        if disciplina.nome == nomeDisciplina:
          return disciplina
    return False

  def relatorio(self):
    aux = self.head
    while aux:
      print(aux.nome)
      for aluno in aux.alunos:
        print(" ", aluno.nome, "-", aluno.matricula)
        for disciplina in aluno.disciplinas:
          print("    ", disciplina.nome)
        print()
      aux = aux.next

multilista = Multilista()
multilista.cadastrarUniversidade("UEPB")
multilista.cadastrarUniversidade("UFCG")
multilista.cadastrarUniversidade("UFPB")
multilista.cadastrarAluno("João", 1, "UEPB")
multilista.cadastrarAluno("Alan", 2, "UFCG")
multilista.cadastrarAluno("Luiza", 3, "UFPB")
multilista.cadastrarAluno("Nathalia", 4, "UEPB")
multilista.cadastrarAluno("Joana", 5, "UFCG")
multilista.cadastrarAluno("Henrique", 6, "UFPB")
multilista.cadastrarDisciplina("Física I", "João", 1, "UEPB")
multilista.cadastrarDisciplina("Estrutura de Dados", "Alan", 2, "UFCG")
multilista.cadastrarDisciplina("Anatomia", "Luiza", 3, "UFPB")
multilista.cadastrarDisciplina("Matemática III", "Nathalia", 4, "UEPB")
multilista.cadastrarDisciplina("Cálculo Integral e Diferencial II", "Joana", 5, "UFCG")
multilista.cadastrarDisciplina("Direito Penal", "Henrique", 6, "UFPB")
multilista.relatorio()
