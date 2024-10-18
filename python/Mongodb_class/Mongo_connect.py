from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class MongoDBConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(MongoDBConnection, cls).__new__(cls)
            cls._instance.initialize(*args, **kwargs)
        return cls._instance

    def initialize(self, uri, db_name):
        try:
            self.client = MongoClient(uri)
            self.db = self.client[db_name]
            # Vérifier la connexion
            self.client.admin.command('ping')
            print("MongoDB connection established.")
        except ConnectionFailure as e:
            print(f"Failed to connect to MongoDB: {e}")

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def close_connection(self):
        self.client.close()
        print("MongoDB connection closed.")