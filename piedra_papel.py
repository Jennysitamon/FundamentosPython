import random
int_rand = random.randint(0, 2)
if int_rand == 0:
    choice_maq = "Piedra"
elif int_rand == 1:
    choice_maq = "Papel"
else:
    choice_maq = "Tijera"

#Elige usuario
choice_txt = """
Elige una Opción:
    Piedra
    Papel
    Tijera
"""
choice_user = input(choice_txt)
print("Maquina ->", choice_maq)
print("Usuario ->", choice_user)

if choice_maq == choice_user:
    print("Es un empate")
else:

    if choice_maq == "Piedra" and choice_user == "Papel":
        print("Gana usuario")

    elif choice_maq == "Piedra" and choice_user == "Tijera":
        print("Gana Máquina")

    elif choice_maq == "Papel" and choice_user == "Piedra":
        print("Gana Máquina")


    elif choice_maq== "Papel" and choice_maq == "Tijera":
        print("Ganaste")

    elif choice_maq == "Tijera" and choice_maq == "Papel":
        print("Gana maquina ")

    else: print("Gana Usuario")

