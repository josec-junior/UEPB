class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

class LinkedList:

  def __init__(self):
    self.head = None
    self._size = 0
  
  def append(self, value):
    if self.head:
      #Inserção quando a lista possuir um ou mais elementos.
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Node(value)
    else:
      #Primeira Inserção, quando a lista está vazia.
      self.head = Node(value)
    self._size += 1

  def __len__(self):
    #Retorna o tamanho da lista.
    return self._size

  def __getitem__(self, index): #Método para acessar o elemento.
    if self.head:
      aux = self.head
      for i in range(index):
        if aux.next:
          aux = aux.next
        else:
          raise IndexError("Índice fora da lista!")
      return aux.data
    else:
      raise IndexError("Lista vazia!")

  def __setitem__(self, index, value): #Método para alterar o elemento.
    if self.head:
      aux = self.head
      for i in range(index):
        if aux.next:
          aux = aux.next
        else:
          raise IndexError("Índice fora da lista!")
      aux.data = value
    else:
      raise IndexError("Lista vazia!")

  def __str__(self): #Método toString()
    output = ""
    if self.head:
      aux = self.head
      output += "["
      while (aux):
        output += str(aux.data)
        if (aux.next):
          output += ", "
        aux = aux.next
      output += "]"
    else:
      output = "[]"
    return output

lista = LinkedList()
lista.append(2)
lista.append(3)
lista.append(4)
print(lista)
