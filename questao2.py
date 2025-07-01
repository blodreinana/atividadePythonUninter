# Questão 2

# exigência de código 1, exibe o print de boas-vindas
print("-- Bem-vindo a Loja de Marmitas da Allana Helena Campos Albino -")  
print(25 * "-", "Cardápio", 29 * "-")  # estimei quantos - iam para a formatção ficar proxima a do exemplo
print(64 * "-")
print(4 * "-", "|", "Tamanho", "|", " Bife Acebolado(BA)", "|", "  Filé de Frango(FF)", "|", 2 * "-")  
print(4 * "-", "|", "    P  ", "|", "       R$ 16.00    ", "|", "      R$ 15.00      ", "|", 2 * "-")  
print(4 * "-", "|", "    M  ", "|", "       R$ 18.00    ", "|", "      R$ 17.00      ", "|", 2 * "-")  
print(4 * "-", "|", "    G  ", "|", "       R$ 22.00    ", "|", "      R$ 21.00      ", "|", 2 * "-")  
print(64 * "-")  
print(64 * "-")  

# exigência de código 5, criação do acumulador para somar os valores dos pedidos
total = 0.0  # total do pedido inicializado com zero

# exigência de código 6, laço principal que repete o processo até o cliente não querer mais
while True:
    # exigência de código 2, input do sabor com validação
    while True:
        sabor = input("Entre com o sabor desejado (BA/FF): ")  # recebe o sabor
        if sabor in ["BA", "FF"]:  # verifica se ele é válido
            break  # se é válido, sai do loop interno
        print("Sabor inválido. Tente novamente")  # mensagem de erro

    # exigência de código 3, input do tamanho com validação
    while True:
        tamanho = input("Entre com o tamanho desejado (P/M/G): ")  # recebe o tamanho
        if tamanho in ["P", "M", "G"]:  # verifica se ele é válido
            break  # se é válido, sai do loop interno
        print("Tamanho inválido. Tente novamente")  # mensagem de erro

    # exigência de código 4, uso de estrutura aninhada para definir o preço com base nas escolhas
    if sabor == "BA":  # se for Bife Acebolado
        if tamanho == "P":
            preco = 16.00
        elif tamanho == "M":
            preco = 18.00
        else:  # tamanho == "G"
            preco = 22.00
    else:  # sabor == "FF" (Filé de Frango)
        if tamanho == "P":
            preco = 15.00
        elif tamanho == "M":
            preco = 17.00
        else:  # tamanho == "G"
            preco = 21.00

    # exigência de código 5, soma o valor ao total
    total += preco  # adiciona o preço do item ao total acumulado

    # exibe o resumo do item pedido
    print(f"Você pediu um {'Bife Acebolado' if sabor == 'BA' else 'Filé de Frango'} no tamanho {tamanho}: R$ {preco:.2f}")

    # exigência de código 6, pergunta se deseja continuar ou encerrar
    continuar = input("Deseja mais alguma coisa? (S/N): ")  # pergunta ao cliente
    if continuar == "N":
        break  # encerra o laço principal se for N
    continue  # volta ao início se for S

# exibe o valor total do pedido
print(f"O valor total a ser pago: R$ {total:.2f}")  # mostra o total final acumulado arredondado
