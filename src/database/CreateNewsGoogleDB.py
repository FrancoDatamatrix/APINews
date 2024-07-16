import os
import bcrypt
from bson import ObjectId
from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper
from datetime import datetime
from .GetUserDB import GetUserDB

class CreateNewsDB:
    def __init__(self):
        # Conexión a la base de datos y a la colección de noticias
        self.client = MongoClient(os.getenv("DB_URL"))
        self.user_collection = GetUserDB()
        self.db_admin = DBmongoHelper()
        self.users_collection = self.db_admin.get_collection("users")

    def create_news(self, usuario, tema, palabra, news):
        
            if ObjectId.is_valid(usuario):
                user_oid = ObjectId(usuario)
                userComplete = self.users_collection.find_one({"_id": user_oid})
        
            if userComplete["rol"] == "user":
                user = userComplete["usuario"]
                user_db = self.client[f"{user}_db"]
                news_collection = user_db["news"]
            else:
                news_collection = self.db_admin.get_collection("news")

                
            
            
            
        
        
            # Obtener el timestamp actual
            timestamp = datetime.now()

            # Crear un documento para el modelo de DB
            news_data = {
                "usuario_id": usuario,
                "tema": tema,
                "palabra": palabra,
                "news": news,
                "timestamp": timestamp  # Agregar el campo timestamp al documento
            }

            # Insertar las noticias en la base de datos y devolver su ID
            result = news_collection.insert_one(news_data)
            news_id = str(result.inserted_id)
            return news_id