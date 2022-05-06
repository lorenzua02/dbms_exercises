import random
import json


def crea(file, n_elementi):
    lst = []
    for x in range(n_elementi):
        cantanti = [
            "Tiziano Ferro",
            "Vasco Rossi",
            "883",
            "Jovanotti",
            "Paky",
            "Tedua",
            "Laura Pausini",
            "Simone Panetti",
            "I Mates",
            "Maneskin",
            "Bresh",
            "Disme",
            "Vaz Te",
            "Ghali",
            "Massimo Pericolo",
            "Izi",
            "Salmo",
            "Sfera Ebbasta",
            "Rkomi",
            "Lazza",
            "Gue",
        ]

        stadio = ["vip", "anello1", "anello2", "prato"]
        galleria = ["platea", "vip", "sopra"]
        np_galleria = random.randint(200, 500)
        np_stadio = random.randint(2000, 5000)
        luoghi = [stadio, galleria]

        luogo = luoghi[random.randint(0, 1)]

        if luogo == ["vip", "anello1", "anello2", "prato"]:  # stadio
            pos = "stadio"
            vip = np_stadio // 100 * 10
            anello1 = np_stadio // 100 * 25
            anello2 = np_stadio // 100 * 25
            prato = np_stadio - vip - anello1 - anello2
            posti = [vip, anello1, anello2, prato]
            prezzo = []
            r = random.randint(5, 10)
            prezzo.append(r)
            prezzo.append(r+10)
            prezzo.append(r+10)
            prezzo.append(r+20)

        else:
            pos = "galleria"
            vip = np_galleria // 100 * 10
            platea = np_galleria // 100 * 20
            sopra = np_galleria - vip - platea
            posti = [platea, vip, sopra]
            prezzo = []
            r = random.randint(5, 10)
            prezzo.append(r + 10)
            prezzo.append(r + 20)
            prezzo.append(r)

        posti_totali = sum(posti)

        dict_posti = {}
        if pos == "stadio":
            for x in range(len(posti)):
                dict_posti.update({stadio[x]: {"posti":posti[x],"prezzo": prezzo[x]}})
        if pos == "galleria":
            for x in range(len(posti)):
                dict_posti.update({galleria[x]: {"posti":posti[x],"prezzo": prezzo[x]}})

        # __________________________________________

        giorno = str(random.randint(1, 28)).rjust(2, "0")
        mese = str(random.randint(1, 12)).rjust(2, "0")
        anno = str(random.randint(2021, 2023))
        ora = str(random.randint(0, 23)).rjust(2, "0")
        resto_ = ":00:00"

        data = anno+"-"+mese+"-"+giorno+" "+ora+resto_

        Luoghi = ["Casa di mia nonna",
                  "Inferno",
                  "San Siro",
                  "Paradiso",
                  "Teatro della Scala",
                  "Oratorio di Desio",
                  "Zurich",
                  "Casa di Bossetti",
                  "Gardaland",
                  "ITSAR, Aula P2",
                  "ITSAR, Ufficio di Alex"]

        structure = {
            # "_id": "autogenerato",
            "cantanti":
                random.sample(cantanti, random.randint(1, 3)),
            "posti_totali": posti_totali,
            "posti": dict_posti,
            "dataora": data,
            "luogo": "".join(random.sample(Luoghi, 1))
        }

        lst.append(structure)

    json.dump(lst, open(file, "w", encoding="utf-8"), indent=4)

    pass


if __name__ == "__main__":
    crea("concerti.json", 200)
