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
            prezzo.append(r + 10)
            prezzo.append(r + 10)
            prezzo.append(r + 20)

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
                dict_posti.update({stadio[x]: {"posti": posti[x], "prezzo": prezzo[x]}})
        if pos == "galleria":
            for x in range(len(posti)):
                dict_posti.update({galleria[x]: {"posti": posti[x], "prezzo": prezzo[x]}})

        giorno = str(random.randint(1, 28)).rjust(2, "0")
        mese = str(random.randint(1, 12)).rjust(2, "0")
        anno = str(random.randint(2021, 2023))
        ora = str(random.randint(0, 23)).rjust(2, "0") + ":00:00"

        data = anno + "-" + mese + "-" + giorno + " " + ora

        # TODO spostare in json a parte
        coords = [{
            "luogo": "Milano",
            "geometry": {
                "type": "Point",
                "coordinates": [
                    9.189033508300781,
                    45.46639130966522
                ]
            }
        },
            {
                "luogo": "Torino",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        7.6827049255371085,
                        45.06845915250033
                    ]
                }
            }, {
                "luogo": "Genova",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        8.933730125427246,
                        44.407082710908114
                    ]
                }
            }, {
                "luogo": "Palermo",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        13.352680206298826,
                        38.111042007788946
                    ]
                }
            }, {
                "luogo": "Roma",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        12.492485046386719,
                        41.89037781786264
                    ]
                }
            }, {
                "luogo": "Firenze",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        11.248047351837158,
                        43.765081538935185
                    ]
                }
            }, {
                "luogo": "Venezia",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        12.33241081237793,
                        45.424570085365076
                    ]
                }
            },
            {
                "luogo": "Perugia",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        12.387900352478026,
                        43.11030422857738
                    ]
                }
            },
            {
                "luogo": "Napoli",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        14.246971607208252,
                        40.8338138590956
                    ]
                }
            }, {
                "luogo": "Bologna",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        11.343238949775696,
                        44.49366989761399
                    ]
                }
            },
            {
                "luogo": "Trieste",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        13.7672,
                        45.6480
                    ]
                }
            }
        ]

        structure = {
            "cantanti": random.sample(cantanti, random.randint(1, 3)),
            "posti_totali": posti_totali,
            "posti": dict_posti,
            "dataora": data
        }

        structure.update(coords[random.randint(0, len(coords) - 1)])
        lst.append(structure)

    json.dump(lst, open(file, "w", encoding="utf-8"), indent=4)


if __name__ == "__main__":
    crea("concerti.json", 200)
