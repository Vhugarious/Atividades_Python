print("PROJETO HEALTH TRACK")
altura = float(input("Por favor, informe sua altura (Exemplo: 1.80): "))
peso = float(input("Agora, forme seu peso (Exemplo: 80.5): "))
imc = peso / (altura **2)

if imc <16:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Baixo peso Grau III.".format(imc))
elif imc >=16 and imc <=16.99:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Baixo peso Grau II.".format(imc))
elif imc >=17 and imc <=18.49:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Baixo peso Grau I.".format(imc))
elif imc >=18.5 and imc <=24.49:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Peso ideal.".format(imc))
elif imc >=25 and imc <=29.99:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Sobrepeso.".format(imc))
elif imc >=30 and imc <=34.99:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Obesidade Grau I.".format(imc))
elif imc >=35 and imc <=39.99:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Obesidade Grau II.".format(imc))
else:
    print("O seu IMC é de {0:.2f}, e você se encontra na categoria de Obesidade Grau III.".format(imc))