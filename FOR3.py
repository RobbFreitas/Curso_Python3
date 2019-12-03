produto = {'nome': 'Caneta Chic', 'Preço': 14.99,
                  'Importada': True, 'estoque': 793}
for chave in produto:
  print(chave)


for valor in produto.values():
  print(valor)


for chave, valor in produto.items():
  print(f'{chave} = {valor}')