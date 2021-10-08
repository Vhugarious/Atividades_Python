print("PROJETO HEALTH TRACK")
idade = int(input("Por favor, insira sua idade: "))

if not (idade >= 3 and idade <= 7):

    bpm = int(input("Agora, insira seus batimentos: "))

    if idade <= 2 and bpm >= 120 and bpm <= 140:
        print("Os seus batimentos encontram-se dentro da faixa adequada.")
    elif idade <= 2 and bpm > 140:
        print("Os seus batimentos encontram-se acima da faixa adequada.")
    elif idade <= 2 and bpm < 120:
        print("Os seus batimentos encontram-se abaixo da faixa adequada.")

    elif idade >= 8 and idade <= 17 and bpm >= 80 and bpm <= 100:
        print("Os seus batimentos encontram-se dentro da faixa adequada.")
    elif idade >= 8 and idade <= 17 and bpm > 100:
        print("Os seus batimentos encontram-se acima da faixa adequada.")
    elif idade >= 8 and idade <= 17 and bpm < 80:
        print("Os seus batimentos encontram-se abaixo da faixa adequada.")

    elif idade >= 18 and idade <= 65 and bpm >= 70 and bpm <= 80:
        print("Os seus batimentos encontram-se dentro da faixa adequada.")
    elif idade >= 18 and idade <= 65 and bpm > 80:
        print("Os seus batimentos encontram-se acima da faixa adequada.")
    elif idade >= 18 and idade <= 65 and bpm < 70:
        print("Os seus batimentos encontram-se abaixo da faixa adequada.")

    elif idade > 65 and bpm >= 50 and bpm <= 60:
        print("Os seus batimentos encontram-se dentro da faixa adequada.")
    elif idade > 65 and bpm > 60:
        print("Os seus batimentos encontram-se acima da faixa adequada.")
    elif idade > 65 and bpm < 50:
        print("Os seus batimentos encontram-se abaixo da faixa adequada.")

elif idade >= 3 and idade <= 7:
    print("Não trabalhamos com a faixa etária de 3 a 7 anos.")

