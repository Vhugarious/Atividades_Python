print("VOTAÇÃO DE CONSOLE\n"
      "Por favor, digite a opção correspondente com o voto de cada funcionário:\n"
      "1- Playstation\n"
      "2- Xbox\n"
      "3- Nintendo\n")
func_1 = int(input("Funcionário 1: "))
func_2 = int(input("Funcionário 2: "))
func_3 = int(input("Funcionário 3: "))
func_4 = int(input("Funcionário 4: "))
func_5 = int(input("Funcionário 5: "))

play = 0
xbox = 0
nint = 0

if func_1 ==1 or func_1 ==2 or func_1 ==3:
      if func_1 == 1:
            play = play + 1
      elif func_1 == 2:
            xbox = xbox + 1
      elif func_1 == 3:
            nint = nint + 1

if func_2 ==1 or func_2 ==2 or func_2 ==3:
      if func_2 == 1:
            play = play + 1
      elif func_2 == 2:
            xbox = xbox + 1
      elif func_2 == 3:
            nint = nint + 1

if func_3 ==1 or func_3 ==2 or func_3 ==3:
      if func_3 == 1:
            play = play + 1
      elif func_3 == 2:
            xbox = xbox + 1
      elif func_3 == 3:
            nint = nint + 1

if func_4 ==1 or func_4 ==2 or func_4 ==3:
      if func_4 == 1:
            play = play + 1
      elif func_4 == 2:
            xbox = xbox + 1
      elif func_4 == 3:
            nint = nint + 1

if func_5 ==1 or func_5 ==2 or func_5 ==3:
      if func_5 == 1:
            play = play + 1
      elif func_5 == 2:
            xbox = xbox + 1
      elif func_5 == 3:
            nint = nint + 1

      if play > xbox and play > nint:
            print("O console mais votado foi Playstation, com {} votos.".format(play))
      elif xbox > play and xbox > nint:
            print("O console mais votado foi Xbox, com {} votos.".format(xbox))
      elif nint > play and nint > xbox:
            print("O console mais votado foi Nintendo, com {} votos.".format(nint))
      else:
            print("Houve empate. Por favor, refaça a votação.")

else:
      print("Um ou mais votos foram inseridos de maneira inválida, tente novamente.")




