from datetime import datetime
import os
from pymongo import MongoClient

class GetScheduleDB:
       def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))

       def get_schedule(self):
        try:
            # Obtener todas las bases de datos
            databases = self.client.list_database_names()
            
            # Obtener la fecha y hora actuales
            now = datetime.now()
            
            # Obtener el timestamp actual en segundos
            current_timestamp = int(now.timestamp())
        
            # Crear un nuevo objeto datetime solo con la fecha (año, mes, día)
            date_only = datetime(now.year, now.month, now.day)
            
            # Calcular la cantidad de segundos transcurridos desde las 00
            current_hour_seconds =  int(datetime.timestamp(now)) - int(datetime.timestamp(date_only)) 
            
            # Consultar los cronogramas en la base de datos
            all_schedules = []
        
            # Recorrer cada base de datos y obtener la colección "schedule"
            for db_name in databases:
                db = self.client[db_name]
                if "Schedule" in db.list_collection_names():
                    schedule_collection = db["Schedule"]
                    schedules = list(schedule_collection.find({
                        "$or": [
                            {"procesado": None},                                                  # Filtrar los schedules no procesados
                            {"procesado": {"$ne": None, "$lte": current_timestamp - 86400}}      # Filtrar los schedules procesados y cuya diferencia de tiempo sea menor a 86400 segundos (24 horas)
                        ],
                        "$expr": {                                                               # $expr para permitir el uso de expresiones de agregación en la consulta. 
                            "$and": [                                                            # $and combina las dos condiciones: la diferencia debe ser menor o igual a 300 y mayor o igual a -300.
                                {"$lte": [{"$subtract": ["$hora", current_hour_seconds]}, 300]}, # $subtract se utiliza para calcular la diferencia entre la hora en la base de datos ($hora)
                                {"$gte": [{"$subtract": ["$hora", current_hour_seconds]}, -300]}
                            ]
                        }
                    }))
                    all_schedules.extend(schedules)
                    
            # schedules = self.schedule_collection.find({
            #     "$or": [
            #         {"procesado": None},                                                  # Filtrar los schedules no procesados
            #         {"procesado": {"$ne": None, "$lte": current_timestamp - 86400}}      # Filtrar los schedules procesados y cuya diferencia de tiempo sea menor a 86400 segundos (24 horas)
            #     ],
            #     "$expr": {                                                               # $expr para permitir el uso de expresiones de agregación en la consulta. 
            #         "$and": [                                                            # $and combina las dos condiciones: la diferencia debe ser menor o igual a 300 y mayor o igual a -300.
            #             {"$lte": [{"$subtract": ["$hora", current_hour_seconds]}, 300]}, # $subtract se utiliza para calcular la diferencia entre la hora en la base de datos ($hora)
            #             {"$gte": [{"$subtract": ["$hora", current_hour_seconds]}, -300]}
            #         ]
            #     }
            # })
            return all_schedules
        except Exception as e:
            # Manejar excepciones específicas si es necesario
            print(f"Se produjo un error al obtener las noticias: {e}")