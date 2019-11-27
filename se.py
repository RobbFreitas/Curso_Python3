num = int(input('Numeros ímpares até aqui: '))
lista = []
for i in range(0,num+1):
    if i %2 != 0:
        lista.append(i)
print(lista, len(lista))
    
