from bson import ObjectId
from bson.errors import InvalidId
from .DBMongoHelper import DBmongoHelper

class GetNewsDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.news_collection = self.db_helper.get_collection("news")

    def get_news(self, identifier):
        # Intentar buscar la noticia por ObjectId (ID)
        try:
            news_oid = ObjectId(identifier)
            news = self.news_collection.find_one({"_id": news_oid})
            if news:
                return news
            else:
                return {"error": "Noticias no encontradas"}
        except InvalidId:
            return {"error": "ID no válido"}
        except Exception as e:
            print(f"Se produjo un error al obtener las noticias: {e}")
            return {"error": "Error al obtener las noticias"}
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()