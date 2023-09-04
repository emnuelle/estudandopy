# Peça para o usuário digitar quatro números reais 
# diferentes. Exiba os números digitados em ordem decrescente com 3 
# casas decimais (crie uma função sem retorno).

def trihousedesc(n1):
    n1.sort(reverse = True)
    for i in n1 :
        print(f"{i:.3f}")

num = []

print("Digite 4 números reais")
for i in range(0,4,1):
    valor = float(input())
    num.append(valor)
trihousedesc(num)
