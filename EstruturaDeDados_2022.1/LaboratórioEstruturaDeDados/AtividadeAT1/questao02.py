def inserirNaLista(lista, i):
  if (i < 4):
    n = int(input("Digite um número: "))
    lista.append(n)
    return inserirNaLista(lista, i + 1)

lista = []
i = 0
inserirNaLista(lista, i)
print(lista)
