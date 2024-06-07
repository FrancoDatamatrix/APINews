
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class DeleteScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")


       def delete_schedule(self, id):
              # Convertir el user_id a ObjectId
              schedule_oid = ObjectId(id)
              result = self.schedule_collection.delete_one({"_id": schedule_oid})
              # Asegurarse de cerrar la conexión después de completar la operación
              self.db_helper.close()
              return result.deleted_count > 0