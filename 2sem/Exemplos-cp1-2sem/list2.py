# Peça para o usuário digitar uma lista de 20 números reais. Ao 
# final exiba a média dos valores digitados contidos na lista.

numeros = []
num = media = 0.0
soma = 0.0
for i in range(0,20,1) :
    print("Digite um número real")
    num = float(input())
    numeros.append(num)
for i in numeros :
    soma += i
media = soma / len(numeros)
print(f"Média dos valores é {media}")
