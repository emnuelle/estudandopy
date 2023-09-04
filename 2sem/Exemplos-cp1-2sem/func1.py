# Peça para o usuário digitar dois números inteiros. Exiba ao 
# final o resto da divisão (crie uma função com retorno).

def resto(n1,n2):
    rs1 = n1 // n2
    rs2 = n2 * rs1
    rs3 = n1- rs2
    return rs3

print("Digite dois números inteiros:")
num1 = int(input())
num2 = int(input())

resultado = resto(num1,num2)

print(f"Resto da divisão: {resultado}")