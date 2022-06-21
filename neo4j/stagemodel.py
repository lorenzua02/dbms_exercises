from neo4j import GraphDatabase


class Neo4jModel:

    def __init__(self, uri, username="", password=""):
        self.driver = GraphDatabase.driver(uri, auth=(username, password))
        print(f"Collegato al database {uri}")

    @staticmethod
    def __return_str_check(a):
        return "true" if a else "false"

    def ristruttura_dict(self, d: dict):
        res = "{ "
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
        """
        - Professor: name, surname, subject
        - Company: name, desc
        - Student: name, course
        """
        diz = self.ristruttura_dict(parms)
        with self.driver.session() as session:
            # non vanno entrambe le righe sottostanti
            id_nodo = session.run(
                f"CREATE (n:{label} " + diz + ") RETURN id(n)").data()[0]['id(n)']
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

    def delete_node(self, node_id):
        with self.driver.session() as session:
            session.run(f"""MATCH (n)
                        WHERE id(n) = {node_id}
                        DELETE n""")
            print('nodo eliminato con successo')
    # lollo funziona secondo te? (y/n)

    def empty_database(self):
        with self.driver.session() as session:
            return session.run("match (n) detach delete n return count(n)").single()[0]


class Scuola(Neo4jModel):

    def __init__(self, uri, username="", password=""):
        super().__init__(uri, username, password)
    # cercare il miglior prof che può fungere da collegamento con l'azienda

    def best_prof(self, id_azienda):
        '''
        dovremmo trovare il prof che ha più alunni in modo tale da dire che:
        l'azienda ha trovato il prof con il maggior numero di possibili dipendenti

        qwerry 1 (trovare i prof connessi all'azienda) --> list[id(prof)]
            # qwerry 1.1 (trovare gli alunni di ogni prof) 
            # qwerry 1.2 (trovare gli alunni che lavorano nell'azienda) 
        qwerry 2 (trovare gli alunni in comune tra azienda e prof) 
        il primo risultato e' il prof con piu' alunni nell'azienda 

        '''
        with self.driver.session() as session:
            """MATCH (p: P)-[:INSEGNA_A]->(s:S), (p)-[:CONTATTO_IN]->(a:C) 
                    
                        WHERE (s)-[:LAVORA_IN]->(a) 
                        AND id(a) = 74
                        RETURN p
                        LIMIT 1"""
            return session.run(f"""
                        MATCH (p: P)-[:INSEGNA_A]->(s:S), (p)-[:CONTATTO_IN]->(a:C)
                        WHERE (s)-[:LAVORA_IN]->(a)
                        AND id(a) = {id_azienda}
                        RETURN p
                        LIMIT 3""").data()


class Montagna(Neo4jModel):

    def __init__(self, uri, username="", password=""):
        super().__init__(uri, username, password)

    # proporre il percorso entro distanze definite per un certo numero di persone.
    # Es "percorso tra 24h e 48h per 5 persone e 1 rifugio"
    # 15 minuti == 0.25 -- 1 ora == 1
    def best_track(self, n_persone, ora_min, ora_max):
        assert type(ora_min) == int and type(ora_max) == int
        with self.driver.session() as session:
            """
            MATCH percorso=(p:partenza)-[:SENTIERO*]-(a:arrivo)
            return 
            reduce(tempo=0, tratta in relationships(percorso) | tempo + tratta.tempo_percorrenza) as tempototale,
            reduce(rifugi=0, rifugio in nodes(percorso) | {if {n_persone} <= rifugio.capacita_max} rifugi + 1) as rifugitot,
            reduce(puntipanoramici=0, puntopanoramico in nodes(percorso) | puntipanoramici + 1) as puntipanoramicitot
            order by tempototale desc
            WHERE {ora_min} < tempototale < {ora_max}
            limit 3
            """


if __name__ == "__main__":
    model = Neo4jModel("bolt://localhost:7687")
    # id_nodo = model.create_node(label="S", name="maio",course="ML")
    # print(model.return_node(id_nodo, "S"))
    model.empty_database()

    model.create_node(label="S", name="aaa", course="aa")

    id_nodo = model.create_node(label="S", name="lollo", course="MLa")
    # print(id_nodo)
    print(model.return_node(label="S"))
    #print(Neo4jModel("bolt://localhost:7687").return_node(label= 'rifugio').data())
    # for n in Neo4jModel("bolt://localhost:7687").return_node(label= 'rifugio'):
    #     print(n)