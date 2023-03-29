<h1> Python    

##  Variáveis: 
    um espaço reservado na memória do computador para armazenar um tipo de dado determinado  
  #### Regras:
    >   Não começar com número; 
    >   Não possuir caractere especial;
    >   Não ser uma palavra reservada;
    >   Deve ser a única a existir; 
    >   Não mudar seu tipo;
    >   Tentar no maximo indicar seu propósito atravez do nome. 
 
  #### Tipos básicos de dados python que podem ser usados para as variáveis:
    > int = "numeros inteiros"
    > float = "para numeros com casas decimais"
    > str = "para armazenar um ou mais caractere"
    > bool = "para valores lógicos (true or false)"

##   Funções e comandos:
    *print()* - (comando) Exibe uma mensagem para o usuário;
    > Todo texto exibido deve ficar entre aspas;
    > Números não ficam entre aspas (fiz isso no ex5.py mas sei que não seria o ideal);
    > Para separar texto e número, utilizar a vírgula;
    > Para pular as linhas utilize "\n" (dentro das aspas, onde quiser pular a linha)
    *type()* - (função) Retorna o tipo de dado do objeto passado como parâmetro, ex:

    
        num = 43
        print(type(num))
        num = 33.33
        print(type(num))
        num = "lero-lero"
        print(type(num))
        num = true
        print(type(num))
     

    Rode o programa e veja o resultado ;)
    
##   Operadores aritiméticos:
    > "+": adição      
    > "-": subtração
    > "*": multiplicação
    > "/": divisão
##   Operadores de atribuição:
Utilizamos para atribuir valores as variáveis

    > "=" : ex. x = 5
    representa: x = 5

    > "+=": ex. x += 5
    representa: x = x + 5

    > "-=": ex. x -= 5
    representa: x = x - 5

    > "*=": ex. x *= 5
    representa: x = x * 5

    > "/=": ex. x /= 5
    representa: x = x / 3

##   Atribuindo múltiplos valores:
O python permite que você realize múltiplas atribuições em uma única linha, ex:

      x, y, z = "Café", "Chá", "Leite"
      print(x)
      print(y)
      print(z)

     Rode o programa e veja o resultado ;)
Também da para atribuir um mesmo valor a múltiplas variáveis, ex;

      x = y = z = "Biscoito"
      print(x)
      print(y)
      print(z)
    
     Rode o programa e veja o resultado ;)

##   Expressão interativa:
Podemos utilizar os operadores de atribuição para realizar cálculos com os valores já presentes em uma variavél, ex:

       num = 10
       print(num)
       num += 5
       print(num)
       
      Rode o programa e veja o resultado ;)

Utilizando o operador e atribuição "+=" para concatenar strings, ex:

       frase = "O rato roeu"
       frase += "\na roupa do rei de Roma"
       print(frase)
      
      Rode o programa e veja o resultado ;)
  
