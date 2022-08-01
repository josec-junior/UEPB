def imprimir(vet, pos, tam):
  if pos < tam:
    print(vet[pos], end = " ")
    imprimir(vet, pos + 1, tam)

tamanho = int(input("Digite o tamanho do vetor: "))
vetor = []
for i in range(tamanho):
  vetor.append(int(input("Digite um número: ")))
imprimir(vetor, 0, tamanho)
