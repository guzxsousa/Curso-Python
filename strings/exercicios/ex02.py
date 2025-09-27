# Melhorando o cadastro de CPF: Adicione outras verificações

# Eliminaado pontos, traços e espaços em brancos.

cpf = input("Informe seu cpf: ").strip().replace(".","").replace("-", "")

if cpf.isalnum() and len(cpf)==11:

    print(f"{cpf} verificado.")

else:

    print(f"{cpf} | inválido!")


