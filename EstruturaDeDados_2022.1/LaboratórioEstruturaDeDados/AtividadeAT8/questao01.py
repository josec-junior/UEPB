class BSTNode:
  
  def __init__(self, value = None): #Método construtor, com parâmetro value definido como None por padrão.
    self.data = value #Nó central.
    self.left = None #Nó filho da esquerda.
    self.right = None #Nó filho da direita.
  
  def insert(self, value): #Método para inserir elemento no próximo nó da árvore disponível.
    if not self.data:
      self.data = value
    elif value < self.data:
      if self.left:
        self.left.insert(value)
      else:
        self.left = BSTNode(value)
    elif value > self.data:
      if self.right:
        self.right.insert(value)
      else:
        self.right = BSTNode(value)

  def imprimir_pre_ordem(self): #Método para percorrer a árvore e imprimir os seus nós, na forma de pré-ordem.
    if self.data:
      print(self.data, end = " ")
      if self.left:
        self.left.imprimir_pre_ordem()
      if self.right:
        self.right.imprimir_pre_ordem()

  def imprimir_ordem_central(self): #Método para percorrer a árvore e imprimir os seus nós, na forma de ordem central.
    if self.data:
      if self.left:
        self.left.imprimir_ordem_central()
      print(self.data, end = " ")
      if self.right:
        self.right.imprimir_ordem_central()

  def imprimir_pos_ordem(self): #Método para percorrer a árvore e imprimir os seus nós, na forma de pós-ordem.
    if self.data:
      if self.left:
        self.left.imprimir_pos_ordem()
      if self.right:
        self.right.imprimir_pos_ordem()
      print(self.data, end = " ")

  def tamanho(self): #Método para retornar o tamanho da árvore.
    if not self.data:
      return 0
    else:
      if self.left:
        esq = self.left.tamanho()
      else:
        esq = 0
      if self.right:
        dir = self.right.tamanho()
      else:
        dir = 0
      return esq + dir + 1

  def soma(self): #Método para retornar a soma dos elementos da árvore.
    if not self.data:
      return 0
    else:
      if self.left:
        esq = self.left.soma()
      else:
        esq = 0
      if self.right:
        dir = self.right.soma()
      else:
        dir = 0
      return esq + dir + self.data

  def altura(self): #Método para retornar a altura da árvore.
    if not self.data:
      return -1
    else:
      if self.left:
        alturaEsq = self.left.altura()
      else:
        alturaEsq = -1
      if self.right:
        alturaDir = self.right.altura()
      else:
        alturaDir = -1
      if alturaEsq > alturaDir:
        return alturaEsq + 1
      else:
        return alturaDir + 1

  def apresentarPaiFilho(self): #Método para apresentar os nós que possuem pai e filhos (pelo menos um filho). 
    if self.data:
      if self.left:
        if self.left.left or self.left.right:
          print("Nó:", self.left.data)
        self.left.apresentarPaiFilho()
      if self.right:
        if self.right.left or self.right.right:
          print("Nó:", self.right.data)
        self.right.apresentarPaiFilho()


root = BSTNode()
root.insert(20)
root.insert(13)
root.insert(7)
root.insert(42)
root.insert(25)
root.insert(3)
root.insert(18)
root.insert(37)
root.insert(22)
root.insert(10)
root.apresentarPaiFilho()
