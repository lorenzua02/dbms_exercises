import redis

scelta = None
redis = redis.Redis(host='localhost', port=6884, db=0, charset='utf-8', decode_responses=True)

if not redis.ping():
    raise "Errore connessione redis"

if not redis.exists("nextp"):
    redis.set("nextp", 0)

# print("Chiavi finora: ", end="")
# print(redis.keys())

while True:
    print("1 - Creazione proposta")
    print("2 - Vota proposta")
    print("3 - Esito votazione")
    print("4 - Reset")
    print("5 - Esci")
    try:
        scelta = int(input("> "))
    except ValueError:
        pass

    if scelta == 1:
        key = "pr:"+redis.get("nextp")
        redis.incr("nextp")

        proponente = input("Proponente: ")
        redis.hset(key, "proponente", proponente)

        titolo = input("Titolo: ")
        redis.hset(key, "titolo", titolo)

        descrizione = input("Descrizione: ")
        redis.hset(key, "descrizione", descrizione)

        redis.zadd("classifica", {key: 0})
    elif scelta == 2:
        idutente = int(input("Inserisci il tuo id utente: "))
        proposta = input("Inserisci proposta da votare")
        if not redis.exists("pr:"+proposta):
            raise "errore, la proposta non esiste"

        print(redis.smembers("votanti:pr:"+proposta))
        print(f"'{idutente}'")
        if redis.sismember("votanti:pr:"+proposta, idutente):
            raise "L'utente ha già votato questa proposta"

        redis.sadd("votanti:pr:"+proposta, idutente)
        redis.zincrby("classifica", 1, "pr:"+proposta)
    elif scelta == 3:
        classifica = redis.zrange("classifica", 0, -1, desc=True, withscores=True)
        # print(classifica)

        punti_primo = int(classifica[0][1])
        print("Ecco la classifica vincitore/i con", punti_primo, "pnt")
        for i in range(len(classifica)):
            if classifica[i][1] == punti_primo:
                print(classifica[i][0], "dal titolo:", redis.hget("pr:"+str(i), "titolo"))
    elif scelta == 4:
        redis.flushall()
    elif scelta == 5:
        break
    else:
        print("Errore, per uscire premi 5")
