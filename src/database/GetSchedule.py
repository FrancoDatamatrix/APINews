from datetime import datetime
from .DBMongoHelper import DBmongoHelper

class GetScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

       def get_schedule(self):
        
        # Obtener el timestamp actual en segundos
        current_timestamp = int(datetime.now().timestamp())
        current_hour = int(datetime.now().strftime('%H%M'))
    
        # Consultar los cronogramas en la base de datos
        schedules = self.schedule_collection.find({
            "$or": [
                {"procesado": None} # Filtrar los schedules no procesados
                # {"procesado": {"$ne": None, "$lte": current_timestamp - 86400}}  # Filtrar los schedules procesados y cuya diferencia de tiempo sea menor a 86400 segundos (24 horas)
            ]
            # "hora": {"$lte": current_hour}  # Filtrar las horas iguales o menores a la actual
        })

        # Convertir el cursor a una lista de diccionarios
        schedules_list = list(schedules)
        return schedules_list