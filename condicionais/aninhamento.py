# -  Exemplo: Fundo de Investimentos

# No mínimo 5% de retorno ao ano;

# Caso o fundo não consiga entrgar os 5% de retorno, ele não pode cobrar taxa dos investidores;

# Caso o fundo consiga entrgar mais de 5% de retorno, ele irá cobrar 2% de taxa dos investidores;

# Caso o fundo consiga mais de 20% de retorno, ele irá cobrar 4% de taxa dos seus investidores.

retorno_min = 0.05

rendimento = float(input("Informe o rendimento: "))

if (rendimento/100) > retorno_min:

    if(rendimento/100)> 0.2:

        taxa = 0.04
     
    else:

        taxa = 0.02
    
else:

    taxa = 0

print(f"Taxa = {taxa:.2%}")


    



