lista_impar = []
ls_nota_impar = []
count_impar = 1
lista_par = []
ls_nota_par = []
count_par = 2

print("Escola JoWell Sant'ana\n"
      "\nDigite as notas dos alunos IMPARES")

for aluno_impar in range(1,10,2):
    lista_impar.append(aluno_impar)

for aluno_par in range(2, 11, 2):
    lista_par.append(aluno_par)



while count_impar in lista_impar:
    nota = float(input("Nota do aluno número {}: ".format(count_impar)))
    while nota > 10 or nota < 0:
        nota = float(input("Valor incorreto.\n"
                         "Digite novamente a nota do aluno número {}: ".format(count_impar)))
    ls_nota_impar.append(nota)
    count_impar += 2

media_impar = (sum(ls_nota_impar) / 5)

print("A nota média dos alunos pares foi: {}".format(media_impar))


print("\nAgora, digite a nota dos alunos PARES")

while count_par in lista_par:
    nota = float(input("Nota do aluno número {}: ".format(count_par)))
    while nota > 10 or nota < 0:
        nota = float(input("Valor incorreto.\n"
                         "Digite novamente a nota do aluno número {}: ".format(count_par)))
    ls_nota_par.append(nota)
    count_par += 2

media_par = (sum(ls_nota_par) / 5)

print("A nota média dos alunos pares foi: {}".format(media_par))

if media_impar > media_par:
    print("Os alunos de números impares tiraram a maior nota!")

elif media_par > media_impar:
    print("Os alunos de números pares tiraram a maior nota!")

else:
    print("Houve empate entre as turmas.")

