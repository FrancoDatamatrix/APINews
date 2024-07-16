from pymongo import MongoClient
import os

class GetAllScheduleDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        

    def get_all_schedule(self):
        try:
            # Obtener todas las bases de datos
            databases = self.client.list_database_names()
        
            all_schedules = []
        
            # Recorrer cada base de datos y obtener la colección "schedule"
            for db_name in databases:
                db = self.client[db_name]
                if "Schedule" in db.list_collection_names():
                    schedule_collection = db["Schedule"]
                    schedules = list(schedule_collection.find({}))
                    all_schedules.extend(schedules)
        except Exception as e:
            # Manejar excepciones específicas si es necesario
                print(f"Se produjo un error al obtener los schedules: {e}")
        finally:
            # Cerrar la conexión después de obtener los datos
            self.client.close()
        
        return all_schedules