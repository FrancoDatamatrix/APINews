import os
from pymongo import MongoClient
from bson import ObjectId

class StopScheduleDB:
       def __init__(self):
              self.client = MongoClient(os.getenv("DB_URL"))
        

       def stop_schedule(self, user_id):
              try:
                     # Obtener todas las bases de datos
                     databases = self.client.list_database_names()
        
                     # Convertir el user_id a ObjectId
                     user_oid = ObjectId(user_id)
        
                     # Recorrer cada base de datos y obtener la colección "schedule"
                     for db_name in databases:
                            db = self.client[db_name]
                            if "Schedule" in db.list_collection_names():
                                   schedule_collection = db["Schedule"]
                                   schedules = schedule_collection.delete_many({"usuario_id": user_oid})

              except Exception as e:
              # Manejar excepciones específicas si es necesario
                     print(f"Se produjo un error al obtener los schedules: {e}")
              finally:
              # Cerrar la conexión después de obtener los datos
                     self.client.close()
        
              return schedules.deleted_count