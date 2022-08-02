class Queue:

  def __init__(self):
    self.head = []

  def push(self, value):
    self.head.append(value)

  def pop(self):
    return self.head.pop(0)

  def __str__(self):
    output = ""
    if (self.isEmpty()):
      output = "[]"
    else:
      for i in range(len(self.head)):
        output += "[" + str(self.head[i]) + "] → "
    return output

  def isEmpty(self):
    return len(self.head) == 0

fila = Queue()
fila.push("João")
fila.push("Maria")
fila.push("Álvaro")
fila.push("Ana")
print(fila)
