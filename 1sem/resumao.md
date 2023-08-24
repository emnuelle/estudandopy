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
    *input()* - (comando) serve para permitir que o usuário entre com algum valor (via terminal)
    > O valor informado pelo usuário com o comando "input()" deve ser atribuido a uma variavel
    > Por padrão, todo valor digitado no terinal, é uma string (cating pode ser necessério em alguns casos) 
    > exemplos de progroma com o comando no arquivo "exinput.py" e "exinputii.py"
    
##   Operadores aritiméticos:
    > "+": adição      
    > "-": subtração
    > "*": multiplicação
    > "/": divisão 
    nota "//" divide em números inteiros
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

## Casting
Algumas vez será necessário especificar um tipo para alguma variável, no python podemos utilizar as funções abaixo para realizar esta conversão de valores;

    > "int()" converte um valor para un número inteiro
    > "float()" converte um valor para um número real (com casas decimais)
    > "str()" converte o valor para uma string
    nota: os valores serão convertidos se isso for possível!
ex:

        x = 10.0  
        print(type(x), x)
        x = int(x)
        print(type(x), x)
        x = str(x)
        print(type(x), x)
        x = float(x)
        print(type(x), x)

      Rode o programa e veja o resultado ;)

## Módulo math
Contém várias funções matemáticas para o uso , pra utiliza-las primeiramente temos que importa-las no início do código, usando **import**. 

        > "math.sqrt(x)" - calcula a raiz quadrada, ex:
            
            import math
            num = 81 
            print(math.sqrt(num))

        Rode o programa e veja o resultado ;)
        > math.ceil(x) - arredonda o número x para cima
        > math.floor(x) - arredonda o número x para baixo 
        > math.pi - retorna o valor de pi
        > math.pow(x,y) - eleva valor x por y


## Notas aula 280423
### interrrompendo o fluxo de execução (boatos que não é uma boa prática)
O comando *break* interrompe por completo o bloco de comando e o comando *continue* pula para próxima iteração
> exs nos arquivos exaulax.py!

### Tratamento de erros


## Notas aula 120523
-- Correção de exs da aula anterior (depois colocar nessa pasta {ver os slides no teams})
### listas 
[LIST]: um objeto que é utilizadopara armazenar múltiplos valores em um variavél 
crims um list e inicializamos seus valores usamos o colchetes []

> ex 
  frutas = [uva, maçã, tomate] |
  print(frutas) |
  *iria aparecer todas asa frutas*

* Ordena os seus valores em indices(começando em 0), não possui um tamo fixo (muda de acordo com os elemetos que possui)
* Os valores podem ser duplicados, para descobrir o tamanho de list utilizamos a função len() e para adicionar novos valores utilizamos a função append()
*Mais exemplos nos slides*

