# Fatiamento em python: "Pedaços" de strings

email = input("Informe seu email: ")

indice_arroba = email.find("@") + 1

servidor_email = email[indice_arroba:]

print(f"Seu servidor de email é : {servidor_email}")