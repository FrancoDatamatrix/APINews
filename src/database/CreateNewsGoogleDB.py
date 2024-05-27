import bcrypt
from .DBMongoHelper import DBmongoHelper
from datetime import datetime

class CreateNewsDB:
    def __init__(self):
        # Conexión a la base de datos y a la colección de noticias
        self.db_helper = DBmongoHelper()
        self.news_collection = self.db_helper.get_collection("news")

    def create_news(self, usuario, tema, palabra, news):
        
            # Obtener el timestamp actual
            timestamp = datetime.now()

            # Crear un documento para el modelo de DB
            news_data = {
                "usuario": usuario,
                "tema": tema,
                "palabra": palabra,
                "news": news,
                "timestamp": timestamp  # Agregar el campo timestamp al documento
            }

            # Insertar las noticias en la base de datos y devolver su ID
            result = self.news_collection.insert_one(news_data)
            news_id = str(result.inserted_id)
            return news_id