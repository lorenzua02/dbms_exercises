import os
import menu
from stagemodel import Neo4jModel


def create_node(neo4j_model):
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

    elif option_create_node == 1:
        print("\nCreazione alunno: \n")
        # Funzione Create Alunno
        name = input("Inserisci il nome: ")
        course = input("Inserisci il corso: ")
        result = neo4j_model.create_node("S", name=name, course=course)
        if result != -1:
            print("Creazione alunno riuscita")
            print("Id:", result)
        else:
            print("Creazione alunno non riuscita")
        input("Continua...")

    elif option_create_node == 2:
        print("\nCreazione professore: \n")
        # Funzione Create Professore
        name = input("Inserisci il nome: ")
        surname = input("Inserisci il cognome: ")
        subject = input("Inserisci la materia: ")
        result = neo4j_model.create_node(
            "P", name=name, surname=surname, subject=subject)
        if result != -1:
            print("Creazione professore riuscita")
            print("Id:", result)
        else:
            print("Creazione professore non riuscita")
        input("Continua...")

    elif option_create_node == 3:
        print("\nCreazione azienda: \n")
        # Funzione Create Professore
        name = input("Inserisci il nome: ")
        desc = input("Inserisci la descrizione: ")
        result = neo4j_model.create_node("C", name=name, desc=desc)
        if result != -1:
            print("Creazione azienda riuscita")
            print("Id:", result)
        else:
            print("Creazione azienda non riuscita")
        input("Continua...")
    return 0


def create_relation(neo4j_model):
    os.system("cls")
    print('[Menu -> Crea relazione]\n\n')
    name_node = input("Inserisci il nome d'origine: ")
    id_origin_node = neo4j_model.return_node(label=name_node)
    if id_origin_node == -1:
        print("Nome non trovato")
        input("Continua...")
        return 0
    name_node = input("Inserisci il nome di destinazione: ")
    id_destination_node = neo4j_model.return_node(label=name_node)
    if id_destination_node == -1:
        print("Nome non trovato")
        input("Continua...")
        return 0
    relation_name = input("Inserisci il nome della relazione: ")
    result = neo4j_model.create_link(id_origin_node, id_destination_node, relation_name)
    if result != -1:
        print("Relazione creata")
        input("Continua...")
        return 0
    else: 
        print("Relazione non creata")
        input("Continua...")
    return 0


def main_menu(neo4j_model):
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
            option = create_node(neo4j_model)

        elif option == 2:
            option = create_relation(neo4j_model)
            continue
        elif option == 3:
            continue
        elif option == 4:
            continue
        elif option == 5:
            continue
        else:
            continue


if __name__ == '__main__':
    model = Neo4jModel("bolt://localhost:7687", "", "")
    main_menu(model)
