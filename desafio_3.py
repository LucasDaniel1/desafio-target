# Primeiro preciso importar a biblioteca datetime para poder trabalhar com datas e horas
from datetime import datetime

# Preciso pegar o valor da conta, para isso uso a função input() e a função float() para converter a string em um número decimal
while True:
    
    try:
        valor = float(input("\nDigite o valor da conta: R$ "))

        if valor < 0:
            print("Erro: o valor não pode ser negativo.")
            continue

        break

    except ValueError:
        print("Erro: digite um valor numérico válido.")


# Agora preciso pegar a data de vencimento da conta, para isso uso a função input() e a função strptime() da biblioteca datetime para converter a string em um objeto datetime
while True:
    
    data_input = input("Digite a data de vencimento (dd/mm/aaaa): ")

    try:
        # Converto a string em um objeto datetime usando o formato dd/mm/aaaa
        data_vencimento = datetime.strptime(data_input, "%d/%m/%Y")
        break

    except ValueError:
        print("Erro: data inválida. Digite no formato dd/mm/aaaa.")

# Pego a data de hoje para poder comparar com a data de vencimento
data_hoje = datetime.today()

# Calculo a diferença entre a data de hoje e a data de vencimento para saber se a conta está atrasada ou não
dia_de_atraso = (data_hoje - data_vencimento).days

# Assim, primeiro verifico se a conta está atrasada ou não, se não estiver atrasada, o valor da multa será 0
# caso contrário, o valor da multa será calculado com base no valor da conta e na quantidade de dias de atraso
if dia_de_atraso <= 0:
    juros = 0
    valor_final = valor

    print(f"\nConta não está atrasada.")
    print(f"Valor: R$ {valor:.2f}")
    print(f"Juros: R$ {juros:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}\n")

# caso esteja atrasada
else:
    # o valor da multa será de 2,5% do valor da conta por dia de atraso
    taxa_diaria = 0.025

    juros  = valor * taxa_diaria * dia_de_atraso
    valor_final  = valor + juros

    print(f"\nDias de atraso: {dia_de_atraso}")
    print(f"Valor original: R$ {valor:.2f}")
    print(f"Juros: R$ {juros:.2f}")
    print(f"Valor final: R$ {valor_final:.2f}\n")