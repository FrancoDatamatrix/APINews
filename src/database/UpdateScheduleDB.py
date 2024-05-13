from datetime import datetime
from .DBMongoHelper import DBmongoHelper

class UpdateScheduleDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def update_processed_date(self, schedule_ids):
        # Obtener la fecha actual
        current_date = datetime.now().date()

        # Actualizar el campo 'procesado' con la fecha actual para los schedules especificados
        update_result = self.schedule_collection.update_many(
            {"_id": {"$in": schedule_ids}},  # Filtrar por los IDs de los schedules a actualizar
            {"$set": {"procesado": current_date}}  # Actualizar el campo 'procesado' con la fecha actual
        )

        return update_result.modified_count  # Devolver el número de schedules actualizados