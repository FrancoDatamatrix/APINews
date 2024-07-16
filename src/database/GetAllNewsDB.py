import os
from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper

class GetAllNewsDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        # self.news_collection = self.db_helper.get_collection("news")

    def get_all_news(self, page=1, page_size=1):
        
        # Obtener todas las bases de datos
        databases = self.client.list_database_names()
        
        # Inicializar la variable news
        news = []

        try:
            # Calcular el índice de inicio y fin para la paginación
            start_index = (page - 1) * page_size
            end_index = start_index + page_size

            print(f"Start Index: {start_index}, End Index: {end_index}")
            
            # Recorrer cada base de datos y obtener la colección "news"
            for db_name in databases:
                db = self.client[db_name]
                if "news" in db.list_collection_names():
                    news_collection = db["news"]
                    news_cursor = list(news_collection.find({}).skip(start_index).limit(page_size))
                    news.extend(news_cursor)
                    
                    
            # Traer las noticias paginadas de la base de datos
            # news_cursor = self.news_collection.find({}).skip(start_index).limit(page_size)
            # news = list(news_cursor)
        except Exception as e:
            # Manejar excepciones específicas si es necesario
            print(f"Se produjo un error al obtener las noticias: {e}")
        finally:
            # Cerrar la conexión después de obtener los datos
            self.client.close()
            if len(news) == 0:
                return {"msg": "No se encontraron mas Noticias"}
        return news