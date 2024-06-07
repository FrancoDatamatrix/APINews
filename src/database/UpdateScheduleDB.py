from datetime import datetime
from .DBMongoHelper import DBmongoHelper
from bson import ObjectId
from utils.second_Converter import SecondConverter

class UpdateScheduleDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")
    
        
        
    def update_processed_date(self, schedule_id):
         # Obtener el timestamp actual en segundos
        current_timestamp = int(datetime.now().timestamp())

        # Convertir el ID del schedule a ObjectId
        schedule_object_id = ObjectId(schedule_id)

        # Actualizar el campo 'procesado' con la fecha actual para el schedule especificado por ID
        update_result = self.schedule_collection.update_one(
            {"_id": schedule_object_id},  # Filtrar por el ID del schedule a actualizar
            {"$set": {"procesado": current_timestamp}}  # Actualizar el campo 'procesado' con la fecha actual
        )
        # Asegurarse de cerrar la conexión después de completar la operación
        self.db_helper.close()

        return update_result.modified_count  # Devolver 1 si se actualizó correctamente, 0 si no se encontró el schedule
    
    
        
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

            # Actualizar el schedule en la base de datos
            result = self.schedule_collection.update_one({'_id': schedule_oid}, update_query)
            return result.modified_count > 0
        
        except Exception as e:
            print(f"Se produjo un error al actualizar el schedule: {e}")
            
            return False
        
        finally:
            # Cerrar la conexión después de completar la operación
            self.db_helper.close()
        

    