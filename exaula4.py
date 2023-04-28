# Digite numeros de QI de essoa diversas, o user deve continuar digitando até digitar 0  (utilizar o break p/ interromper). Fazer contagem dos genios (quem tem QI superior aou igual a 140 e ignorar quem tem menos), apenas números ineteiros são permitidos

cont = 0
while True:
    try : 
        print("Digite o valor de QI")
        print("Ou 0 para encerrar")
        qi = int(input())
        if qi == 0 :
            break
        if qi < 140 :
            continue
        cont += 1
    except ValueError:
        print("Erro! Apenas números inteiros.")
print(f"Quantidade de gênios é {cont}")

