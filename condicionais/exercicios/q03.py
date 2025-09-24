# Criando um mini sistema de controle de estoque:
# - Categorias = alimentos, bebidas e limpeza
# - Estoque min = 50, 75 e 30

try:

    nome_produto = input("Informe o nome do produto: ")

    categoria = input("Informe a categoria do produto: ").lower().strip()

    qtd_atual_estoque = int(input("Informe a quantidade atual do produto no estoque: "))

    if not (nome_produto and categoria and str(qtd_atual_estoque)):

        print("\nVocê deixou de preencher alguns dos campos.\n")

    elif categoria ==  'alimentos':

        if qtd_atual_estoque < 50:

            print(f"\nSolicitar {nome_produto} à equipe de compras, temos apenas {qtd_atual_estoque} unidades em estoque!")

    elif categoria == 'bebidas':

        if qtd_atual_estoque < 75:

            print(f"\nSolicitar {nome_produto} à equipe de compras, temos apenas {qtd_atual_estoque} unidades em estoque!")

    elif categoria == 'limpeza':

        if qtd_atual_estoque < 30:

            print(f"\nSolicitar {nome_produto} à equipe de compras, temos apenas {qtd_atual_estoque} unidades em estoque!")

    else:

        print("Categoria Não existe!")

except ValueError:

    print("\nErro! Preencha corretamente os campos!\n")
