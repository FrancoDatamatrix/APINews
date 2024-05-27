from .DBMongoHelper import DBmongoHelper
from utils.second_Converter import SecondConverter
from datetime import datetime

class CreateScheduleDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def create_schedule(self, user_id, hora, tema, palabras, lugar):
        try:
            # Obtener el timestamp actual
            timestamp = int(datetime.timestamp(datetime.now()))
            
            # Convertimos las horas a segundos
            segundos_totales = SecondConverter.converter(hora)
        
            # Crear un documento para el nuevo cronograma
            schedule_data = {
                "usuario_id": user_id,
                "hora": segundos_totales,
                "tema":tema,
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
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()