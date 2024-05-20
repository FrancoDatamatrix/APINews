from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class StopScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")


       def stop_schedule(self, user_id):
              # Convertir el user_id a ObjectId
              user_oid = ObjectId(user_id)
              result = self.schedule_collection.delete_many({"_id": user_oid})
              return result.deleted_count