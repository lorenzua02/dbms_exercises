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


now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

mongo = MongoClient('mongodb://localhost:37000/')

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
result = list(mongo.eventi.concerti.find(filter=query))

while True:
    print_evento(result[index])
    print("1 - Precedente")
    print("2 - Successivo")
    print("3 - Seleziona evento")
    print("9 - Esci")
    scelta = int(input("> "))
    if scelta == 1 and index != 0:
        index -= 1
    elif scelta == 2 and index != len(result)-1:
        index += 1
    elif scelta == 3:
        # TODO seleziona evento
        print("IDK")
    elif scelta == 9:
        break

mongo.close()
print("Adios")
