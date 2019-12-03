palavra = 'paralelepípedo'
for letra in palavra:
  print(letra, end = ', ')
print('\nFim')


aprovados = ['Rafaela', 'Pedro', 'Renato', 'Maria']
for nome in aprovados:
  print(nome, end = '\n')


for posicao, nome in enumerate(aprovados):
  print(f'{posicao + 1} -', nome)
print('\nFim')


dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta',
                         'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
  print(f'Hoje é {dia}')