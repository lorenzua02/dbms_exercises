from stagemodel import Neo4jModel as n4j


neo = n4j("bolt://localhost:7687")

neo.create_node('rifugio', nome='rifugio del dragone', capacita_max=100)
neo.create_node('rifugio', nome='rifugio del peccatore', capacita_max=30)
neo.create_node('rifugio', nome='rifugio del cornuto', capacita_max=69)

p = neo.create_node('partenza', nome='partenza del dragone')
a = neo.create_node('arrivo', nome='arrivo del dragone')
neo.create_link('SENTIERO', 
                origin_id=p, 
                destination_id=a,
                nome='sentiero del dragone', difficolta=8, tempo_percorrenza=3, numero=1)           

p = neo.create_node('partenza', nome='partenza del peccatore')
a = neo.create_node('arrivo', nome='arrivo del peccatore')
neo.create_link('SENTIERO',  
                origin_id=p, 
                destination_id=a,
                nome='sentiero del peccatore',
                difficolta=4, tempo_percorrenza=2, numero=14)

p = neo.create_node('partenza', nome='partenza del cornuto')
a = neo.create_node('arrivo', nome='arrivo del cornuto')
neo.create_link('SENTIERO',  
                origin_id=p, 
                destination_id=a,
                nome='sentiero del cornuto',
                difficolta=3, tempo_percorrenza=0.25, numero=3)

neo.create_node('punto_panoramico', altezza=2000)
neo.create_node('punto_panoramico', altezza=3251)
neo.create_node('punto_panoramico', altezza=503)