Durante gli studi, ho realizzato piccoli progetti con i miei compagni di corso per allenarci ad utilizzare i database che studiavamo man mano.

# Redis
Realizzazione applicazione Python che usando Redis gestisce le proposte in un condominio.

Il programma deve:
- Permettere l'inserimento di una proposta (titolo, descrizione, proponente)
- Fare votare all'utente le proposte che preferisce (limite 1 voto ad utente per proposta)
- Stampare la proposta vincente (quella/e con più voti)
- Permettere di resettare tutto il database

# MongoDB
Realizzazione applicazione Python che usando MongoDB simuli un gestionale di concerti.

Il programma deve:
- Permettere l'inserimento di un concerto (numero posti, data, luogo, cantanti)
- Permettere all'utente di cercare un concerto con criteri personalizzati come distanza e cantanti
- Simulare l'acquisto di un biglietto

Per faciltare il testing è stato creato un seeder: un piccolo script che genera dati di concerti casuali

# Neo4j
Realizzazione applicazione Python che usando Neo4j gestisca gli stage curriculari della scuola.

L'applicativo risolve il problema di "trovare il docente meglio informato sull'azienda x", ovvero quel professore che ha avuto il maggior numero di studenti che hanno lavorato nell'azienda data in input.

Il sistema crea/cancella nodi e relazioni e ricerca il miglior professore.

Abbiamo previsto un seeder che importa dei "dummy data" per facilitare il testing
