from pymongo import MongoClient
from dotenv import load_dotenv
from flask import g
from flask_jwt_extended import get_jwt_identity
import os
import logging

# Carga las variables de entorno
load_dotenv()

class DBmongoHelper:
    
    def __init__(self, db_name="ApiNews"):
        self.client = MongoClient(os.getenv("DB_URL"))
        self.db = self.client[db_name]
        
    def get_collection(self, collection_name):
        return self.db[collection_name]
    
    def close(self):
        self.client.close()
        
# def set_user_db(current_user):
#         db_name = f"{current_user}_db"
#         g.db_helper = DBmongoHelper(db_name)