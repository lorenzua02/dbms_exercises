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

    def create_node(self, label, **kargs):
        """
        - Professor: name, surname, subject
        - Company: name, desc
        - Student: name, course
        """
        assert label in ['S', 'P', 'C']
        # TODO controllo kargs in funziona alla label
        # query = CREATE(n:$label {tutti i kargs}) RETURN n
        # return id di n

    def create_link(self, origin_id, destination_id, label):
        with self.driver.session() as session:
            session.run("...")

    def empty_database(self):
        with self.driver.session() as session:
            return session.run("match (n) detach delete n return count(n)").single()[0]
