from stagemodel import Neo4jModel


db = Neo4jModel("bolt://localhost:7687", "", "")
print(f"Cancellati {db.empty_database()} nodi.")

while True:
    print("[1] ...")
    scelta = int(input("> "))
    if scelta == 9:
        break

db.close()
