soma = 0 
valor_n = int(input('digite o valor: '))
for i in range (1, valor_n + 1):
    calculo = (2*i + 5 *i) ** 2
    print(calculo)
    soma += calculo
print(soma)
