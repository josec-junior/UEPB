class Fila:

  def __init__(self): #Método Construtor.
    self.head = []

  def push(self, value): #Método para adicionar um elemento no final da fila. 
    self.head.append(value)

  def pop(self): #Método para remover o primeiro elemento da fila.
    return self.head.pop(0)

  def isEmpty(self): #Método para retornar se a fila está vazia ou não. (True - se estiver, False - se não estiver)
    return len(self.head) == 0

  def __str__(self): #Método toString() da classe Fila.
    output = ""
    if self.isEmpty():
      output = "Fila vazia."
    else:
      tamanho = len(self.head)
      for i in range(tamanho):
        output += "-[" + str(self.head[i]) + "]- "
    return output

class Cliente:

  def __init__(self, nome):
    self.nome = nome
    self.compras = [] #Lista de compras do cliente.
  
  def realizarCompra(self, valorProduto): #Método para adicionar um produto a lista de compras do cliente.
    self.compras.append(valorProduto) 

  def valorTotalCompra(self): #Método para calcular o valor total da compra do cliente.
    tamanho = len(self.compras)
    soma = 0
    for i in range(tamanho):
      soma += self.compras[i]
    return soma

  def __str__(self): #Método toString() da classe Cliente.
    output = "Nome: " + self.nome 
    return output

class Atendimento:

  def __init__(self): 
    pass #Método construtor vazio.
    #Esta classe não possui atributos, apenas métodos, pois ela foi feita apenas para integrar a classe Cliente com a classe Fila.

  def inserirCliente(self, fila, cliente): #Método para inserir um cliente na fila.
    fila.push(cliente)

  def atenderCliente(self, fila): #Método para atender (remover) o primeiro cliente da fila.
    if fila.isEmpty():
      print("Não há mais clientes na fila!")
    else:
      total = fila.head[0].valorTotalCompra()
      print("Cliente", fila.head[0].nome, "atendido!")
      print("Valor total das compras:", total, "R$")
      fila.pop()

caixa = Atendimento()
fila = Fila()
c1 = Cliente("Júnior")
c2 = Cliente("Rebeca")
caixa.inserirCliente(fila, c1)
caixa.inserirCliente(fila, c2)
c1.realizarCompra(4.50)
c1.realizarCompra(3.50)
c1.realizarCompra(7)
c2.realizarCompra(6.50)
c2.realizarCompra(5)
c2.realizarCompra(8)
caixa.atenderCliente(fila)
caixa.atenderCliente(fila)
