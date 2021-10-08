print("Votação dia live.\n"
      "Por favor, digite quantos votos cada dia recebeu.")

segunda = int(input("Segunda-feira: "))
terca = int(input("Terça-feira: "))
quarta = int(input("Quarta-feira: "))
quinta = int(input("Quinta-feira: "))
sexta = int(input("Sexta-feira: "))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta:
    print("Segunda-feira foi o dia mais votado.")
elif terca > segunda and terca > quarta and terca > quinta and terca > sexta:
    print("Terça-feira foi o dia mais votado.")
elif quarta > segunda and quarta > terca and quarta > quinta and quarta > sexta:
    print("Quarta-feira foi o dia mais votado.")
elif quinta > segunda and quinta > terca and quinta > quarta and quinta > sexta:
    print("Quinta-feira foi o dia mais votado.")
elif sexta > segunda and sexta > terca and sexta > quarta and sexta > quinta:
    print("Sexta-feira foi o dia mais votado.")
else:
    print("Houve empate entre dois ou mais dias.")