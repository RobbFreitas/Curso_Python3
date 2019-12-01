# Fórmula inicial área da circunferência
#!/user/local/bin/python3
from math import pi
import sys 


class TerminalColor:
  ERRO = '\033[91m'
  NORMAL = '\033[0m'


def circulo(raio):
    return pi * float(raio)**2


def help():
   print(TerminalColor.ERRO + 
            f'É necessário informar o raio do círculo Sintaxe: {raio} <raio>'
            + TerminalColor.NORMAL)


if __name__ == '__main__':
    raio = float(input('Informe o valor do raio (apenas valor numérico):  '))
    if raio < 2 or raio == 0:
      help()
    else:
      area = circulo(raio)
      print('O tamanho da área do círculo é {:.2f}m'.format(area))
