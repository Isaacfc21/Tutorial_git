from pymongo import MongoClient
from .mongo_db_configs import mongo_db_infos

class DBConnectionHandler:
    def __init__(self) -> None:
        self._connection_string = 'mongodb://localhost:27017/'
        self._database_name = mongo_db_infos["DB_NAME"]
        self._client = None
        self._db_connection = None
        
    def connect_to_db(self):
        self._client = MongoClient(self._connection_string)
        self._db_connection = self._client[self._database_name]
        
    def get_db_connection(self):
        return self._db_connection

    def get_db_client(self):
        return self._client
