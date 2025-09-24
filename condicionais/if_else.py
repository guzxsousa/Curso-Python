# Tratando condição falsa - Else;

meta = 50000

qtd_vendidas = int(input("Informe a quantidade vendida no mês: "))

if qtd_vendidas >= meta:

    print(f"Batemos a meta de vendas de iphone e, vendemos {qtd_vendidas} unidades.")

else:
    print("Infelizmente não batemos a meta.")
    print(f"Vendemos {qtd_vendidas} unidades, a meta era {meta} unidades.")
 
