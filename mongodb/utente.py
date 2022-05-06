# Lorenzo Mogicato
# Simone Daniele
# Matias Maiorano

from pymongo import MongoClient
import datetime
import os


def print_info_acquisto(e):
    while True:
        clear_console()
        print_evento(e)
        i = 1
        scelte = []
        menu = ""
        for x in e["posti"].keys():
            print(
                f'[{i}] - {x}: {e["posti"][x]["prezzo"]}EUR, {e["posti"][x]["posti"]} posti rimanenti')
            scelte.append(x)
            i += 1
        print("[9] - Indietro")
        decisione = input("> ")
        try:
            decisione = int(decisione) - 1
            lst_scelte = [x for x in range(i-1)]
            lst_scelte.append(9-1) # uscita
            if decisione in lst_scelte:
                break
            else:
                print("Input invalido")
                input("Premi un tasto per continuare\n>")
        except:
            print("Input invalido")
            input("Premi un tasto per continuare\n>")
        if decisione == 9 - 1:
            return
    while True:
        try:
            clear_console()
            print_evento(e)
            quantita = int(input("\nInserisci numero biglietti da acquistare: "))
            break
        except:
            print("Input invalido")
            input("Premi un tasto per continuare\n>")
            clear_console()
            continue
    acquista(e, scelte[decisione], quantita)
    pass

def clear_console():
    os.system("cls")
    pass


def utente():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # TODO inserimento data "massima"

    index = 0

    result = []
    while True:
        if not result:
            result_exist = False
        while result_exist == False:
            req = input("Inserisci nome artista: ")
            query = {
                "$and": [
                    {"cantanti": {"$in": [req]}},
                    {"dataora": {"$gt": now}},
                    {"posti_totali": {"$gt": 0}}
                    # TODO luogo range < 7 km
                ]
            }
            result = list(mongo.eventi.concerti.find(filter=query))
            if result:
                result_exist = True
            else:
                print("Nessun risultato per il seguente artitsta:", req)
        clear_console()
        print(f"Risultati per {req} | pagina numero [{index + 1}/{len(result)}]")
        print_evento(result[index])
        print("[1] - Precedente")
        print("[2] - Successivo")
        print("[3] - Seleziona evento")
        print("[9] - Esci")
        scelta = input("> ")
        try:
            scelta = int(scelta)
        except:
            scelta = 10 # metto 10 se non posso fare il casting della scelta
            clear_console()
            print("Input invalido")
            input("Premi un tasto per continuare\n>")
        if scelta == 1 and index != 0:
            index -= 1
            clear_console()
        elif scelta == 2:
            if index == len(result) - 1:
                clear_console()
                print(f"Eventi finiti per l'artitsta {req}")
                input("Premi un tasto per continuare\n>")
                index = -1
            index += 1
            clear_console()
        elif scelta == 3:
            print_info_acquisto(result[index])
        elif scelta == 9:
            clear_console()
            break
        else:
            print("Input invalido")
            input("Premi un tasto per continuare\n>")


    pass


def print_evento(e):
    print("Data:", e['dataora'])
    print("Luogo:", e['luogo'])
    cantanti = e['cantanti']
    print("Cantante/i:", cantanti[0], end='')
    for cantante in cantanti[1:]:
        print(", " + cantante, end='')
    print("\nPosti rimanenti:", e['posti_totali'])


def acquista(e, tipo_posto, quantity=1, interrupt_after_purchase=True):
    # TODO controllare che quantity non sfori il numero di posti disponibili
    names = []
    for _ in range(quantity):
        names.append(input("Inserisci nominativo/i: "))

    # Scalo quantity-posti da posti_totali e dal tipo del posto
    mongo.eventi.concerti.update_one({"_id": e["_id"]}, {
        '$set': {
            'posti_totali': e["posti_totali"] - quantity,
            f'posti.{tipo_posto}.posti': e["posti"][tipo_posto]["posti"] - quantity
        }}
    )

    # Genero biglietto
    for name in names:
        biglietto = {
            "tipo_posto": tipo_posto,
            "owner": name,
            "concerto": {
                "id": e["_id"],
                "cantanti": e["cantanti"],
                "dataora": e["dataora"],
                "luogo": e["luogo"]
            }
        }
        mongo.eventi.biglietti.insert_one(biglietto)

    print("Grazie per l'acquisto")
    if interrupt_after_purchase:
        exit()


if __name__ != '__main__':
    raise Exception("Lanciami come programma principale grazie")
else:
    clear_console()
    mongo = MongoClient('mongodb://localhost:37000/')
    utente()
    mongo.close()
    print("Grazie per usato il servizio di biglietteria")
