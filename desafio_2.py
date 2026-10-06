# Novamente preciso importar a biblioteca json para poder trabalhar com o arquivo JSON
import json

dados_json = '''
{
	"estoque":
	[
	  {
		"codigoProduto": 101,
		"descricaoProduto": "Caneta Azul",
		"estoque": 150
	  },
	  {
		"codigoProduto": 102,
		"descricaoProduto": "Caderno Universitário",
		"estoque": 75
	  },
	  {
		"codigoProduto": 103,
		"descricaoProduto": "Borracha Branca",
		"estoque": 200
	  },
	  {
		"codigoProduto": 104,
		"descricaoProduto": "Lápis Preto HB",
		"estoque": 320
	  },
	  {
		"codigoProduto": 105,
		"descricaoProduto": "Marcador de Texto Amarelo",
		"estoque": 90
	  }
	]
}
'''
# Preciso agora importar o arquivo JSON para dentro do Python, para isso uso a função loads() da biblioteca json
dados = json.loads(dados_json)

# Variavel para id unico
id_unico = 1

# variaveis para armazenar os dados da movimentação
# Verifica se o código é um número
print("\n")
while True:
    try:
        codigo = int(input("Código do produto: "))
        break
    except ValueError:
        print("Erro: o código do produto deve ser um número.")


# Verifica se o tipo é entrada ou saida
while True:
    tipo = input("Tipo da movimentação (entrada/saída): ").lower().strip()

    if tipo == "entrada" or tipo == "saída":
        break

    print("Erro: digite apenas 'entrada' ou 'saída'.")

# Verifica se a quantidade é um número
while True:
    # Verifica se a quantidade é um número inteiro
    try:
        quantidade = int(input("Quantidade: "))

        if quantidade <= 0:
            print("Erro: a quantidade deve ser maior que zero.")
            continue

        break

    # Caso a quantidade não seja um número inteiro, exibe uma mensagem de erro
    except ValueError:
        print("Erro: a quantidade deve ser um número.")


descricao = input("Descrição da movimentação: ")

# variável para armazenar se o produto foi encontrado ou não
Prod_encontrado = False

# Agora preciso percorrer cada produto e verificar se o código informado existe no estoque
# caso exista preciso atualizar o estoque de acordo com o tipo da movimentação

for produto in dados['estoque']:

    if produto['codigoProduto'] == codigo:
        # Significa que achei o produto
        Prod_encontrado = True

        if tipo == "entrada":
            produto['estoque'] += quantidade

        elif tipo == "saida":

            # se for do tipo de saída entao primeiro preciso verificar se a quantidade solicitada é maior que o estoque atual, 
            # caso seja preciso exibir uma mensagem de erro e não atualizar o estoque
            if quantidade > produto['estoque']:
                print("Erro: estoque insuficiente.")
                break

            # Se a quantidade solicitada for menor ou igual ao estoque atual, então posso atualizar o estoque
            produto['estoque'] -= quantidade


        # Agora preciso exibir os dados da movimentação realizada
        print("\nMovimentação realizada!")
        print(f"ID: {id_unico}")
        print(f"Descrição: {descricao}")
        print(f"Produto: {produto['descricaoProduto']}")
        print(f"Estoque final: {produto['estoque']}\n")

        # Agora preciso incrementar o id unico para a próxima movimentação
        id_unico += 1
        break

# Se o produto não foi encontrado, preciso exibir uma mensagem de erro
if not Prod_encontrado:
    print("Erro: produto não encontrado!!!")