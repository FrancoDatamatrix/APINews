from datetime import datetime
import logging
import os

from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId
from utils.second_Converter import SecondConverter

class UpdateScheduleDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))
    
        
    def update_processed_date(self, schedule_id):
         # Obtener el timestamp actual en segundos
        current_timestamp = int(datetime.now().timestamp())

        # Convertir el ID del schedule a ObjectId
        schedule_object_id = ObjectId(schedule_id)
        
        databases = self.client.list_database_names()
        
        update_result = None
        
        for db_name in databases:
            db = self.client[db_name]
            if "Schedule" in db.list_collection_names():
                schedule_collection = db["Schedule"]
                result = schedule_collection.update_one(
                    {"_id": schedule_object_id},  # Filtrar por el ID del schedule a actualizar
                    {"$set": {"procesado": current_timestamp}}  # Actualizar el campo 'procesado' con la fecha actual
                )
            if result.modified_count > 0:
                    update_result = result
        
        if update_result:
            return update_result.modified_count
        else:
            return 0  # Devolver 1 si se actualizó correctamente, 0 si no se encontró el schedule
    
        
        
    def update(self, updated_data):
        try:
        
            schedule_id = updated_data.pop("id", None)
            # Convertir el ID de schedule a ObjectId
            schedule_oid = ObjectId(schedule_id)
        
            # Verificar que hay campos para actualizar
            if not updated_data:
                return False
        
            # Convertir el campo "hora" si está presente
            if "hora" in updated_data:
                updated_data["hora"] = SecondConverter.converter(updated_data["hora"])
                  
            # Agregar la marca de tiempo actual al campo "lastUpdatedSchedule"
            updated_data["lastUpdatedSchedule"] = int(datetime.timestamp(datetime.now()))

            # Preparar la actualización con el operador $set
            update_query = {"$set": updated_data}
            
            databases = self.client.list_database_names()
            
            total_modified_count = 0
            
            logging.info(update_query)
            logging.info(schedule_oid)
            
            for db_name in databases:
                db = self.client[db_name]
                if "Schedule" in db.list_collection_names():
                    schedule_collection = db["Schedule"]
                    
                    result = schedule_collection.update_one({'_id': schedule_oid}, update_query)
                    total_modified_count += result.modified_count

            
            return total_modified_count > 0
        
        except Exception as e:
            print(f"Se produjo un error al actualizar el schedule: {e}")
            
            return False
        
        finally:
            # Cerrar la conexión después de completar la operación
            self.client.close()
        

    