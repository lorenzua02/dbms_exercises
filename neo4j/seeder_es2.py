from stagemodel import Neo4jModel


def seeder(obj):
    """
    - Professor: name, surname, subject
    - Company: name, desc
    - Student: name, course
    """

    idnodo1 = obj.create_node("P", name="aa", surname="bbb", subject="ccc")
    idnodo2 = obj.create_node("S", name="ddd", course="eee")

    obj.create_link(idnodo1, idnodo2, "LABEL")

    p1 = obj.create_node("P", name="Marco", surname="Rossi", subject="matematica")
    p2 = obj.create_node("P", name="Mario", surname="Bianchi", subject="inglese")
    p3 = obj.create_node("P", name="Andrea", surname="Verdi", subject="reti")
    p4 = obj.create_node("P", name="Antonio", surname="Russo", subject="ML")
    p5 = obj.create_node("P", name="Chiara", surname="Esposito", subject="statistica")
    p6 = obj.create_node("P", name="Maria", surname="Mariani", subject="AI")

    s1 = obj.create_node("S", name="Luigi", course="ML")
    s2 = obj.create_node("S", name="Mario", course="ML")
    s3 = obj.create_node("S", name="Martina", course="ML")
    s4 = obj.create_node("S", name="Giulia", course="ML")
    s5 = obj.create_node("S", name="Edoardp", course="ML")
    s6 = obj.create_node("S", name="Francesco", course="ML")
    s7 = obj.create_node("S", name="Mattia", course="ML")
    s8 = obj.create_node("S", name="Luca", course="smart")
    s9 = obj.create_node("S", name="Giuseppe", course="smart")
    s10 = obj.create_node("S", name="Franco", course="smart")
    s11 = obj.create_node("S", name="Giorgia", course="smart")
    s12 = obj.create_node("S", name="Marco", course="smart")

    a1 = obj.create_node("C", name="tesla", desc="auto")
    a2 = obj.create_node("C", name="atzure", desc="cloud")
    a3 = obj.create_node("C", name="amazon", desc="e-commerce")
    a4 = obj.create_node("C", name="ibm", desc="IT")
    a5 = obj.create_node("C", name="apple", desc="device")

    obj.create_link( s1, a1, "lavora_in")
    obj.create_link( s2, a2, "lavora_in")
    obj.create_link( s3, a3, "lavora_in")
    obj.create_link( s4, a4, "lavora_in")
    obj.create_link( s5, a4, "lavora_in")
    obj.create_link( s6, a1, "lavora_in")
    obj.create_link( s7, a2, "lavora_in")
    obj.create_link( s8, a1, "lavora_in")

    obj.create_link( p1, s1, "insegna_a")
    obj.create_link( p1, s2, "insegna_a")
    obj.create_link( p1, s3, "insegna_a")
    obj.create_link( p1, s4, "insegna_a")
    obj.create_link( p1, s5, "insegna_a")
    obj.create_link( p2, s6, "insegna_a")
    obj.create_link( p2, s7, "insegna_a")
    obj.create_link( p3, s8, "insegna_a")
    obj.create_link( p3, s9, "insegna_a")
    obj.create_link( p4, s9, "insegna_a")
    obj.create_link( p4, s10, "insegna_a")
    obj.create_link( p4, s11, "insegna_a")
    obj.create_link( p4, s12, "insegna_a")
    obj.create_link( p5, s12, "insegna_a")

    obj.create_link(p6, a5, "contatto_in")
    obj.create_link(p1, a1, "contatto_in")
    obj.create_link(p1, a2, "contatto_in")
    obj.create_link(p1, a3, "contatto_in")
    obj.create_link(p5, a4, "contatto_in")
    obj.create_link(p5, a1, "contatto_in")
    obj.create_link(p4, a3, "contatto_in")
    obj.create_link(p5, a3, "contatto_in")


if __name__ == '__main__':
    seeder(obj = Neo4jModel("neo4j://localhost:7687", "", ""))
