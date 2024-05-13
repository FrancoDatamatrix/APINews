from pymongo import MongoClient
from dotenv import load_dotenv
import os

#Carga las variables de entorno
load_dotenv()

class DBmongoHelper:
    
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        self.db = self.client[os.getenv("DB_NAME")]
        
    def get_collection(self, collection_name):
    #Obtiene una colección específica de la base de datos.
        return self.db[collection_name]



