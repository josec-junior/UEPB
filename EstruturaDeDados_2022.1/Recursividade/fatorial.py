def fatorial(n):
  if n == 0:
    return 1
  else:
    return n * fatorial(n - 1)


n = int(input("Digite um número: "))
fat = fatorial(n)
print("O fatorial de", n, "é", fat)
