import os
import menu

def create_node():
    os.system("cls")
    print('[Menu -> Crea nodo]\n\n|[1]| Crea Alunno\n|[2]| Crea Professore\n|[3]| Crea Azienda\n|[9]| Torna indietro\n')
    option_create_node = input("Inserisci scelta: ")
    try:
        option_create_node = int(option_create_node)
    except:
        # Scelta non presente
        option_create_node = -1
    if option_create_node == 9:
        return 0
        option_create_node = 0

    elif option_create_node == 1:
        print("Alunno")
        # Funzione Create Alunno
        input("Continua...")

    elif option_create_node == 2:
        print("Professore")
        # Funzione Create Professore
        input("Continua...")

    elif option_create_node == 3:
        print("Azienda")
        # Funzione Create Azineda
        input("Continua...")
    return 0

def main_menu():
    while True:
        os.system("cls")
        print('[Menu]\n\n|[1]| Crea nodo\n|[2]| Crea relazione\n|[3]| Cancella nodo\n|[4]| Cancella relazione\n|[5]| Cerca il miglior prof\n|[9]| Esci\n')
        option = input("Inserisci scelta: ")

        try:
            option = int(option)
        except:
            # Scelta non presente
            option = -1

        if option == 9:
            input("adios")
            os.system("cls")
            break

        elif option not in [x for x in range(0, 6)]:
            print("Scelta non presente")
            input("Premi un tasto per continuare")
            continue

        elif option == 1:
            option = create_node()

        elif option == 2:
            continue
        elif option == 3:
            continue
        elif option == 4:
            continue
        elif option == 5:
            continue
        else:
            continue