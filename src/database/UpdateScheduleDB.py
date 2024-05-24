from datetime import datetime
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class UpdateScheduleDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def update_processed_date(self, schedule_id):
         # Obtener el timestamp actual en segundos
        current_timestamp = int(datetime.now().timestamp())

        # Convertir el ID del schedule a ObjectId
        schedule_object_id = ObjectId(schedule_id)

        # Actualizar el campo 'procesado' con la fecha actual para el schedule especificado por ID
        update_result = self.schedule_collection.update_one(
            {"_id": schedule_object_id},  # Filtrar por el ID del schedule a actualizar
            {"$set": {"procesado": current_timestamp}}  # Actualizar el campo 'procesado' con la fecha actual
        )

        return update_result.modified_count  # Devolver 1 si se actualizó correctamente, 0 si no se encontró el schedule