from .DBMongoHelper import DBmongoHelper

class StopScheduleDB:
       def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")


       def stop_schedule(self, user_id):
        result = self.schedule_collection.delete_many({"usuario_id": user_id})
        return result.deleted_count