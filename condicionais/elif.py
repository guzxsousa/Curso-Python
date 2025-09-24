# - Condicionais em Python: Elif - Para condições sequenciais

# Exemplo: Analisar bônus dos funcionários.

# Regras de bônus:
# - vendas abaixo da meta, não ganha bônus;
# - vendas acima da meta, ganha 3% do valor das vendas;
# - vendas acima de 100% (dobro) da meta, ganha 7% do valor das vendas.

meta_vendas = float(input("Informe a meta de vendas do funcionário: "))

valor_vendas = float(input("Informe quanto o funcionário vendeu: "))

if(valor_vendas > (meta_vendas*2)):

    bonus = 0.07 * valor_vendas

elif(valor_vendas >= meta_vendas):

    bonus = 0.03 * valor_vendas

else:

    bonus = 0

print(f"Vendas = R${valor_vendas:.2f} | Meta = R${meta_vendas:.2f}")
print(f"Bônus: R${bonus:.2f}")

