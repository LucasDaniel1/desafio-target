# Como os dados que recebi estão no formato JSON preciso desta biblioteca para tratar ele como JSON
import json

# Assim carrego os dados
dados_json = '''
{
  "vendas": [
    { "vendedor": "João Silva", "valor": 1200.50 },
    { "vendedor": "João Silva", "valor": 950.75 },
    { "vendedor": "João Silva", "valor": 1800.00 },
    { "vendedor": "João Silva", "valor": 1400.30 },
    { "vendedor": "João Silva", "valor": 1100.90 },
    { "vendedor": "João Silva", "valor": 1550.00 },
    { "vendedor": "João Silva", "valor": 1700.80 },
    { "vendedor": "João Silva", "valor": 250.30 },
    { "vendedor": "João Silva", "valor": 480.75 },
    { "vendedor": "João Silva", "valor": 320.40 },
    
    { "vendedor": "Maria Souza", "valor": 2100.40 },
    { "vendedor": "Maria Souza", "valor": 1350.60 },
    { "vendedor": "Maria Souza", "valor": 950.20 },
    { "vendedor": "Maria Souza", "valor": 1600.75 },
    { "vendedor": "Maria Souza", "valor": 1750.00 },
    { "vendedor": "Maria Souza", "valor": 1450.90 },
    { "vendedor": "Maria Souza", "valor": 400.50 },
    { "vendedor": "Maria Souza", "valor": 180.20 },
    { "vendedor": "Maria Souza", "valor": 90.75 },
    
    { "vendedor": "Carlos Oliveira", "valor": 800.50 },
    { "vendedor": "Carlos Oliveira", "valor": 1200.00 },
    { "vendedor": "Carlos Oliveira", "valor": 1950.30 },
    { "vendedor": "Carlos Oliveira", "valor": 1750.80 },
    { "vendedor": "Carlos Oliveira", "valor": 1300.60 },
    { "vendedor": "Carlos Oliveira", "valor": 300.40 },
    { "vendedor": "Carlos Oliveira", "valor": 500.00 },
    { "vendedor": "Carlos Oliveira", "valor": 125.75 },
    
    { "vendedor": "Ana Lima", "valor": 1000.00 },
    { "vendedor": "Ana Lima", "valor": 1100.50 },
    { "vendedor": "Ana Lima", "valor": 1250.75 },
    { "vendedor": "Ana Lima", "valor": 1400.20 },
    { "vendedor": "Ana Lima", "valor": 1550.90 },
    { "vendedor": "Ana Lima", "valor": 1650.00 },
    { "vendedor": "Ana Lima", "valor": 75.30 },
    { "vendedor": "Ana Lima", "valor": 420.90 },
    { "vendedor": "Ana Lima", "valor": 315.40 }
  ]
}
'''

# Preciso agora importar o arquivo JSON para dentro do Python, para isso uso a função loads() da biblioteca json
dados = json.loads(dados_json)

# Variavel para armazenar o total das vendas
comissoes = {}

# Variavel para armazenar a comissão de cada venda
comissao = 0

# Agora preciso percorrer cada venda e somar o valor das vendas de cada vendedor
for venda in dados['vendas']:

    vendedor = venda['vendedor']
    valor = venda['valor']

    if valor < 100:
        comissao = 0
    elif valor < 500:
        # A comissão é de 1% do valor da venda
        comissao = valor * 0.01
    else:
        # A comissão é de 5% do valor da venda
        comissao = valor * 0.05

    # Agora preciso somar a comissão de cada venda para cada vendedor, para isso uso um dicionário onde a chave é o nome do vendedor e o valor é a soma das comissões
    # Assim se o vendedor já existe pega a comissão atual dele, caso não exista retorna 0
    # depois soma a comissão da venda atual e atualiza o valor no dicionário
    comissoes[vendedor] = comissoes.get(vendedor, 0) + comissao


for vendedor, comissao in comissoes.items():
    print(f'\n\nVendedor: {vendedor}, Comissão Total: R$ {comissao:.2f}')
    
print("\n")