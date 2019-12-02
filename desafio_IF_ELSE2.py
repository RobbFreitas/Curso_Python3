def faixa_etaria(idade):
  if 0 <= idade < 18:
    return 'Menor de idade'
  elif idade in range (18, 65):
      return 'Adulto'
  elif idade in range (65,100):
      return 'Idoso'
  elif idade >= 100:
      return 'Centenária'
  else:
      return 'Idade inválida'
    

if __name__ == '__main__':
  idade = float(input('Informe idade: '))
  print(faixa_etaria(idade))