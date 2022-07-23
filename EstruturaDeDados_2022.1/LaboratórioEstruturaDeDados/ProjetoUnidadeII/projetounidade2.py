def gerarMenu():
  print("-=" * 20)
  print("1. Cadastrar Aluno")
  print("2. Cadastrar Disciplina em Aluno")
  print("3. Cadastrar Nota na Disciplina do Aluno")
  print("4. Remover Aluno")
  print("5. Remover Disciplina de Aluno")
  print("6. Remover Nota de Disciplina de Aluno")
  print("7. Atualizar Aluno")
  print("8. Atualizar Disciplina de Aluno")
  print("9. Atualizar Nota da Disciplina de Aluno")
  print("10. Visualizar Média do Aluno na Disciplina")
  print("11. Visualizar Alunos em Ordem Alfabética")
  print("12. Visualizar Alunos com Média Menor do que 7")
  print("13. Visualizar Alunos com Média Maior ou Igual a 7")
  print("14. Visualizar Notas das Disciplinas do Aluno")
  print("15. Sair")
  print("-=" * 20)
  
class Disciplina:

  def __init__(self, nome):
    self.nome = nome
    self.notas = []
    self.next = None

  def calcularMedia(self):
    quantNotas = len(self.notas)
    if quantNotas == 2:
      media = (self.notas[0] + self.notas[1]) // 2
      return media
    else:
      return -1
  
  def adicionarNota(self, nota):
    quantNotas = len(self.notas)
    if quantNotas < 2:
      self.notas.append(nota)
      return True
    else:
      return False

  def atualizarNota(self, posicao, nota):
    if posicao == 1:
      self.notas[0] = nota
    elif posicao == 2:
      self.notas[1] = nota

  def __str__(self):
    output = str(self.nome)
    output += "\n"
    quantNotas = len(self.notas)
    if quantNotas > 0:
      for i in range(quantNotas):
        output += "     "
        output += str(i + 1) + "º Nota: " + str(self.notas[i]) + "\n"
    return output

class Aluno:

  def __init__(self, nome, matricula):
    self.nome = nome
    self.matricula = matricula
    self.disciplinas = []
    self.next = None

  def __str__(self):
    output = "[Nome: " + str(self.nome) + ", Matrícula: " + str(self.matricula) + "]"
    output += "\n--- Disciplinas ---"
    quantDisciplinas = len(self.disciplinas)
    if quantDisciplinas > 0:
      for i in range(quantDisciplinas):
        output += "\n   " + str(self.disciplinas[i])
    return output

class Universidade:

  def __init__(self, value = None):
    self.data = value
    self.left = None
    self.right = None

  def inserirAluno(self, aluno):
    if not self.data:
      self.data = aluno
    elif aluno.nome < self.data.nome:
      if self.left:
        self.left.inserirAluno(aluno)
      else:
        self.left = Universidade(aluno)
    elif aluno.nome > self.data.nome:
      if self.right:
        self.right.inserirAluno(aluno)
      else:
        self.right = Universidade(aluno)

  def buscarAluno(self, nome, matricula):
    if self.data.nome == nome and self.data.matricula == matricula:
      return self.data
    elif nome < self.data.nome:
      if self.left:
        return self.left.buscarAluno(nome, matricula)
    elif nome > self.data.nome:
      if self.right:
        return self.right.buscarAluno(nome, matricula)
    return None

  def imprimirOrdemCentral(self):
    if self.data:
      if self.left:
        self.left.imprimirOrdemCentral()
      print(self.data)
      print()
      if self.right:
        self.right.imprimirOrdemCentral()

  def cadastrarDisciplina(self, nomeAluno, matriculaAluno, nomeDisciplina):
    busca = self.buscarAluno(nomeAluno, matriculaAluno)
    if busca:
      busca.disciplinas.append(Disciplina(nomeDisciplina))
      print("Disciplina cadastrada com sucesso!")
    else:
      print("Aluno não encontrado!")

  def buscarDisciplina(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaAluno = self.buscarAluno(nomeAluno, matriculaAluno)
    if buscaAluno:
      for disciplina in buscaAluno.disciplinas:
        if disciplina.nome == nomeDisciplina:
          return disciplina
    else:
      return False

  def cadastrarNota(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaDisciplina = self.buscarDisciplina(nomeAluno, matriculaAluno, nomeDisciplina)
    if buscaDisciplina:
      nota = float(input("Digite a nota do aluno: "))
      cadastroNota = buscaDisciplina.adicionarNota(nota)
      if (cadastroNota):
        print("Nota cadastrada com sucesso!")
      else:
        print("O aluno já possui 2 notas nesta disciplina! Logo, não é possível cadastrar mais notas.")
    else:
      print("Disciplina não encontrada!")

  def alterarNota(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaDisciplina = self.buscarDisciplina(nomeAluno, matriculaAluno, nomeDisciplina)
    if buscaDisciplina:
      posicao = int(input("Você quer alterar a nota 1 ou nota 2? "))
      while (posicao != 1 and posicao != 2):
        print("Valor inválido! informe se você deseja alterar a nota 1 ou a nota 2.")
        posicao = int(input("Você quer alterar a nota 1 ou a nota 2? "))
      nota = float(input("Digite a nota do aluno: "))
      buscaDisciplina.atualizarNota(posicao, nota)

  def visualizarMedia(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaDisciplina = self.buscarDisciplina(nomeAluno, matriculaAluno, nomeDisciplina)
    if buscaDisciplina:
      media = buscaDisciplina.calcularMedia()
      if (media == -1):
        print("Não é possível calcular a média desta disciplina, pois ainda não possui 2 notas cadastradas.")
      else:
        print("Média de", nomeAluno, "na disciplina de", nomeDisciplina, "é", media)
    else:
      print("Disciplina não encontrada!")

  def atualizarDisciplina(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaDisciplina = self.buscarDisciplina(nomeAluno, matriculaAluno, nomeDisciplina)
    if buscaDisciplina:
      novoNome = input("Digite o novo nome da Disciplina: ")
      buscaDisciplina.nome = novoNome
      buscaDisciplina.notas[0] = float(input("Digite a nota 1 da disciplina: "))
      buscaDisciplina.notas[1] = float(input("Digite a nota 2 da disciplina: "))
    else:
      print("Disciplina não encontrada!")

  def atualizarAluno(self, nome, matricula):
    buscaAluno = self.buscarAluno(nome, matricula)
    if buscaAluno:
      novoNome = input("Digite o novo nome do aluno: ")
      buscaAluno.nome = novoNome
      novaMatricula = int(input("Digite a nova matrícula do aluno: "))
      buscaAluno.matricula = novaMatricula
      aux = buscaAluno
      self.removerAluno(buscaAluno.nome)
      self.inserirAluno(aux)
      print("Aluno atualizado com sucesso!")
    else:
      print("Aluno não encontrado!")

  def visualizarNotas(self, nome, matricula):
    buscaAluno = self.buscarAluno(nome, matricula)
    if buscaAluno:
      print(buscaAluno)
    else:
      print("Aluno não encontrado!")

  def visualizarMediasMenoresQue7(self):
    if self.data:
      if self.left:
        self.left.visualizarMediasMenoresQue7()
      for disciplina in self.data.disciplinas:
        media = disciplina.calcularMedia()
        if media < 7 and media >= 0:
          print(self.data.nome, "-", disciplina.nome,", Média:", media)
      if self.right:
        self.right.visualizarMediasMenoresQue7()

  def visualizarMediasMaioresOuIgualA7(self):
    if self.data:
      if self.left:
        self.left.visualizarMediasMaioresOuIgualA7()
      for disciplina in self.data.disciplinas:
        media = disciplina.calcularMedia()
        if media >= 7:
          print(self.data.nome, "-", disciplina.nome,", Média: ", media)
      if self.right:
        self.right.visualizarMediasMaioresOuIgualA7()

  def removerDisciplina(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaAluno = self.buscarAluno(nomeAluno, matriculaAluno)
    if buscaAluno:
      for disciplina in buscaAluno.disciplinas:
        if disciplina.nome == nomeDisciplina:
          buscaAluno.disciplinas.remove(disciplina)
          print("Disciplina", disciplina.nome, "removida!") 
    else:
      print("Aluno não encontrado!")
  
  def removerNota(self, nomeAluno, matriculaAluno, nomeDisciplina):
    buscaDisciplina = self.buscarDisciplina(nomeAluno, matriculaAluno, nomeDisciplina)
    if buscaDisciplina:
      posicao = int(input("Você deseja remover a nota 1 ou a nota 2? "))
      while (posicao != 1 and posicao != 2):
        print("Valor inválido! informe se você deseja remover a nota 1 ou a nota 2.")
        posicao = int(input("Você deseja remover a nota 1 ou a nota 2? "))
      if posicao == 1:
        buscaDisciplina.notas.pop(0)
      else:
        buscaDisciplina.notas.pop(1)
    else:
      print("Disciplina não encontrada!")

  def encontrarMenor(self):
    while self.left:
      self.left.encontrarMenor()
    return self.data

  def removerAluno(self, nome):
    if nome < self.data.nome:
      self.left = self.left.removerAluno(nome)
    elif nome > self.data.nome:
      self.right = self.right.removerAluno(nome)
    else:
      if self.left is None:
        return self.right
      elif self.right is None:
        return self.left
      else:
        aux = self.right.encontrarMenor()
        self.data = aux
        self.right = self.right.removerAluno(self.data.nome)
    return self

uepb = Universidade()
opcao = 0
while opcao != 15:
  gerarMenu()
  opcao = int(input("Digite a operação que você deseja realizar: "))
  if opcao == 1:
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    aluno = Aluno(nome, matricula)
    uepb.inserirAluno(aluno)
  elif opcao == 2:
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    nomeDisciplina = input("Digite o nome da disciplina: ")
    uepb.cadastrarDisciplina(nome, matricula, nomeDisciplina)
  elif opcao == 3:
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matrícula do aluno: "))
    nomeDisciplina = input("Digite o nome da disciplina: ")
    uepb.cadastrarNota(nome, matricula, nomeDisciplina)
  elif opcao == 4:
    nome = input("Digite o nome do aluno que você deseja remover: ")
    uepb.removerAluno(nome)
  elif opcao == 5:
    nome = input("Digite o nome do aluno que possui a discplina que você deseja remover: ")
    matricula = int(input("Digite a matrícula do aluno que possui a disciplina que  você deseja remover: "))
    nomeDisciplina = input("Digite o nome da disciplina que você deseja remover: ")
    uepb.removerDisciplina(nome, matricula, nomeDisciplina)
  elif opcao == 6:
    nome = input("Digite o nome do aluno que possui a disciplina que você deseja remover a nota: ")
    matricula = int(input("Digite a matrícula do aluno que possui a disciplina que você deseja remover a nota: "))
    nomeDisciplina = input("Digite o nome da disciplina que você deseja remover a nota: ")
    uepb.removerNota(nome, matricula, nomeDisciplina)
  elif opcao == 7:
    nome = input("Digite o nome do aluno que você deseja atualizar: ")
    matricula = int(input("Digite a matrícula aluno que você deseja atualizar: "))
    uepb.atualizarAluno(nome, matricula)
  elif opcao == 8:
    nome = input("Digite o nome do aluno que possui a disciplina que você deseja atualizar: ")
    matricula = int(input("Digite a matrícula aluno que possui a disciplina que você deseja atualizar: "))
    nomeDisciplina = input("Digite o nome da disciplina que você deseja atualizar: ")
    uepb.atualizarDisciplina(nome, matricula, nomeDisciplina)
  elif opcao == 9:
    nome = input("Digite o nome do aluno que possui a disciplina que você deseja atualizar a nota: ")
    matricula = int(input("Digite a matrícula aluno que possui a disciplina que você deseja atualizar a nota: "))
    nomeDisciplina = input("Digite o nome da disciplina que você deseja atualizar a nota: ")
    uepb.alterarNota(nome, matricula, nomeDisciplina)
  elif opcao == 10:
    nome = input("Digite o nome do aluno que você deseja visualizar a média: ")
    matricula = int(input("Digite a matrícula do aluno que você deseja visualizar a média: "))
    nomeDisciplina = input("Digte o nome da disciplina que você deseja visualizar a média: ")
    uepb.visualizarMedia(nome, matricula, nomeDisciplina)
  elif opcao == 11:
    print("--- Alunos em ordem alfabética ---")
    uepb.imprimirOrdemCentral()
    print("-" * 9)
  elif opcao == 12:
    print("--- Alunos com médias menores do que 7 ---")
    uepb.visualizarMediasMenoresQue7()
    print("-" * 9)
  elif opcao == 13:
    print("--- Alunos com médias maiores ou iguais a 7 ---")
    uepb.visualizarMediasMaioresOuIgualA7()
    print("-" * 9)
  elif opcao == 14:
    nome = input("Digite o nome do aluno que você deseja visualizar as notas: ")
    matricula = int(input("Digite a matrícula do aluno que você deseja visualizar as notas: "))
    uepb.visualizarNotas(nome, matricula)
  elif opcao == 15:
    print("Encerrando o sistema...")