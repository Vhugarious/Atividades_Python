print("Sorte Fibonacci")
n = int(input('Digite um valor: '))
a = 0
b = 0

while b < n:
  b = b + a
  a = b - a
  if a == 0:
    b += 1

if n == b:
  print('Ação bem sucedida!')
else:
  print('A ação falhou!')