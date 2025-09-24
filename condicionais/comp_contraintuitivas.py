# Comparações Contraintuitivas:

faturamento = input("Informe o faturamento da loja: ")

custo = input("Informe o custo da loja: ")

if faturamento and custo:

    lucro = float(faturamento) - float(custo)
    print(f"\nLucro  = R${lucro:.2f}")

else:

    print("Faturamento ou Custo não informados!!\n")
    
# tambem poderia usar o tratamento de erros.

