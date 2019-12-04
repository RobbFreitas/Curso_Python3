from random import randint


def sortear_dado(numero):
  return randint (1, 6)


for i in range (1, 7):
  if i %2 != 0:
    continue
  elif i %2 == 0 and i == sortear_dado(randint):
    print(f'Acertou! o número era: {i}')
    break
else:
  print(f'Não acertou! O número era: {sortear_dado(randint)}')
