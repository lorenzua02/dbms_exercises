# Lorenzo Mogicato
# Simone Daniele
# Matias Maiorano

import urllib.request
import json
from pymongo import MongoClient
import datetime

if __name__ != '__main__':
    raise Exception("Lanciami come programma principale grazie")


# TODO prenderla da json esterno in .gitignore
apikey = "&appid=790103a2a81e03e9dd13ec518a5a1690"
url = "http://api.openweathermap.org/geo/1.0/direct?q="

citta = input("Inserisci il nome di una citta \n")
if input("vuoi cercare in italia? (y/n)\n").lower()[0] == "y":
    citta += ",it"

response = urllib.request.urlopen(url + citta + apikey)
data_json = json.loads(response.read())
lat = data_json[0]["lat"]
lon = data_json[0]["lon"]


def print_evento(e):
    print("Data:", e['dataora'])
    print("Luogo:", e['luogo'])
    print("Distanza:", round(e['distance'], 2), "km")
    cantanti = e['cantanti']
    print("Cantante/i:", cantanti[0], end='')
    for cantante in cantanti[1:]:
        print(", " + cantante, end='')
    print("\nPosti rimanenti:", e['posti_totali'])


def acquista(e, tipo_posto, quantity=1, interrupt_after_purchase=True):
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
            if quantita > e["posti"][scelte[decisione]]["posti"]:
                print("Troppi posti selezionati")
                input("Premi un tasto per continuare\n>")
            break
        except e:
            print("Input invalido")
            input("Premi un tasto per continuare\n>")
            # continue
    acquista(e, scelte[decisione], quantita)


mongo = MongoClient('mongodb://localhost:37000/')
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
req = input("Inserisci nome artista: ").capitalize()
max_distance_km = 50

aggregate = [
    {
        '$geoNear': {
            'near': {
                'type': 'Point',
                'coordinates': [lon, lat]
            },
            'distanceField': 'distance',
            'distanceMultiplier': 0.001
        }
    }, {
        '$match': {
            '$and': [
                {'cantanti': {'$in': [req]}},
                {'dataora': {'$gt': now}},
                {'posti_totali': {'$gt': 0}},
                {'distance': {"lt": max_distance_km}}
            ]
        }
    }
]

index = 0

while True:
    result = list(mongo.eventi.concerti.aggregate(pipeline=aggregate))
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
