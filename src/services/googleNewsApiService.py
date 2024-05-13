from ..database import GetScheduleDB , GetUserWordsDB , CreateNewsDB
from ..utils import GoogleNewsAPI

class GoogleNewsApiService:
    def __init__(self):
        self.get_schedule_db = GetScheduleDB()
        self.get_user_Words_db = GetUserWordsDB()
        self.create_news_db = CreateNewsDB()

    def get_news(self):
        # Obtener los cronogramas diarios de la base de datos
        schedules = self.get_schedule_db.get_schedule()
        success = True
        
        # Iterar sobre cada cronograma
        for schedule in schedules:
            hora = schedule.get("hora")
            usuario = schedule.get("usuario_id")
            palabras, lugar = self.get_user_words_db.get_words(usuario)
            
            # Iterar sobre cada palabra en el arreglo de palabras
            for palabra in palabras:
                # Hacer la consulta a la API de Google Search
                response = GoogleNewsAPI.get_google_search_api(palabra,lugar)
                
                # Crear la noticia en la base de datos
                if response:
                    news_created = self.create_news_db.create_news(palabra, usuario, response)
                    if not news_created:
                        success = False  # Si la creación de noticias falla, marcar como no exitoso
        
        return success