# Questão 1 

# exigência de código 1, exibe o print de boas-vindas
print("Bem-vindo(a) a loja da Allana Helena Campos Albino") # exibe apenas a saida de boas-vindas

# exigência de código 2, input do valorDoPedido e da quantidadeDeParcelas
valorDoPedido = float(input("Entre com o valor do pedido: ")) # o flot input recebe o valor do pedido em float
quantidadeDeParcelas = int(input("Entre com a quantidade de parcelas: ")) # o int input recebe o valor do pedido em inteiro

# exigência de código 3 e 5, implementação de juros com uso de if,elif e else, e o operador and
if quantidadeDeParcelas < 4: # se a parcela for menor que 4 
    juros = 0 # o juros será de 0%
elif quantidadeDeParcelas >= 4 and quantidadeDeParcelas < 6: # mas se a parcela seja maior ou igual 4 e menor do que 6
    juros = 0.04 # o juros será de 4%
elif quantidadeDeParcelas >= 6 and quantidadeDeParcelas < 9: # mas se a parcela seja maior ou igual a 6 e menor do que 9
    juros = 0.08 #o juros será de 8%
elif quantidadeDeParcelas >= 9 and quantidadeDeParcelas < 13: # mas se a parcela seja maior ou igual a 9 e menor do que 13
    juros = 0.16 # o juros será de 16%
else: # e caso nenhuma desas condições for verdade, o juros será de 32%
    juros = 0.32

# exigência de código 4, implementação do valorDaParcela e do valorTotalParcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeDeParcelas # conta o valor da parcela                 
valorTotalParcelado = valorDaParcela * quantidadeDeParcelas # conta o valor total parcelado


print(f"O valor das parcelas é de: {valorDaParcela}") # saida do resultado das parcelas
print(f"O valor total parcelado é de: {valorTotalParcelado}") # saida do valor total parcelado
# print(f"Essa foi a porcentagem de juros da sua parcela: {juros * 100}%") exibiria qual foi a porcentagem de juros do cliente




