class Stack:

  def __init__(self):
    self.head = []

  def push(self, value):
    self.head.append(value)

  def pop(self):
    return self.head.pop()

def inverter(string):
  palavra = Stack()
  tam = len(string)
  for i in range(tam):
    palavra.push(string[i])
  invertida = ""
  for i in range(tam):
    invertida += palavra.pop()
  return invertida

str = input("Digite alguma palavra: ")
invert = inverter(str)
print(str, "ao contrário fica", invert)
