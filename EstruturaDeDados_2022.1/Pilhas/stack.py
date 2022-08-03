class Stack:

  def __init__(self):
    self.head = [] #Topo da pilha/último elemento

  def push(self, value):
    self.head.append(value) #Insere um elemento na pilha

  def pop(self):
    return self.head.pop() #Remove o elemento que está no topo da pilha/último elemento adicionado
  
  def isEmpty(self):
    return len(self.head) == 0

  def __str__(self):
    output = ""
    if (self.head):
      tamanho = len(self.head) - 1
      for i in range(tamanho, -1, -1):
        output += "[" + str(self.head[i]) + "]\n"
    else:
      output = "[]"
    return output

pilha = Stack()
pilha.push(1)
pilha.push(4.5)
pilha.push("Júnior")
pilha.push("Estrutura de Dados")
pilha.push(30.44)
print(pilha)
