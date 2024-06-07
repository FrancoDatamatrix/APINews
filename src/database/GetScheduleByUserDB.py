from bson import ObjectId
from bson.errors import InvalidId
from .DBMongoHelper import DBmongoHelper

class GetScheduleByUserDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def get_user_schedule(self, identifier):
        try:
            # Convertir el identificador a ObjectId
            user_oid = ObjectId(identifier)
            # Intentar buscar los schedules por usuario (ID)
            schedule = self.schedule_collection.find({"usuario_id": user_oid})
            if schedule:
                return schedule
            else:
                return {"error": "Schedules no encontrado"}
        except InvalidId:
            return {"error": "ID no válido"}
        except Exception as e:
            print(f"Se produjo un error al obtener los schedules: {e}")
            return {"error": "Error al obtener los schedules"}