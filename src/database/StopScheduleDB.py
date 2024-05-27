from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class StopScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")


       def stop_schedule(self, user_id):
              # Convertir el user_id a ObjectId
              user_oid = ObjectId(user_id)
              result = self.schedule_collection.delete_many({"usuario_id": user_oid})
              # Asegurarse de cerrar la conexión después de completar la operación
              self.db_helper.close()
              return result.deleted_count