import os
from bson import ObjectId
from bson.errors import InvalidId
from pymongo import MongoClient
from .GetUserDB import GetUserDB
from .DBMongoHelper import DBmongoHelper


class GetScheduleByUserDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        # self.user_collection = GetUserDB()

    def get_user_schedule(self, user_complete):
        try:
            
            if user_complete:
                user = user_complete["usuario"]
                user_db = self.client[f"{user}_db"]
                schedule_collection = user_db["Schedule"]
                
            # Intentar buscar los schedules por usuario (ID)
            schedule = schedule_collection.find({})
            
            
            if schedule:
                return schedule
            else:
                return {"error": "Schedules no encontrado"}
        except InvalidId:
            return {"error": "ID no válido"}
        except Exception as e:
            print(f"Se produjo un error al obtener los schedules: {e}")
            return {"error": "Error al obtener los schedules"}