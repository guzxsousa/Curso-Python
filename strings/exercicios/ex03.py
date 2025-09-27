# Cadastro de e-mails

nome = input("Informe seu nome: ").strip()

email = input("Informe seu email: ").strip()

indice_arroba = email.find('@') # -> Retorna -1, caso não encontre o char

if nome and email:

    if '@' in email:

        if (indice_arroba != -1) and ('.' in email[indice_arroba:]):

            print(f"Email Válido: {email}")

        else:

            print("Email Inválido!")
    else:

        print("Email Inválido!")

else:

    print("Digite os campos corretamente.")
