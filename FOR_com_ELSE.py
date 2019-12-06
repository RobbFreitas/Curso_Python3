PALAVRAS_PROIBIDAS = ('futebol', 'religião', 'política')
textos = [
  'João gosta de futebol e política',
  'A praia foi divertida',
]

for texto in textos:
  found = False # Se nenhuma palavra for encontrada esse valor será falso
  for palavra in texto.lower().split():
    if palavra in PALAVRAS_PROIBIDAS:
      print('Texto possui ao menos uma palavra proibida: ', palavra)
      found = True # Encontrou a palavra proibida
      break

  if not found:
    print('Texto autorizado', texto
    )
