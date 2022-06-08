from stagemodel import Neo4jModel
import os
import menu

db = Neo4jModel("bolt://localhost:7687", "", "")
print(f"Cancellati {db.empty_database()} nodi.")
menu.main_menu()
db.close()
