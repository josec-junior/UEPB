class Cliente:

  def __init__(self, nome, cpf, numeroConta):
    self.nome = nome
    self.cpf = cpf
    self.numeroConta = numeroConta

  def __str__(self):
    output = "Nome: " + str(self.nome) + ", CPF: " + str(self.cpf) + ", Número da Conta: " + str(self.numeroConta)
    return output

class Queue:

  def __init__(self):
    self.head = []

  def push(self):
    self.head.append()

  def pop(self):
    return self.head.pop(0)

  def isEmpty(self):
    return len(self.head) == 0

  def __str__(self):
    output = ""
    if(not self.head.isEmpty()):
      tam = len(self.head)
      for i in range(tam):
        output += str(self.head[i])
        if (i < tam - 1):
          output += "→"
    else:
      output = "Fila vazia!"
    return output

class Banco:

  def __init__(self):
    pass

  def inserirCliente(self, fila, cliente):
    fila.push(cliente)

  def atenderCliente(self, fila):
    fila.pop()

fila = Queue()
atendimento = Banco()
c1 = Cliente("Júnior", "136", "003")
c2 = Cliente("Miguel", "101", "006")
c3 = Cliente("Johnny", "198", "004")
print(c1)
print(c2)
print(c3)
