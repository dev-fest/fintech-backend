from pymongo import MongoClient
from threading import Lock
import certifi

class MongoDBConnection:
    """Singleton for managing MongoDB connection."""
    _instance = None
    _lock = Lock()

    def __new__(cls, uri, db_name):
        with cls._lock:
            if not cls._instance:
                cls._instance = super(MongoDBConnection, cls).__new__(cls)
                # use the SSL certificate
                cls._instance.client = MongoClient(uri, tls=True, tlsCAFile=certifi.where())
                cls._instance.db = cls._instance.client[db_name]
        return cls._instance

    def get_collection(self, collection_name):
        """Retrieve a collection from the database."""
        return self.db[collection_name]




