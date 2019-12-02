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
    

print(10 * '*')
print('Faixa etária\nMenor de idade\nAdulto\nIdoso\nCentenária\nIdade inválida')
print(10 * '*')


if __name__ == '__main__':
  idade = float(input('Informe a idade: '))
  print(faixa_etaria(idade))
