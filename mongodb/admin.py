from pymongo import MongoClient
import urllib.request
import json


mongo = MongoClient('mongodb://localhost:37000/')
apikey = "&appid=790103a2a81e03e9dd13ec518a5a1690"  # TODO .env
url = "http://api.openweathermap.org/geo/1.0/direct?q="

if __name__ == '__main__':
    citta = input("Inserisci il nome di una citta: ")
    search_in_italy = input("Vuoi cercare in italia? (y/n): ")
    if search_in_italy.lower()[0]=="y":
        citta += ",it"

    response = urllib.request.urlopen(url + citta + apikey)  # TODO params={} do not build the str
    data_json = json.loads(response.read())
    lat = f"&lat={data_json[0]['lat']}"
    lon = f"&lon={data_json[0]['lon']}"

    print("Sistema di creazione concerti")
    while True:
        concerto = {}
        # TODO controllo input
        data = input("Inserisci data in formato yyyy-mm-dd -> ")
        orario = input("Inserisci orario in formato hh:mm -> ") + ":00"
        luogo = input("Inserisci luogo -> ")

        cantanti = []
        while True:
            cantanti.append(input("Inserisci cantante: "))
            add_more = input("Vuoi inserire un altro cantante? (y/n): ")
            if add_more.lower()[0] == "n":
                break

        concerto["posti"] = {}
        tot_posti = 0
        while True:
            tipo = input("Inserisci nome posto (es. platea): ")
            n_posti = int(input("Inserisci numero di posti: "))
            tot_posti += n_posti
            prezzo = float(input("Prezzo per posto: "))
            concerto["posti"][tipo] = {"posti": n_posti, 'prezzo': prezzo}
            add_more = input("Vuoi inserire un altro posto? (y/n): ")
            if add_more.lower()[0] == "n":
                break

        concerto["luogo"] = luogo
        concerto["dataora"] = data + " " + orario
        concerto["cantanti"] = cantanti
        concerto["posti_totali"] = tot_posti

        mongo.eventi.concerti.insert_one(concerto)

        add_more = input("Vuoi inserire un altro concerto? (y/n): ")
        if add_more.lower()[0] == "n":
            break
