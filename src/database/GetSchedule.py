from datetime import datetime
from .DBMongoHelper import DBmongoHelper

class GetScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

       def get_schedule(self):
        # Obtener la hora y fecha actual
        current_time = datetime.now().time()
        current_date = datetime.now().date()

        # Consultar los cronogramas en la base de datos
        schedules = self.schedule_collection.find({
            "$or": [
                {"procesado": {"$exists": False}},  # Filtrar los schedules no procesados
                {"procesado": {"$ne": current_date}}  # Filtrar los schedules procesados en una fecha diferente a la actual
            ],
            "hora": {"$lte": current_time}  # Filtrar las horas iguales o menores a la actual
        })

        # Convertir el cursor a una lista de diccionarios
        schedules_list = list(schedules)

        return schedules_list