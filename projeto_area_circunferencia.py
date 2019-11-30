# Fórmula inicial área da circunferência
#!/user/local/bin/python3
from math import pi


def circulo(raio):
    return pi * float(raio)**2


def help ():
   print('É necessário informar o raio do círculo\nSintaxe: {} <raio>'.format(raio))


if __name__ == '__main__':
    raio = float(input('Informe o valor do raio:  '))
    if raio < 2 or raio == 0:
      help()
    else:
      area = circulo(raio)
      print('O tamanho da área do círculo é {:.2f}m'.format(area))
