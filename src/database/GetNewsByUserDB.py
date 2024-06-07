from bson import ObjectId
from bson.errors import InvalidId
from .DBMongoHelper import DBmongoHelper

class GetNewsByUserDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.news_collection = self.db_helper.get_collection("news")

    def get_user_news(self, identifier, page=1, page_size=5):
        try:
            # Convertir el identificador a ObjectId
            user_oid = ObjectId(identifier)

            # Calcular el índice de inicio y fin para la paginación
            start_index = (page - 1) * page_size
            end_index = start_index + page_size

            # Intentar buscar las noticias por usuario (ID) con paginación
            news_cursor = self.news_collection.find({"usuario_id": user_oid}).skip(start_index).limit(page_size)
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