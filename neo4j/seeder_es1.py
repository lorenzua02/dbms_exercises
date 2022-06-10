from stagemodel import Neo4jModel as n4j


neo = n4j("bolt://localhost:7687")

neo.create_node()

