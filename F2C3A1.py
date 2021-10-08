print("PROJETO HEALTH TRACK - Consumo de calorias")
quantidade = int(input('Qual a quantidade de alimentos ingeridos: '))
alimento = []
count = 1
cal = 0
while c <= quantidade:
  alimento.append(input('Digite o nome do {}º alimento: '.format(c)))
  caloria = float(input('Digite a quantidade de calorias: '))
  cal += caloria
  count += 1

print("Você ingeriu {} alimento(s), dentre eles {}.\n"
      "Totalizando uma média de {} calorias.".format(quantidade, alimento, (int(cal/quantidade))))
