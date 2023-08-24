# Peça para o usuário digitar um número inteiro qualquer. 
# Exiba a raiz quadrada (crie uma função com retorno).

def raiz(n1):
    rs = n1 ** (1/2)
    return int(rs)

print("Digite um número inteiro:")
num1 = int(input())
resultado = raiz(num1)

print(f"Raiz quadrada: {resultado}")