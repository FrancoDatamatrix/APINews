from .DBMongoHelper import DBmongoHelper
from datetime import datetime

class CreateScheduleDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def create_schedule(self, user_id, hora, palabras,lugar):
        # Obtener el timestamp actual
        
        timestamp = int(datetime.timestamp(datetime.now()))

        # Crear un documento para el nuevo cronograma
        schedule_data = {
            "usuario_id": user_id,
            "hora": hora,
            "palabras": palabras,
            "lugar": lugar,
            "procesado": None,
            "lastUpdatedSchedule": timestamp
        }

        # Insertar el nuevo cronograma en la base de datos
        result = self.schedule_collection.insert_one(schedule_data)

        # Obtener el ID del nuevo cronograma creado y convertirlo a str
        schedule_id = str(result.inserted_id)

        # Retornar el ID del nuevo cronograma creado como JSON
        return schedule_id if schedule_id else None