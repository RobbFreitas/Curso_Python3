sequencia = int(input('Numero: '))
atual = 1
antecessor = 1
for i in range (2, sequencia):
    sucessor = antecessor
    antecessor = sucessor
    atual = antecessor + sucessor
print('resposta {}'.format(atual))
