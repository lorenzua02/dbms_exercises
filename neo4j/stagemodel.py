import json

from neo4j import GraphDatabase
import traceback


class Neo4jModel:
    
    def __init__(self, uri, username="", password=""):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        print(f"Collegato al database {uri}")

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
        diz = json.dumps(parms)
        with self.driver.session() as session:
            # non vanno entrambe le righe sottostanti 
            id_nodo = session.run(f"CREATE (n:{label}" + "{nome:'luca'}) RETURN id(n)", label=label)
            
            id_nodo = session.run(f"CREATE (n:{label} " + diz + ") RETURN id(n)", label=label)
            id_nodo = session.run("CREATE (n:$label " + diz + ") RETURN id(n)", label=label)

        return id_nodo

    def create_link(self, origin_id, destination_id, label, **parms):
        diz = json.dumps(parms)
        with self.driver.session() as session:
            session.run(f"""MATCH (a),(b)
                        WHERE id(a) = $origin_id and id(b) = $destination_id
                        CREATE (a)-[r:$label {diz}]->(b)""", 
                        origin_id=origin_id, 
                        label=label, 
                        destination_id=destination_id)
   
    def return_node(self, node_id=None, label=None):
        # TODO prevedere la return per parametri dei nodi 
        
        if label:
            with self.driver.session() as session:
                return session.run(f"""MATCH (n: {label}) RETURN n""")
        
        with self.driver.session() as session:
            return session.run("""MATCH (n)
                        WHERE id(n) = $node_id
                        RETURN n""", node_id=node_id)
        
        return None

    def return_label(self, node_id):
        with self.driver.session() as session:
            return session.run("""MATCH (n)
                        WHERE id(n) = $node_id
                        RETURN labels(n)""", node_id=node_id)
    
    def empty_database(self):
        with self.driver.session() as session:
            return session.run("match (n) detach delete n return count(n)").single()[0]

if __name__ == "__main__":
    print(Neo4jModel("bolt://localhost:7687").return_node(label= 'rifugio'))