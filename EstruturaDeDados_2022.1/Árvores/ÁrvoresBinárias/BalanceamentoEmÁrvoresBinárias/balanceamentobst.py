class BSTNode:

  def __init__(self, value = None):
    self.data = value
    self.left = None
    self.right = None

  def insert(self, value):
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

  def imprimir_pre_ordem(self):
    if self.data:
      print(self.data, end = " ")
      if self.left:
        self.left.imprimir_pre_ordem()
      if self.right:
        self.right.imprimir_pre_ordem()
  
  def imprimir_ordem_central(self):
    if self.data:
      if self.left:
        self.left.imprimir_ordem_central()
      print(self.data, end = " ")
      if self.right:
        self.right.imprimir_ordem_central()

  def imprimir_pos_ordem(self):
    if self.data:
      if self.left:
        self.left.imprimir_pos_ordem()
      if self.right:
        self.right.imprimir_pos_ordem()
      print(self.data, end = " ")

  def tamanho(self):
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

  def soma(self):
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

  def altura(self):
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

  def balanceada(self): #Método para verificar se a árvore está balanceada
    if not self.data:
      return True
    else:
      if self.left:
        esqBalanceada = self.left.balanceada()
        esqAltura = self.left.altura()
      else:
        esqBalanceada = True
        esqAltura = -1
      if self.right:
        dirBalanceada = self.right.balanceada()
        dirAltura = self.right.altura()
      else:
        dirBalanceada = True
        dirAltura = -1
      calculoBalanceada = abs(esqAltura - dirAltura) <= 1
      return esqBalanceada and dirBalanceada and calculoBalanceada

  def gerar_lista(self, lista): #Método para gerar uma estrutura auxiliar (lista) onde será guardado os elementos da árvore de forma ordenada.
    if self.data:
      if self.left:
        self.left.gerar_lista(lista)
      lista.append(self.data)
      if self.right:
        self.right.gerar_lista(lista)

  def destruir(self): #Método para remover a árvore da memória.
    if self.data:
      if self.left:
        self.left.destruir()
      if self.right:
        self.right.destruir()
      del self.data
      del self

  def gerar_arvore(self, lista, inicio, fim): #Método para reconstruir a árvore com os elementos da estrutura auxiliar.
    meio = (inicio + fim) // 2
    self.data = lista[meio]
    if inicio <= meio - 1:
      self.left = BSTNode()
      self.left.gerar_arvore(lista, inicio, meio - 1)
    else:
      self.left = None
    if meio + 1 <= fim:
      self.right = BSTNode()
      self.right.gerar_arvore(lista, meio + 1, fim)
    else:
      self.right = None

  def balanceamento_estatico(self): #Método para realizar o Balanceamento Estático.
    if not self.balanceada():
      l = []
      self.gerar_lista(l)
      self.destruir()
      self = BSTNode()
      self.gerar_arvore(l, 0, len(l) - 1)
    return self


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
print("Pré-ordem: ", end = "")
root.imprimir_pre_ordem()
print("\nOrdem central: ", end = "")
root.imprimir_ordem_central()
print("\nPós-ordem: ", end = "")
root.imprimir_pos_ordem()
print("\nTamanho:", root.tamanho())
print("Soma:", root.soma())
print("Altura da árvore:", root.altura())
print("Balanceada: ", root.balanceada())
root = root.balanceamento_estatico()
print()
print("Após o Balanceamento Estático...")
print()
print("Pré-ordem: ", end = "")
root.imprimir_pre_ordem()
print("\nOrdem central: ", end = "")
root.imprimir_ordem_central()
print("\nPós-ordem: ", end = "")
root.imprimir_pos_ordem()
print("\nTamanho:", root.tamanho())
print("Soma:", root.soma())
print("Altura da árvore:", root.altura())
print("Balanceada: ", root.balanceada())