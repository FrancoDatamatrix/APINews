import os
from bson import ObjectId
from bson.errors import InvalidId
from flask import g
from pymongo import MongoClient

class GetScheduleByID:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
        # self.schedule_collection = self.db_helper.get_collection("Schedule")

    def get_schedule(self, identifier):
        try:
            databases = self.client.list_database_names()
            
            all_schedules = []
            
            # Convertir el identificador a ObjectId
            schedule_oid = ObjectId(identifier)
            # Intentar buscar el schedule por ObjectId (ID)
            
            for db_name in databases:
                db = self.client[db_name]
                if "Schedule" in db.list_collection_names():
                    schedule_collection = db["Schedule"]
                    schedules = list(schedule_collection.find({"_id": schedule_oid}))
                    all_schedules.extend(schedules)
        
            if all_schedules:
                return all_schedules
            else:
                return {"error": "Schedule no encontrado"}
        except InvalidId:
            return {"error": "ID no válido"}
        except Exception as e:
            print(f"Se produjo un error al obtener el schedule: {e}")
            return {"error": "Error al obtener el schedule"}
    
            # schedule = self.schedule_collection.find_one({"_id": schedule_oid})
            # if schedule:
            #     return schedule
            # else:
            #     return {"error": "Schedule no encontrado"}
        # except InvalidId:
        #     return {"error": "ID no válido"}
        # except Exception as e:
        #     print(f"Se produjo un error al obtener el schedule: {e}")
        #     return {"error": "Error al obtener el schedule"}
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()