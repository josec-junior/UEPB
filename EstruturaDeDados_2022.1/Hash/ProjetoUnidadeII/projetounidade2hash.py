def gerarMenu(): #Método para gerar um menu na tela.
  print("-=" * 10)
  print("1. Inserir Funcionário")
  print("2. Buscar Salário de um Funcionário")
  print("3. Listar todos os Funcionários")
  print("0. Sair")
  print("-=" * 10)

class Funcionario:

  def __init__(self, nome, salario):
    self.nome = nome
    self.salario = salario

  def __str__(self):
    output = "[Nome: " + str(self.nome) + ", Salário: " + str(self.salario) + " R$]"
    return output

class Hash:

  def __init__(self, tamanho):
    self.tamanho = tamanho
    self.linhas = []
    self.gerarMatriz(tamanho) 
  
  def gerarMatriz(self, tamanho): #Método para gerar uma matriz que será utilizada para representar a tabela.
    for i in range(tamanho):
      self.linhas.append([] * 1) 

  def inserirFuncionario(self, funcionario): #Método para inserir um Funcionário na tabela.
    codigoPrimeiraLetra = ord(funcionario.nome[0])
    posicao = codigoPrimeiraLetra % self.tamanho
    self.linhas[posicao].append(funcionario)

  def buscarSalario(self, nome): #Método para retornar o salário de um Funcionário.
    for i in range(len(self.linhas)):
      for j in range(len(self.linhas[i])):
        if self.linhas[i][j].nome == nome:
          return self.linhas[i][j]
    return False

  def listarFuncionarios(self): #Método para listar todos os Funcionários da tabela.
    for i in range(len(self.linhas)):
      for j in range(len(self.linhas[i])):
        print(self.linhas[i][j], end = " ")
      print()


hash = Hash(10)
opcao = -1
while (opcao != 0):
  gerarMenu()
  opcao = int(input("Digite a operação que você deseja realizar: "))
  if opcao == 1:
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    funcionario = Funcionario(nome, salario)
    hash.inserirFuncionario(funcionario)
  elif opcao == 2:
    nome = input("Digite o nome do funcionário que você deseja buscar o salário: ")
    busca = hash.buscarSalario(nome)
    if (busca):
      print("O salário de", busca.nome, "é", busca.salario, "R$")
    else:
      print("Funcionário não encontrado!")
  elif opcao == 3:
    hash.listarFuncionarios()
  elif opcao == 0:
    print("Encerrando o sistema...")
