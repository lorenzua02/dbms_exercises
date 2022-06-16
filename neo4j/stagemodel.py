import json
from platform import node

from neo4j import GraphDatabase
import traceback


class Neo4jModel:
    
    def __init__(self, uri, username="", password=""):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        print(f"Collegato al database {uri}")

    @staticmethod
    def __return_str_check(a):
        return "true" if a else "false"

    def ristruttura_dict(self, d: dict):

        res = "{"
        for x in d.keys():
            if type(d[x]) == str:
                res += f"{x}: \"{d[x]}\""
            elif type(d[x]) == bool:
                res += f"{x}: {self.__return_str_check(d[x])}"
            else:
                res += f"{x}: {d[x]}"
            res += ","
        res = res[:-1]
        res += "}"
        return res

    def close(self):
        if self.driver:
            self.driver.close()
            print(f"Scollegato dal database {self.driver}.")

    def create_node(self, label, **parms):
        # TODO generalizzazione n label (parm "label" -> array)
        """
        - Professor: name, surname, subject
        - Company: name, desc
        - Student: name, course
        """
        diz = self.ristruttura_dict(parms)
        with self.driver.session() as session:
            # non vanno entrambe le righe sottostanti 
            id_nodo = session.run(f"CREATE (n:{label} " + diz + ") RETURN id(n)").data()[0]['id(n)']
        print('Nodo creato correttamente')
        return id_nodo

    def get_id(self, label, **parms):
        diz = self.ristruttura_dict(parms)
        with self.driver.session() as session:
            return session.run(f"MATCH (n:{label} " + diz + ") RETURN id(n)").data()[0]['id(n)']

    def create_link(self, origin_id, destination_id, label, **parms):
        label = label.upper()
        diz = self.ristruttura_dict(parms)
        with self.driver.session() as session:
            session.run(f"""MATCH (a),(b)
                        WHERE id(a) = {origin_id} and id(b) = {destination_id}
                        CREATE (a)-[:{label} {diz}]->(b)""").data()
   
    def return_node(self, node_id=None, label=None):
        # TODO prevedere la return per parametri dei nodi 

        if label:
            with self.driver.session() as session:
                return session.run(f"MATCH (n: {label}) RETURN n").data()

        with self.driver.session() as session:
            return session.run(f"MATCH (n) WHERE id(n) = {node_id} RETURN n").data()
        

    def return_label(self, node_id):
        with self.driver.session() as session:
            return session.run(f"""MATCH (n)
                        WHERE id(n) = {node_id}
                        RETURN labels(n)""").data()
    
    def empty_database(self):
        with self.driver.session() as session:
            return session.run("match (n) detach delete n return count(n)").single()[0]

if __name__ == "__main__":
    model = Neo4jModel("bolt://localhost:7687")
    # id_nodo = model.create_node(label="S", name="maio",course="ML")
    # print(model.return_node(id_nodo, "S"))
    model.empty_database()

    model.create_node(label="S", name="aaa",course="aa")
    
    id_nodo = model.create_node(label="S", name="lollo",course="MLa")
    #print(id_nodo)
    print(model.return_node(label="S"))
    #print(Neo4jModel("bolt://localhost:7687").return_node(label= 'rifugio').data())
    # for n in Neo4jModel("bolt://localhost:7687").return_node(label= 'rifugio'):
    #     print(n)

    
