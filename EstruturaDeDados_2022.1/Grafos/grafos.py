class Aresta:

  def __init__(self, value, dest):
    self.value = value
    self.dest = dest
    self.next = None

class Vertice:

  def __init__(self, label):
    self.label = label
    self.next = None
    self.adj = None
    self.mark = False

  def profundidade(self):
    if self:
      print(self.label, end = " ")
      self.mark = True
      aux = self.adj
      while aux:
        if not aux.dest.mark:
          aux.dest.profundidade()
        aux = aux.next

class Grafo:

  def __init__(self):
    self.head = None
  
  def insert_vertice(self, label):
    if not self.head:
      self.head = Vertice(label)
    else:
      aux = self.head
      while aux.next:
        aux = aux.next
      aux.next = Vertice(label)
  
  def busca_vertice(self, label):
    aux = self.head
    while aux.next and aux.label != label:
      aux = aux.next
    return aux

  def insert_aresta(self, value, ori, dest):
    aux_ori = self.busca_vertice(ori)
    aux_dest = self.busca_vertice(dest)
    if not aux_ori.adj:
      aux_ori.adj = Aresta(value, aux_dest)
    else:
      aux_ares = aux_ori.adj
      while aux_ares.next:
        aux_ares = aux_ares.next
      aux_ares.next = Aresta(value, aux_dest)

g = Grafo()
g.insert_vertice("A")
g.insert_vertice("B")
g.insert_vertice("C")
g.insert_vertice("D")
g.insert_aresta(5, "A", "B")
g.insert_aresta(4, "A", "C")
g.insert_aresta(7, "B", "D")
g.insert_aresta(3, "C", "D")
print("Profundidade:", end = " ")
g.head.profundidade()