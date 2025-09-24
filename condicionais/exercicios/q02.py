# Exercícios 02:
# - Meta = 1000 vendas;
# - Se valor_vendas >= 2000, bônus = 15% do valor de vendas;
# - Se valor_vendas < 2000, bônus = 10% do valor de vendas;
# - Se valor_vendas < 1000, bônus = 0.

meta_vendas = 1000

for i in range(5):

    valor_vendas = float(input(f"Informe o valor de vandas do funcionário {i+1}: "))

    if valor_vendas>=2000:
        
        bonus = 0.15 * valor_vendas

    elif valor_vendas>=1000:

        bonus = 0.1 * valor_vendas

    else:

        bonus = 0

    print(f"Valor Vendas = R${valor_vendas:.2f} | Bônus = R${bonus}\n")    