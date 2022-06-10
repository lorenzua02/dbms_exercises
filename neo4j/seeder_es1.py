from stagemodel import Neo4jModel as n4j


neo = n4j("bolt://localhost:7687")

neo.create_node('rifugio', nome = 'rifugio del dragone', capacita_max = 100)
neo.create_node('rifugio', nome = 'rifugio del peccatore', capacita_max = 30)
neo.create_node('rifugio', nome = 'rifugio del cornuto', capacita_max = 69)

neo.create_node('partenza', nome = 'sentiero del dragone')
neo.create_link('SENTIERO', nome = 'sentiero del dragone', difficolta = 8, tempo_percorrenza = '3H', numero = 1)
neo.create_node('arrivo', nome = 'sentiero del dragone')

neo.create_node('partenza', nome = 'sentiero del peccatore')
neo.create_link('SENTIERO', nome = 'sentiero del peccatore', difficolta = 4, tempo_percorrenza = '2H', numero = 14)
neo.create_node('arrivo', nome = 'sentiero del peccatore')

neo.create_node('partenza', nome = 'sentiero del cornuto')
neo.create_link('SENTIERO', nome = 'sentiero del cornuto', difficolta = 3, tempo_percorrenza = '15M', numero = 3)
neo.create_node('arrivo', nome = 'sentiero del cornuto')

neo.create_node('punto_panoramico', altezza = 2000)
neo.create_node('punto_panoramico', altezza = 3251)
neo.create_node('punto_panoramico', altezza = 503)
