import time
from db_connection import MongoDBConnection
from mongo_observer import MongoObserver
from pymongo.errors import PyMongoError


def watch_collection_changes(uri, db_name, collection_name):
    """Surveille les changements d'une collection MongoDB."""
    connection = MongoDBConnection(uri, db_name)
    collection = connection.get_collection(collection_name)

    observer = MongoObserver()

    try:
        # Démarrer le Change Stream pour surveiller les événements
        with collection.watch() as stream:
            print(f"Observation de la collection '{collection_name}' en cours...")
            for change in stream:
                observer.update(change)
    except PyMongoError as e:
        print(f"Erreur lors de l'observation : {e}")

if __name__ == "__main__":
    URI = "mongodb://localhost:27017"
    DB_NAME = "my_database"
    COLLECTION_NAME = "my_collection"

    # Lancer l'observation des changements
    watch_collection_changes(URI, DB_NAME, COLLECTION_NAME)
