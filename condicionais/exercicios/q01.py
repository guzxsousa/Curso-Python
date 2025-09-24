# Exercício 01: Cálculo de Bônus
# - Se o valor de vendas for >= a meta, o valor do bônus é 10% do valor de vendas;
# - Caso contrário o valor é 0.

meta_vendas = 1000

for i in range(3):

    valor_vendas = float(input(f"Informe o valor de vendas do funcionário {i+1}: "))

    if valor_vendas >= meta_vendas:

        bonus = 0.10 * valor_vendas

    else:

        bonus = 0

    print(f"Valor Vendas = R${valor_vendas:.2f} | Bônus = R${bonus} .")
        

