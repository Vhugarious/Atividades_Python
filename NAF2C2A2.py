print("Desconto de viagens")

categoria = int(input("Por favor, escolha a categoria dos assentos:\n"
                   "1- Econômica\n"
                   "2- Executiva\n"
                   "3- Primeira classe\n"
                   "Opção: "))

if categoria == 1 or categoria == 2 or categoria == 3:

    viajantes = int(input("Agora, digite a quantidade de viajantes: "))

    if viajantes >= 2:
        valor_bruto = float(input("Digite o valor do seu pacote: "))

        if categoria == 1:
            if viajantes == 2:
                valor_desc = valor_bruto * 0.03
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes
                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

            elif viajantes == 3:
                valor_desc = valor_bruto * 0.04
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes
                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

            elif viajantes >= 4:
                valor_desc = valor_bruto * 0.05
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes

                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

        elif categoria == 2:
            if viajantes == 2:
                valor_desc = valor_bruto * 0.05
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes
                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

            elif viajantes == 3:
                valor_desc = valor_bruto * 0.07
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes
                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

            elif viajantes >= 4:
                valor_desc = valor_bruto * 0.08
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes

                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

        elif categoria == 3:
            if viajantes == 2:
                valor_desc = valor_bruto * 0.1
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes
                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

            elif viajantes == 3:
                valor_desc = valor_bruto * 0.15
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes
                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))

            elif viajantes >= 4:
                valor_desc = valor_bruto * 0.20
                valor_liq = valor_bruto - valor_desc
                valor_div = valor_liq / viajantes

                print("Obrigado por viajar conosco!\n"
                      "O seu pacote no valor de ${0:.2f}, teve um desconto de ${1:.2f}, e saiu por ${2:.2f}. Valor a ser pago por viajante ${3:.2f}.".format(valor_bruto,valor_desc,valor_liq,valor_div))


    else:
        print("Promoção válida a partir de 2 viajantes. Tente novamente.")


else:
    print("Opção inválida. Tente novamente.")

