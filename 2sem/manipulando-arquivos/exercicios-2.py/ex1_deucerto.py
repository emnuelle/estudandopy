# Função de cadastro
def cadastro():
    try:
        print("****************")
        print("Área de cadastro")
        print("****************")

        print("Digite o nome:")
        nome = input()
        nome_arquivo = f'd:/realizando-atividades/{nome}.txt'
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
            print("Digite o usuário:")
            nome_usuario = input()
            arquivo.write(f"Nome de usuário: {nome_usuario}\n")

            print("Digite a senha:")
            senha = input()
            arquivo.write(f"Senha: {senha}\n")

        print("Cadastro concluído com sucesso!")

    except FileNotFoundError:
        print("Caminho e/ou arquivo inexistente")

# Programa
while True:
    cadastro()
    resposta = input("Deseja cadastrar outro usuário? (S/N): ").strip().lower()
    if resposta != 's':
        break