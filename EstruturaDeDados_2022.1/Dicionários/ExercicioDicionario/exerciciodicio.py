arquivo = open("scorpions.txt", "r")
lista = arquivo.read().lower().split()

ocorrencias = {}

for palavra in lista:
  ocorrencias[palavra] = ocorrencias.get(palavra, 0) + 1

max_ocorrencias = None
max_palavra = None

for k, v in ocorrencias.items():
  if max_ocorrencias == None or v > max_ocorrencias:
    max_ocorrencias = v
    max_palavra = k
print("A palavra que aparece mais vezes é", max_palavra, "com", max_ocorrencias, "ocorrências.")

print()

listatmp = sorted([(v, k) for k,v in ocorrencias.items()], reverse = True)
num_palavras = 10
for i in range(num_palavras):
  print(listatmp[i][1], "-", listatmp[i][0])