#Fórmula inicial área da circunferência
#!/user/local/bin/python3
from math import pi


def circulo (raio):
  return pi * float(raio )**2 


if __name__ == '__main__':
  raio = float(input('Informe o valor do raio:  '))
  area = circulo(raio)
  print(f'A área do círculo é {area}')
