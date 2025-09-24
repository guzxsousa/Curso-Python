# Casos com várias condições - and e or;

# - Se o valor_vendas > meta_vendas e vendas_loja >= meta_vendas_loja, bônus = 3% do valor_vendas;
# - Se valor_vendas > meta_vendas e vendas_loja < meta_vendas_loja, bônus = 0.
# - Se a nota do funcionário for 9 ou 10, ele tambem ganha 3% do valor_vendas.

meta_vendas = 1000

meta_vendas_loja = 10000

meta_nota = 9

vendas_loja = float(input("Informe o valor da vendas total da loja: \n"))

for i in range(5):

    nota = int(input(f"Informe a nota do funcionário {i+1}: "))

    valor_vendas = float(input(f"Informe o valor de vandas do funcionário {i+1}: "))

    if valor_vendas >= 1000 and vendas_loja >= meta_vendas_loja:
        
        bonus = 0.03 * valor_vendas

    elif nota >= meta_nota:

        bonus = 0.03 * valor_vendas

    else:

        bonus = 0

    print(f"Valor Vendas = R${valor_vendas:.2f} | Bônus = R${bonus}\n")    

# Tambem poderia usar a condição do elif junto com a condição do if, mas utilizando o 'or'.