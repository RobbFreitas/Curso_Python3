#Fórmula inicial área da circunferência
#!/user/local/bin/python3
from math import pi
if __name__ == '__main__':
  raio = float(input('Informe o valor do raio: '))
  calculo = pi * (raio **2 )
print(f'O valor da área é {calculo}m')
