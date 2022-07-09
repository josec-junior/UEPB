produtos = {}

def cadastrarProduto(produtos):
  produto = input("Digite o nome do produto: ")
  preco = float(input("Digite o preço deste produto: "))
  produtos[produto] = produtos.get(produto, preco)

def removerProduto(produtos):
  produto = input("Digite o nome do produto que você deseja remover: ")
  if produto in produtos:
    del produtos[produto]
  else:
    print("Este produto não está cadastrado no sistema!")

def buscarProduto(produtos):
  produto = input("Digite o nome do produto que você deseja procurar: ")
  if produto in produtos:
    print("Produto:", produto)
    print("Preço:", produtos[produto], "R$")
  else:
    print("Este produto não está cadastrado no sistema!")

def listarProdutos(produtos):
  if (len(produtos) == 0):
    print("Nenhum produto cadastrado no sistema!")
  else:
    print("-=" * 10)
    for k,v in produtos.items():
      print("Produto:", k)
      print("Preço:", v, "R$")
      print()
    print("-=" * 10)
    print()

def menu():
  print("-=" * 10)
  print("1. Cadastrar um Novo Produto")
  print("2. Remover um Produto")
  print("3. Buscar um Produto")
  print("4. Listar todos os Produtos")
  print("5. Sair")
  print("-=" * 10)

opcao = 0
while (opcao != 5):
  menu()
  opcao = int(input("Digite a operação que você deseja realizar: "))
  if (opcao == 1):
    cadastrarProduto(produtos)
  elif (opcao == 2):
    removerProduto(produtos)
  elif (opcao == 3):
    buscarProduto(produtos)
  elif (opcao == 4):
    listarProdutos(produtos)
  elif (opcao == 5):
    print("Encerrando o sistema...")
