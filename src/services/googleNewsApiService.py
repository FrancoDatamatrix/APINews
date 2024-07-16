import os
from pymongo import MongoClient
from database.GetSchedule import GetScheduleDB
from database.GetUserWordsDB import GetUserWordsDB
from database.CreateNewsGoogleDB import CreateNewsDB
from database.DBMongoHelper import DBmongoHelper
from utils.googleNewsApi import GoogleNewsAPI
from database.UpdateScheduleDB import UpdateScheduleDB
import logging

class GoogleNewsApiService:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        self.get_schedule_db = GetScheduleDB()
        self.get_user_words_db = GetUserWordsDB()
        self.create_news_db = CreateNewsDB()
        self.update_schedule_db = UpdateScheduleDB()

    def get_news(self):
        try:
            # Obtener los cronogramas diarios de la base de datos
            logging.info("Checando Base de datos")
            schedules = self.get_schedule_db.get_schedule()
            
            if not schedules:
                logging.info("No hay ningun schedule")
                return "No hay ningun schedule"
            
            success = True
            
            # Iterar sobre cada cronograma
            for schedule in schedules:
                logging.info(f"Info Schedule {schedule}")
                hora = schedule.get("hora")
                usuario = schedule.get("usuario_id")
                tema = schedule.get("tema")
                palabras = schedule.get("palabras")
                arrPalabras = palabras.split(',')
                lugar = schedule.get("lugar")
                logging.info(f"Iterando schedules para usuario {usuario} a las {hora}")
                
                # Iterar sobre cada palabra en el arreglo de palabras
                for palabra in arrPalabras:
                    # Hacer la consulta a la API de Google Search
                    response = GoogleNewsAPI.get_google_search_api(palabra, lugar)
                    logging.info(f"Iterando palabras: {palabra} en lugar: {lugar}")
                    
                    # Crear la noticia en la base de datos
                    if not response:
                        logging.warning("No hay respuesta de Google")
                        continue  # Continuar con la siguiente palabra
                    
                    news_created = self.create_news_db.create_news(usuario,tema, palabra, response)
                    if news_created:
                        logging.info("Noticias creadas!")
                    else:
                        logging.error("No se crearon noticias")
                        success = False  # Si la creación de noticias falla, marcar como no exitoso

                # Llamar al método update_processed_date de updateScheduleDB
                self.update_schedule_db.update_processed_date(schedule.get("_id"))
                
            # Asegurarse de cerrar la conexión después de completar la operación
            self.client.close()
            
            return "Schedule completado" if success else "Schedule completado con errores"
        
        except Exception as e:
            logging.error(f"Error al obtener noticias: {e}")
            return "Error al obtener noticias"

# Configurar logging
logging.basicConfig(level=logging.INFO)
