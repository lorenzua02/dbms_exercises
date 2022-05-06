from pymongo import MongoClient

if __name__ != '__main__':
    raise Exception("Lanciami come programma principale grazie")


mongo = MongoClient('mongodb://localhost:37000/')

print("Sistema di creazione concerti")
while True:
    concerto = {}
    # TODO contorllo input
    data = input("Inserisci data in formato yyyy-mm-dd -> ")
    orario = input("Inserisci orario in formato hh:mm -> ") + ":00"
    luogo = input("Inserisci luogo -> ")

    cantanti = []
    while True:
        cantanti.append(input("Inserisci cantante: "))
        if input("Vuoi inserire un altro cantante? (y/n): ").lower()[0] == "n":
            break

    concerto["posti"] = {}
    tot_posti = 0
    while True:
        tipo = input("Inserisci nome posto (es. platea): ")
        n_posti = int(input("Inserisci numero di posti: "))
        tot_posti += n_posti
        prezzo = float(input("Prezzo per posto: "))
        concerto["posti"][tipo] = {"posti": n_posti, 'prezzo': prezzo}
        if input("Vuoi inserire un altro posto? (y/n): ").lower()[0] == "n":
            break

    concerto["luogo"] = luogo
    concerto["dataora"] = data + " " + orario
    concerto["cantanti"] = cantanti
    concerto["posti_totali"] = tot_posti

    mongo.eventi.concerti.insert_one(concerto)

    if input("Vuoi inserire un altro concerto? (y/n): ").lower()[0] == "n":
        break
