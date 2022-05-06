# Lorenzo Mogicato
# Simone Daniele
# Matias Maiorano

from pymongo import MongoClient
import datetime

if __name__ != '__main__':
    raise Exception("Lanciami come programma principale grazie")


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


def print_info_acquisto(e):
    i = 1
    scelte = []
    for x in e["posti"].keys():
        print(f'[{i}] - {x}: {e["posti"][x]["prezzo"]}EUR, {e["posti"][x]["posti"]} posti rimanenti')
        scelte.append(x)
        i += 1
    print("[9] - Indietro")
    decisione = int(input("> ")) - 1
    if decisione == 9 - 1:
        return
    while True:
        try:
            quantita = int(input("Inserisci numero biglietti da acquistare: "))
            break
        except e:
            print("Inserisci un numero")
            continue
    acquista(e, scelte[decisione], quantita)


mongo = MongoClient('mongodb://localhost:37000/')
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

req = input("Inserisci nome artista: ")
# TODO inserimento data "massima"

query = {
    "$and": [
        {"cantanti": {"$in": [req]}},
        {"dataora": {"$gt": now}},
        {"posti_totali": {"$gt": 0}}
        # TODO luogo range < 7 km
    ]
}

index = 0

while True:
    result = list(mongo.eventi.concerti.find(filter=query))
    if not result:
        # TODO richiere l'input
        raise Exception("Artista non presente")
    print_evento(result[index])
    print("[1] - Precedente")
    print("[2] - Successivo")
    print("[3] - Seleziona evento")
    print("[9] - Esci")
    scelta = int(input("> "))
    if scelta == 1 and index != 0:
        index -= 1
    elif scelta == 2 and index != len(result) - 1:
        index += 1
    elif scelta == 3:
        print_info_acquisto(result[index])
    elif scelta == 9:
        break
    else:
        print("Invalido")

mongo.close()
print("Grazie per usato il servizio di biglietteria")
