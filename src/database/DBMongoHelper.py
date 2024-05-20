from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Carga las variables de entorno
load_dotenv()

class DBmongoHelper:
    
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        self.db = self.client["ApiNews"]
        
    def get_collection(self, collection_name):
        return self.db[collection_name]