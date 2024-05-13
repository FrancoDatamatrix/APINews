from .DBMongoHelper import DBmongoHelper
from datetime import datetime

class CreateScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

       def create_schedule(self, user_id, hora, palabras):
        # Obtener el timestamp actual
        timestamp = datetime.timestamp(datetime.now())

        # Crear un documento para el nuevo cronograma
        schedule_data = {
            "usuario_id": user_id,
            "hora": hora,
            "palabras": palabras,
            "procesado": None,
            "timestamp": timestamp
        }
        
        # Insertar el nuevo cronograma en la base de datos
        result = self.schedule_collection.insert_one(schedule_data)
        
        # Retornar el ID del nuevo cronograma creado
        return str(result.inserted_id)