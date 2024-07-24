import os
import logging
from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId
from .GetUserDB import GetUserDB

class GetFilteredNewsDB:
    def __init__(self):
        self.db_admin = DBmongoHelper()
        self.users_collection = self.db_admin.get_collection("users")
        self.client = MongoClient(os.getenv("DB_URL"))
        self.user_collection = GetUserDB()

    def get_filtered_news(self, tema=None, usuario_id=None, page=1, page_size=1, sort_by='timestamp', sort_order=-1):
                
        try:
            
            # Inicializar la variable news
            news = []
            has_more = False
            
            # Construir el filtro de búsqueda
            filter_criteria = {}
            if tema:
               filter_criteria["tema"] = {"$regex": tema, "$options": "i"}
            if usuario_id:
                user_oid = ObjectId(usuario_id)
                filter_criteria['usuario_id'] = user_oid
                

            # Calcular el índice de inicio para la paginación
            start_index = (page - 1) * page_size
        
            if ObjectId.is_valid(usuario_id):
                user_oid = ObjectId(usuario_id)
                userComplete = self.users_collection.find_one({"_id": user_oid})
                user = userComplete["usuario"]
                user_db = self.client[f"{user}_db"]
                news_collection = user_db["news"]
                
                # Traer las noticias paginadas de la base de datos
                news_cursor = news_collection.find(filter_criteria).sort(sort_by, sort_order).skip(start_index).limit(page_size)
                news = list(news_cursor)
            
            else:
                databases = self.client.list_database_names()
            
                # Recorrer cada base de datos y # Traer las noticias paginadas de la base de datos
                for db_name in databases:
                    db = self.client[db_name]
                    if "news" in db.list_collection_names():
                        news_collection = db["news"]
                        searchNews = list(news_collection.find(filter_criteria).sort(sort_by, sort_order).skip(start_index).limit(page_size))
                        news.extend(searchNews)
                    
                    
            

            
            
        except Exception as e:
            # Manejar excepciones específicas si es necesario
            print(f"Se produjo un error al obtener las noticias: {e}")
        finally:
            # Cerrar la conexión después de obtener los datos
            self.client.close()

        return news