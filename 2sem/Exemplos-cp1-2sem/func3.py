# Peça para o usuário digitar vários números inteiros, deve continuar 
# digitando até que digite o valor 0 para encerrar. Exiba para cada número 
# que ele digitar se o número é par ou ímpar (crie uma função sem retorno).

def par_impar(n1):
    rs = n1 % 2
    if rs == 0:
        print("Este número é PAR")
    else: 
        print("Este número é ÍMPAR")

num = 1
while(num != 0):
    print("Digite um número inteiro (ou zero)")
    num = int(input())
    par_impar(num)
print("Fim de programa.")
