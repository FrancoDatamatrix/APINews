import os
import string
import random
from pymongo import MongoClient
from flask import jsonify
from werkzeug.security import generate_password_hash

class CreateDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))    

    def create_db(self, user_data):
        db_name = f"{user_data['usuario']}_db"
        db = self.client[db_name]
        
        db_username, db_password = generate_credentials()
    
        db.command("createUser", db_username, pwd=db_password, roles=[{"role": "readWrite", "db": db_name}])

        
        response = {
            "db_name": db_name,
            "db_username": db_username,
            "db_password": db_password
        }
        
        self.client.close()
        
        return response


def generate_credentials():
        username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        return username, password