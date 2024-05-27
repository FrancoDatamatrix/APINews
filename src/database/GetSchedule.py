from datetime import datetime
from .DBMongoHelper import DBmongoHelper

class GetScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

       def get_schedule(self):
        try:
            # Obtener la fecha y hora actuales
            now = datetime.now()
            
            # Obtener el timestamp actual en segundos
            current_timestamp = int(now.timestamp())
        
            # Crear un nuevo objeto datetime solo con la fecha (año, mes, día)
            date_only = datetime(now.year, now.month, now.day)
            
            # Calcular la cantidad de segundos transcurridos desde las 00
            current_hour_seconds =  int(datetime.timestamp(now)) - int(datetime.timestamp(date_only)) 
            
            # Consultar los cronogramas en la base de datos
            schedules = self.schedule_collection.find({
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
            })

            # Convertir el cursor a una lista de diccionarios
            schedules_list = list(schedules)
            return schedules_list
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()