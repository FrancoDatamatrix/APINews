import os
from bson import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient
from .GetUserDB import GetUserDB


class GetNewsByUserDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        # self.user_collection = GetUserDB()

    def get_user_news(self, user_complete, page=1, page_size=1):
        try:

            # Calcular el índice de inicio y fin para la paginación
            start_index = (page - 1) * page_size
            end_index = start_index + page_size

            
            if user_complete:
                user = user_complete["usuario"]
                user_db = self.client[f"{user}_db"]
                news_collection = user_db["news"]
                
            
            # Intentar buscar las noticias del usuario con paginación
            news_cursor = news_collection .find({}).skip(start_index).limit(page_size)
            news = list(news_cursor)

            
            if news:
                return news
            else:
             return {"error": "noticias no encontradas"}
        except InvalidId:
            return {"error": "ID no válido"}
        except Exception as e:
            print(f"Se produjo un error al obtener las noticias: {e}")
            return {"error": "Error al obtener las noticias"}