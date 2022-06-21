import os
import menu
from stagemodel import Neo4jModel, Scuola
from seeder_es2 import seeder

'''menu
[Menu]
|[1]| Crea nodo
|[2]| Crea relazione
|[3]| Cancella nodo
|[4]| Cerca il miglior prof
|[5]| Pulizia del database
|[6]| Importa dummy data
|[9]| Esci
'''


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
            # print("Id:", result)
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
            # print("Id:", result)
        else:
            print("Creazione professore non riuscita")
        input("Continua...")

    elif option_create_node == 3:
        print("\nCreazione azienda: \n")
        # Funzione Create Azienda
        name = input("Inserisci il nome: ")
        desc = input("Inserisci la descrizione: ")
        result = neo4j_model.create_node("C", name=name, desc=desc)
        if result != -1:
            print("Creazione azienda riuscita")
            # print("Id:", result)
        else:
            print("Creazione azienda non riuscita")
        input("Continua...")
    return 0


def create_relation(neo4j_model):
    os.system("cls")
    print('[Menu -> Crea relazione]\n\n|[1]| Prof -> Alunno : insegna_a\n|[2]| Alunno -> Azienda : lavora_in\n|[3]| Prof -> Azienda : contatto_in\n|[9]| Torna indietro\n')
    option_create_relation = input("Inserisci scelta: ")
    try:
        option_create_relation = int(option_create_relation)
    except:
        # Scelta non presente
        option_create_relation = -1
    if option_create_relation == 9:
        return 0
    
    elif option_create_relation == 1:
        error = False
        print("\nCreazione relazione Prof -> Alunno : insegna_a \n")
        # Funzione relazione prof -> alunno : insegna
        print("Inserisci i dati del professore")
        name = input("Inserisci il nome: ")
        surname = input("Inserisci il cognome: ")
        subject = input("Inserisci la materia: ")
        try:
            origin_id = neo4j_model.get_id(label='P', name=name, surname=surname, subject=subject)
        except:
            print('Problema nel trovare il nodo')
            error = True
            input('Continua...')
        if not error:
            print("Inserisci i dati dell' alunno")
            name = input("Inserisci il nome: ")
            course = input("Inserisci il corso: ")
            try:
                destination_id = neo4j_model.get_id(label='S', name=name, course=course)
            except:
                print('Problema nel trovare il nodo')
                error = True
                input('Continua...')
            if not error:
                result = neo4j_model.create_link(origin_id, destination_id, 'insegna_a')
                if result != -1:
                    print("Creazione relazione riuscita")
                    # print("Id:", result)
                else:
                    print("Creazione relazione non riuscita")
                input("Continua...")
        
    elif option_create_relation == 2:
        error = False
        print("\nCreazione relazione Alunno -> Azienda : lavora_in \n")
        # Funzione relazione Alunno -> Azienda : lavora_in
        print("Inserisci i dati dell' alunno")
        name = input("Inserisci il nome: ")
        course = input("Inserisci il corso: ")
        try:
            origin_id = neo4j_model.get_id(label='S', name=name, course=course)
        except:
            print('Problema nel trovare il nodo')
            error = True
            input('Continua...')
        if not error:
            print("Inserisci i dati dell'azienda")
            name = input("Inserisci il nome: ")
            desc = input("Inserisci la descrizione: ")
            try:
                destination_id = neo4j_model.get_id(label='C', name=name, desc=desc)
            except:
                print('Problema nel trovare il nodo')
                error = True
                input('Continua...')
            if not error:
                result = neo4j_model.create_link(origin_id, destination_id, 'lavora_in')
                if result != -1:
                    print("Creazione relazione riuscita")
                    # print("Id:", result)
                else:
                    print("Creazione relazione non riuscita")
                input("Continua...")
                
    elif option_create_relation == 3:
        error = False
        print("\nCreazione relazione Prof -> Azienda : contatto_in \n")
        # Funzione relazione Prof -> Azienda : contatto_in
        print("Inserisci i dati del professore")
        name = input("Inserisci il nome: ")
        surname = input("Inserisci il cognome: ")
        subject = input("Inserisci la materia: ")
        try:
            origin_id = neo4j_model.get_id(label='P', name=name, surname=surname, subject=subject)
        except:
            print('Problema nel trovare il nodo')
            error = True
            input('Continua...')
        if not error:
            print("Inserisci i dati dell'azienda")
            name = input("Inserisci il nome: ")
            desc = input("Inserisci la descrizione: ")
            try:
                destination_id = neo4j_model.get_id(label='C', name=name, desc=desc)
            except:
                print('Problema nel trovare il nodo')
                error = True
                input('Continua...')
            if not error:
                result = neo4j_model.create_link(origin_id, destination_id, 'lavora_in')
                if result != -1:
                    print("Creazione relazione riuscita")
                    # print("Id:", result)
                else:
                    print("Creazione relazione non riuscita")
                input("Continua...")
                
    return 0

def delete_node(neo4j_model):
    os.system("cls")
    print('[Menu -> Cancella nodo]\n\n|[1]| Cancella Alunno\n|[2]| Cancella Professore\n|[3]| Cancella Azienda\n|[9]| Torna indietro\n')
    option_delete_node = input("Inserisci scelta: ")
    try:
        option_delete_node = int(option_delete_node)
    except:
        # Scelta non presente
        option_delete_node = -1
    if option_delete_node == 9:
        return 0

    elif option_delete_node == 1:
        print("\nCancellazione alunno: \n")
        # Funzione Cancella Alunno
        name = input("Inserisci il nome: ")
        course = input("Inserisci il corso: ")
        try:
            result = neo4j_model.delete_node(neo4j_model.get_id("S", name=name, course=course))
        except:
            result = -1
        if result != -1:
            print("Cancellazione alunno riuscita")
            # print("Id:", result)
        else:
            print("Cancellazione alunno non riuscita")
        input("Continua...")
        
    elif option_delete_node == 2:
        print("\nCancellazione professore: \n")
        # Funzione Cancella Professore
        name = input("Inserisci il nome: ")
        surname = input("Inserisci il cognome: ")
        subject = input("Inserisci la materia: ")
        try:
            result = neo4j_model.delete_node(neo4j_model.get_id("P", name=name, surname=surname, subject=subject))
        except:
            result = -1
        if result != -1:
            print("Cancellazione professore riuscita")
            # print("Id:", result)
        else:
            print("Cancellazione professore non riuscita")
        input("Continua...")

    elif option_delete_node == 3:
        print("\nCancellazione azienda: \n")
        # Funzione Cancella Azienda
        name = input("Inserisci il nome: ")
        desc = input("Inserisci la descrizione: ")
        try:
            result = neo4j_model.delete_node(neo4j_model.get_id("C", name=name, desc=desc))
        except:
            result = -1
        if result != -1:
            print("Cancellazione azienda riuscita")
            # print("Id:", result)
        else:
            print("Cancellazione azienda non riuscita")
        input("Continua...")
    return 0

def find_best(neo4j_model):
    print("[Menu -> Cerca il miglior prof]\n\n|[1]| Inserisci i dati dell'azienda\n|[9]| Torna indietro\n")
    option_find_best_prof = input("Inserisci scelta: ")
    try:
        option_find_best_prof = int(option_find_best_prof)
    except:
        # Scelta non presente
        option_find_best_prof = -1
    if option_find_best_prof == 9:
        return 0
    
    elif option_find_best_prof == 1:

        name = input("Inserisci il nome: ")
        desc = input("Inserisci la descrizione: ")
        try:
            result = neo4j_model.best_prof(neo4j_model.get_id("C", name=name, desc=desc))
        except:
            result = -1
        if result != -1:
            print("Risultati trovati:")
            for x in result:
                print(x['p']['name'], x['p']['surname'], f"({x['p']['subject']})")
            # print("Id:", result)
        else:
            print("Nessun match trovato")
        input("Continua...")
    return 0


def main_menu(neo4j_model):
    while True:
        os.system("cls")
        print('[Menu]\n\n|[1]| Crea nodo\n|[2]| Crea relazione\n|[3]| Cancella nodo\n|[4]| Cerca il miglior prof\n|[5]| Pulizia del database\n|[6]| Importa dummy data\n|[9]| Esci\n')
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

        elif option not in [x for x in range(0, 7)]:
            print("Scelta non presente")
            input("Premi un tasto per continuare")
            continue
        
        #Crea nodo
        elif option == 1:
            option = create_node(neo4j_model)
            
        # Crea relazione
        elif option == 2:
            option = create_relation(neo4j_model)
            continue
        
        # Cancella nodo
        elif option == 3:
            option = delete_node(neo4j_model)
            continue
        
        # Cerca il miglior prof
        elif option == 4:
            option = find_best(neo4j_model)
            continue
        
        # Pulizia db
        elif option == 5:
            neo4j_model.empty_database()
            print('Database pulito')
            input('Continua...')
            continue

        # Import seeder
        elif option == 6:
            seeder(neo4j_model)
            print('Dataset Importato')
            input('Continua...')
            continue

if __name__ == '__main__':
    model = Scuola("bolt://localhost:7687", "", "")
    main_menu(model)