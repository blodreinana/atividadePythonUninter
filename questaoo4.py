# Questão 4

# exigência de código 1, exibe o print de boas-vindas 
print("Bem-vindo à Empresa de Allana Helena Campos Albino")  # exibe a saudação inicial com nome completo

# exigência de código 2, criação da lista e da variável id_global
lista_funcionarios = []  # lista que irá armazenar os dicionários com os dados dos funcionários
id_global = 5349178  # define o RU como valor inicial do ID dos funcionários

# exigência de código 3, função que cadastra o funcionário
def cadastrar_funcionario(id):
    print(3 * "-", "Cadastrar Funcionário", 3 * "-")
    print(f"ID do Funcionário: {id}")  # mostra o ID que será atribuído
    nome = input("Nome: ")  # input do nome
    setor = input("Setor: ")  # input do setor
    salario = float(input("Salário: "))  # input do salário

    funcionario = {
        "id": id,
        "nome": nome,
        "setor": setor,
        "salario": salario
    }

    lista_funcionarios.append(funcionario.copy())  # exigência de código 7, adiciona uma cópia do dicionário
    print("Funcionário cadastrado com sucesso!")  # confirmação

# exigência de código 4, função que permite consultar funcionários
def consultar_funcionarios():
    while True:
        print(3 * "-", "Consultar Funcionário", 3 * "-")
        print("1 - Consultar Todos os Funcionários")
        print("2 - Consultar Funcionário por ID")
        print("3 - Consultar Funcionário(s) por Setor")
        print("4 - Retornar ao menu")
        opcao = input("Escolha uma opção: ")  # input da escolha

        if opcao == "1":
            for func in lista_funcionarios:
                print("\nID:", func["id"])
                print("Nome:", func["nome"])
                print("Setor:", func["setor"])
                print("Salário: R$", func["salario"])
        elif opcao == "2":
            id_busca = int(input("Digite o ID do funcionário: "))
            encontrou = False
            for func in lista_funcionarios:
                if func["id"] == id_busca:
                    print("\nID:", func["id"])
                    print("Nome:", func["nome"])
                    print("Setor:", func["setor"])
                    print("Salário: R$", func["salario"])
                    encontrou = True
            if not encontrou:
                print("ID inválido.")
        elif opcao == "3":
            setor_busca = input("Digite o setor: ")
            encontrou = False
            for func in lista_funcionarios:
                if func["setor"].lower() == setor_busca.lower():
                    print("\nID:", func["id"])
                    print("Nome:", func["nome"])
                    print("Setor:", func["setor"])
                    print("Salário: R$", func["salario"])
                    encontrou = True
            if not encontrou:
                print("Nenhum funcionário encontrado neste setor.")
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

# exigência de código 5, função que remove funcionário da lista
def remover_funcionario():
    print(3 * "-", "Remover Funcionário", 3 * "-")
    id_remover = int(input("Digite o ID do funcionário a ser removido: "))
    encontrou = False
    for i in range(len(lista_funcionarios)):
        if lista_funcionarios[i]["id"] == id_remover:
            del lista_funcionarios[i]  # remove o funcionário
            print("Funcionário removido com sucesso.")
            encontrou = True
            break
    if not encontrou:
        print("ID inválido.")  # se o ID não for encontrado

# exigência de código 6, menu principal com repetição
while True:
    print(3 * "-", "Menu Principal", 3 * "-")
    print("1 - Cadastrar Funcionário")
    print("2 - Consultar Funcionário")
    print("3 - Remover Funcionário")
    print("4 - Encerrar Programa")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_funcionario(id_global)  # chama a função de cadastro
        id_global += 1  # incrementa o ID
    elif escolha == "2":
        consultar_funcionarios()  # chama a função de consulta
    elif escolha == "3":
        remover_funcionario()  # chama a função de remoção
    elif escolha == "4":
        print("Programa encerrado.")  # encerra o programa
        break
    else:
        print("Opção inválida.")  # caso a escolha seja incorreta
