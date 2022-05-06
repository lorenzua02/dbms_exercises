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
        print(", "+cantante, end='')
    print("\nPosti rimanenti:", e['posti_totali'])


def acquista(e, tipo_posto, quantity=1):
    name = input("Inserisci nominativo: ")

    # Scalo quantity-posti da posti_totali e dal tipo del posto
    mongo.eventi.concerti.update_one({"_id": e["_id"]}, {
        '$set': {
            'posti_totali': e["posti_totali"]-quantity,
            f'posti.{tipo_posto}.posti': e["posti"][tipo_posto]["posti"]-quantity
            }}
    )

    # Genero biglietto
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


def print_info_acquisto(e):
    i = 1
    scelte = []
    for x in e["posti"].keys():
        print(f'[{i}] - {x}: {e["posti"][x]["prezzo"]}EUR, {e["posti"][x]["posti"]} posti rimanenti')
        scelte.append(x)
        i += 1
    decisione = int(input("> ")) - 1
    # TODO AA
    acquista(e, scelte[decisione])


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
    print_evento(result[index])
    print("[1] - Precedente")
    print("[2] - Successivo")
    print("[3] - Seleziona evento")
    print("[9] - Esci")
    scelta = int(input("> "))
    if scelta == 1 and index != 0:
        index -= 1
    elif scelta == 2 and index != len(result)-1:
        index += 1
    elif scelta == 3:
        # TODO seleziona evento
        print_info_acquisto(result[index])
        print("IDK")
    elif scelta == 9:
        break
    else:
        print("Invalido")

mongo.close()
print("Adios")
