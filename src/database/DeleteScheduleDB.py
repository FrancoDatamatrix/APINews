
import os
from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId
from flask import g

class DeleteScheduleDB:
       def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
       #  self.schedule_collection = self.db_helper.get_collection("Schedule")


       def delete_schedule(self, id):
              databases = self.client.list_database_names()
              # Convertir el user_id a ObjectId
              schedule_oid = ObjectId(id)
              
              new_result = None
              
              for db_name in databases:
                     db = self.client[db_name]
                     if "Schedule" in db.list_collection_names():
                            schedule_collection = db["Schedule"]
                            result = schedule_collection.delete_one({"_id": schedule_oid})
                     if result.deleted_count > 0:
                            new_result = result
                            
              self.client.close()
              if new_result:
                     return new_result.deleted_count
              else:
                     return 0