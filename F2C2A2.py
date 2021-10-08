print("Bônus do cliente")

plano = int(input("Por favor, escolha a opção do seu plano:\n"
                  "1-Basic\n"
                  "2-Silver\n"
                  "3-Gold\n"
                  "4-Platinum\n"
                  "Opção: "))

if plano == 1:
    faturamento = float(input("Agora insira o seu faturamento (Ex: 12.25): "))
    bonus = float(faturamento) * 0.3
    print("O Bônus a ser pago é de ${0:.2f}.".format(bonus))
elif plano == 2:
    faturamento = float(input("Agora insira o seu faturamento (Ex: 12.25): "))
    bonus = faturamento * 0.2
    print("O Bônus a ser pago é de ${0:.2f}.".format(bonus))
elif plano == 3:
    faturamento = float(input("Agora insira o seu faturamento (Ex: 12.25): "))
    bonus = faturamento * 0.1
    print("O Bônus a ser pago é de ${0:.2f}.".format(bonus))
elif plano == 4:
    faturamento = float(input("Agora insira o seu faturamento (Ex: 12.25): "))
    bonus = faturamento * 0.05
    print("O Bônus a ser pago é de ${0:.2f}.".format(bonus))
else:
    print("Opção errada. Por favor, escolha uma das opções acima.")
