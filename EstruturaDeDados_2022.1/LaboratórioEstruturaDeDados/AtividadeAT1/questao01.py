def cacularKMPercorridos(kmPercorridos, dias):
  total = (60 * dias) + (kmPercorridos * 0.15)
  return total

km = float(input("Digite a quantidade de KMs Percorridos: "))
dias = int(input("Digite a quantidade de dias que o carro foi alugado: "))
pagamento = cacularKMPercorridos(km, dias)
print("Você rodou", km, "KM e alugou o carro por", dias, "dias, o total a pagar é", pagamento, "R$")
