print("Projeto finance kids")
exchange = int(input("Quantas transações foram feitas? "))
valor = []
n = 1

while n <= exchange:
  valor.append(int(input('Digite o valor  da {}ª transação: '.format(n))))

  n += 1

sum(valor)

print("O valor total foi de ${0:.2f}.\n"
  "Sendo uma média de ${1:.2f} por transação.".format(float(sum(valor)),(sum(valor)/exchange)))