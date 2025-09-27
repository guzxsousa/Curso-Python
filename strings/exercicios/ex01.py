# Cadastro de CPF: Crie um programa para cadastro de CPF de clientes que recebe o CPF em um input apenas com número.

cpf = input("Informe seu CPF (apenas números): ").strip()

if cpf.isalnum() and len(cpf)==11:

    print(f"{cpf} verificado.")

else:

    print(f"{cpf} inválido, digite apenas números.")

