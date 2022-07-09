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

  def __getitem__(self, index):
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

  def __setitem__(self, index, value):
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

  def __str__(self):
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

  def removeFirstElement(self): #Questão 01
    if (self.head):
      if (self.head.next):
        aux = self.head
        self.head = self.head.next
        aux.next = None
        del (aux)
      else:
        del (self.head)
        self.head = None
    else:
      raise IndexError("Lista vazia!")

  def removeLastElement(self): #Questão 02
    if (self.head):
      aux = self.head
      ant = None
      while (aux.next):
        ant = aux
        aux = aux.next
      if (ant == None):
        del (aux)
        self.head = None
      else:
        ant.next = None
        del (aux)
    else:
      raise IndexError("Lista vazia!")

  def printOnlyNumberPairs(self): #Questão 03
    if (self.head):
      output = "["
      aux = self.head
      while (aux):
        if (aux.data % 2 == 0):
          output += str(aux.data)
          if (aux.next):
            output += ", "
        aux = aux.next
      output += "]"
      print(output)
    else:
      raise IndexError("Lista vazia!")

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)
l.append(8)
l.printOnlyNumberPairs()
