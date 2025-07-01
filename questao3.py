# Questão 3

# exigência de código 1, exibe o print de boas-vindas 
print("Bem-vindo à Fábrica de Camisetas da Allana Helena Campos Albino") 

# exigência de código 2, criação da função escolha_modelo
def escolha_modelo():
    while True:  # repete até escolher um modelo válido
        print("Escolha o modelo de camiseta:")
        print("MCS - Manga Curta Simples (R$1.80)")
        print("MLS - Manga Longa Simples (R$2.10)")
        print("MCE - Manga Curta com Estampa (R$2.90)")
        print("MLE - Manga Longa com Estampa (R$3.20)")
        modelo = input("Digite o modelo desejado: ")  # recebe o modelo 

        if modelo == "MCS":
            return 1.80  # retorna o valor do modelo
        elif modelo == "MLS":
            return 2.10
        elif modelo == "MCE":
            return 2.90
        elif modelo == "MLE":
            return 3.20
        else:
            print("Modelo inválido. Tente novamente.\n")  # mensagem de erro caso digite errado com quebra de linha

# exigência de código 3, criação da função num_camisetas
def num_camisetas():
    while True:  # repete até o número da camisa estar dentro do limite e ser válido
        try:
            num = int(input("Digite o número de camisetas: "))  # recebe o número total de camisetas
            if num > 20000:
                print("Não aceitamos pedidos com mais de 20.000 camisetas.\n")  # valida o limite
                continue
            if num < 20:
                desconto = 0.0
            elif num < 200:
                desconto = 0.05
            elif num < 2000:
                desconto = 0.07
            else:  # entre 2000 e 20000
                desconto = 0.12

            return num * (1 - desconto)  # aplica o desconto e retorna a quantidade ajustada
        except ValueError:  # exigência de código 6, uso do try/except para número inválido
            print("Entrada inválida. Digite um número inteiro.\n")

# exigência de código 4, criação da função frete
def frete():
    while True:  # repete até escolher uma opção válida
        print("Escolha o tipo de frete:")
        print("0 - Retirar na fábrica (R$0.00)")
        print("1 - Transportadora (R$100.00)")
        print("2 - Sedex (R$200.00)")
        tipo = input("Digite o número da opção desejada: ")  # recebe o tipo de  frete

        if tipo == "0":
            return 0.00  # retorna o valor do frete
        elif tipo == "1":
            return 100.00
        elif tipo == "2":
            return 200.00
        else:
            print("Opção inválida. Tente novamente.\n")  

# exigência de código 5, cálculo do total principal fora das funções 
preco_modelo = escolha_modelo()  # chama a função para pegar o preço da camiseta
qtd_final = num_camisetas()  # chama a função para calcular a quantidade com desconto
frete_final = frete()  # chama a função do frete

# cálculo do valor total (preço do modelo * quantidade com desconto + frete)
total = (preco_modelo * qtd_final) + frete_final

# exibe o valor final do pedido
print(f"\nTotal a pagar: R$ {total:.2f}")  # mostra o total final formatado com duas casas decimais
