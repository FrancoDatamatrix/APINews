import bcrypt
from .DBMongoHelper import DBmongoHelper
from datetime import datetime

class CreateNewsDB:
    def __init__(self):
        # Conexión a la base de datos y a la colección de noticias
        self.db_helper = DBmongoHelper()
        self.news_collection = self.db_helper.get_collection("news")

    def create_news(self, news, usuario, palabra):
        # Obtener el timestamp actual
        timestamp = datetime.now()

        # Crear un documento para el modelo de DB
        news_data = {
            "usuario": usuario,
            "palabra": palabra,
            "news": news,
            "timestamp": timestamp  # Agregar el campo timestamp al documento
        }

        # Insertar las noticias en la base de datos y devolver su ID
        result = self.news_collection.insert_one(news_data)
        return result.inserted_id