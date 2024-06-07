from bson import ObjectId
from bson.errors import InvalidId
from .DBMongoHelper import DBmongoHelper

class GetScheduleByID:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def get_schedule(self, identifier):
        try:
            # Convertir el identificador a ObjectId
            schedule_oid = ObjectId(identifier)
            # Intentar buscar el schedule por ObjectId (ID)
            schedule = self.schedule_collection.find_one({"_id": schedule_oid})
            if schedule:
                return schedule
            else:
                return {"error": "Schedule no encontrado"}
        except InvalidId:
            return {"error": "ID no válido"}
        except Exception as e:
            print(f"Se produjo un error al obtener el schedule: {e}")
            return {"error": "Error al obtener el schedule"}
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()