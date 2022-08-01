def fibonacci(pos):
  if pos == 1 or pos == 2:
    return 1
  else:
    return fibonacci(pos - 1) + fibonacci(pos - 2)


posicao = int(input("Digite a posição na sequência de Fibonacci que você deseja visualizar o número que está lá: "))
num = fibonacci(posicao)
print("O número que está nessa posição é o", num)
