# corrigindo o cp II

import random

# Sorteio do usuário
sorteio = random.randint(1,5)

if sorteio == 1: nomefunc = "lero1"
elif sorteio == 2: nomefunc = "lero2"
elif sorteio == 3: nomefunc = "lero3"
elif sorteio == 4: nomefunc = "lero4"
else: nomefunc = "lero5"

# mensagem de boas vindas 
print(f"Bem-vindo a vinheria Agnelo.\n O funcionário {nomefunc} vai acompanhá-lo nesta compra.")

# Requisitando informações do cliete 
print("Informe seu nome: ")
nome = input()
print("Informe o CEP da sua residência:")
cep = input()
print("Informe o ano de seu nascimento: ")
anonasc = input()

# Verificando a maioriadade 
idade = 2023 - anonasc
if idade < 18 :
    print(f"{nome}, não é permitida a venda para menores de 18 anos!")
else : 
    print("Continua aqui")

# Variáveis para auxiliar nos cálculos 
subtotal = total = 0

# Preparândo a mensagem final
msgfinal = f"Dados da compra: \nAtendido por:{nomefunc} \nCliente:{nome} \nItens da compra: \tValor: \tQtde: \tSubtotal: \t"

# Repetindo a venda de vinhos
continua = "sim"
while continua.lower() == "sim":
    # exibindo opções de vinhos
    print(f"Escolha um dos vinhos da lista:\n (1) Vinho suave tinto\t R$15.00\n (2) Vinho seco tinto\t R$25.00\n (3)Vinho suave banco\t R$35.00\n (4) Vinho seco branco\t R$30,00\n (5) Suco de Uva\t R$40.00\n ")

    # Armazenando o vinho escolhidp e quantidade
    vinho = int(input())
    print("Em qual quantidade deseja adquirir este vinho?")
    qtde = int(input())
    match vinho :
        case 1 :
            subtotal = 15 * qtde
            msgfinal += f"Vinho suave Tinto\t R$15.00\t {qtde}\t R${subtotal:2f}\n"
        case 2 :
            subtotal = 25 * qtde
            msgfinal += f"Vinho seco Tinto\t R$25.00\t {qtde}\t R${subtotal:2f}\n"
        case 3 :
            subtotal = 35 * qtde
            msgfinal += f"Vinho suave branco\t R$35.00\t {qtde}\t R${subtotal:2f}\n"
        case 4 :
            subtotal = 30 * qtde
            msgfinal += f"Vinho seco branco\t R$35.00\t {qtde}\t R${subtotal:2f}\n"
        case 5 :
            subtotal = 40 * qtde
            msgfinal += f"Suco de uva\t R$40.00\t {qtde}\t R${subtotal:2f}\n"
        case _ :
            print("Por favor, escolha uam das opções da lista")
    total += subtotal 
    # total = total + subtotal


    # Continuando u não a compra
    print("Deseja continuar comprando?\n Responda Sim ou não.")
    continua = input

# exibindo informações finais 
print(msgfinal)