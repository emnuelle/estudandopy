#paia
#Foi mais ou menos

# Monte um programa de cadastro de usuários. Devem
# ser cadastrados as informações de nome, login e senha.
# Para cada cadastro crie um arquivo (o nome do arquivo
# deve ser composto do login). O usuário deve continuar
# cadastrando usuários enquanto quiser (defina uma
# condição para parar).

# Função de cadastro
def cadastro():
    try:
        print("****************")
        print("Área de cadastro")
        print("****************")

        print("Digite o nome:")
        nome = input()
        criando_cadastro = open(f'd:/realizando-atividades/{nome}.txt', 'x', encoding='utf-8')
        criando_cadastro.close()

        print("Digite o usuário:")
        nome_usuario = input()
        adc_user = open(f'd:/realizando-atividades/{nome}.txt', 'w', encoding='utf-8')
        adc_user.write(f"Nome de usuário: {nome_usuario}")
        adc_user.close()

        print("Digite a senha:")
        senha = input()
        adc_senha = open(f'd:/realizando-atividades/{nome}.txt', 'a', encoding='utf-8')
        adc_senha.append(f"Senha: {senha}")
        adc_senha.close()

        #Testando aq
        teste = open(f'd:/realizando-atividades/{nome}.txt', 't', encoding='utf-8')
        print(teste.read())
        teste.close()
    except FileNotFoundError:
        print("Caminho e /ou arquivo inxistente")

# Progama
print(cadastro())




