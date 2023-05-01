from stagemodel import Neo4jModel


def seeder(conn):
    """
    - Professor: name, surname, subject
    - Company: name, desc
    - Student: name, course
    """

    idnodo1 = conn.create_node("P", name="aa", surname="bbb", subject="ccc")
    idnodo2 = conn.create_node("S", name="ddd", course="eee")
    conn.create_link(idnodo1, idnodo2, "LABEL")

    data = [
        ("Marco", "Rossi", "matematica"),
        ("Mario", "Bianchi", "inglese"),
        ("Andrea", "Verdi", "reti"),
        ("Antonio", "Russo", "ML"),
        ("Chiara", "Esposito", "statistica"),
        ("Maria", "Mariani", "AI"),
    ]
    p = []
    for row in data:
        p.append(conn.create_node("P", name=row[0], surname=row[1], subject=row[2]))

    data = [
        ("Luigi", "ML"),
        ("Mario", "ML"),
        ("Martina", "ML"),
        ("Giulia", "ML"),
        ("Edoardp", "ML"),
        ("Francesco", "ML"),
        ("Mattia", "ML"),
        ("Luca", "smart"),
        ("Giuseppe", "smart"),
        ("Franco", "smart"),
        ("Giorgia", "smart"),
        ("Marco", "smart"),
    ]
    s = []
    for row in data:
        s.append(conn.create_node("S", name=row[0], course=row[1]))

    data = [
        ("tesla", "auto"),
        ("atzure", "cloud"),
        ("amazon", "e-commerce"),
        ("ibm", "IT"),
        ("apple", "device"),
    ]
    a = []
    for row in data:
        a.append(conn.create_node("C", name=row[0], desc=row[1]))

    links = [
        (s[0], a[0], "lavora_in"),
        (s[1], a[1], "lavora_in"),
        (s[2], a[2], "lavora_in"),
        (s[3], a[3], "lavora_in"),
        (s[4], a[3], "lavora_in"),
        (s[5], a[0], "lavora_in"),
        (s[6], a[1], "lavora_in"),
        (s[7], a[0], "lavora_in"),

        (p[0], s[0], "insegna_a"),
        (p[0], s[1], "insegna_a"),
        (p[0], s[2], "insegna_a"),
        (p[0], s[3], "insegna_a"),
        (p[0], s[3], "insegna_a"),
        (p[1], s[5], "insegna_a"),
        (p[1], s[6], "insegna_a"),
        (p[2], s[7], "insegna_a"),
        (p[2], s[8], "insegna_a"),
        (p[3], s[8], "insegna_a"),
        (p[3], s[9], "insegna_a"),
        (p[3], s[10], "insegna_a"),
        (p[3], s[11], "insegna_a"),
        (p[4], s[11], "insegna_a"),

        (p[5], a[3], "contatto_in"),
        (p[0], a[0], "contatto_in"),
        (p[0], a[1], "contatto_in"),
        (p[0], a[2], "contatto_in"),
        (p[4], a[3], "contatto_in"),
        (p[4], a[0], "contatto_in"),
        (p[3], a[2], "contatto_in"),
        (p[4], a[2], "contatto_in"),
    ]
    for row in links:
        conn.create_link(row[0], row[1], row[2])


if __name__ == '__main__':
    seeder(conn=Neo4jModel("neo4j://localhost:7687", "", ""))
