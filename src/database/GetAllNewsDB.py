from .DBMongoHelper import DBmongoHelper

class GetAllNewsDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.news_collection = self.db_helper.get_collection("news")

    def get_all_news(self, page=1, page_size=5):
        # Inicializar la variable news
        news = []

        try:
            # Calcular el índice de inicio y fin para la paginación
            start_index = (page - 1) * page_size
            end_index = start_index + page_size

            print(f"Start Index: {start_index}, End Index: {end_index}")

            # Traer las noticias paginadas de la base de datos
            news_cursor = self.news_collection.find({}).skip(start_index).limit(page_size)
            news = list(news_cursor)
        except Exception as e:
            # Manejar excepciones específicas si es necesario
            print(f"Se produjo un error al obtener las noticias: {e}")
        finally:
            # Cerrar la conexión después de obtener los datos
            self.db_helper.close()

        return news