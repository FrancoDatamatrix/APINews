import os
from bson import ObjectId
from pymongo import MongoClient
from .DBMongoHelper import DBmongoHelper
from utils.second_Converter import SecondConverter
from datetime import datetime

class CreateScheduleDB:
    def __init__(self):
        self.db_admin = DBmongoHelper()
        self.users_collection = self.db_admin.get_collection("users")
        self.client = MongoClient(os.getenv("DB_URL"))

    def create_schedule(self, user_id, hora, tema, palabras, lugar):
        try:
            
            if ObjectId.is_valid(user_id):
                user_oid = ObjectId(user_id)
                userComplete = self.users_collection.find_one({"_id": user_oid})
                
            if userComplete["rol"] == "user":
                user = userComplete["usuario"]
                user_db = self.client[f"{user}_db"]
                schedule_collection = user_db["Schedule"]
            else:
                schedule_collection = self.db_admin.get_collection("Schedule")
                
            # Obtener el timestamp actual
            timestamp = int(datetime.timestamp(datetime.now()))
            
            # Convertimos las horas a segundos
            segundos_totales = SecondConverter.converter(hora)
        
            # Crear un documento para el nuevo cronograma
            schedule_data = {
                "usuario_id": user_id,
                "hora": segundos_totales,
                "tema":tema,
                "palabras": palabras,
                "lugar": lugar,
                "procesado": None,
                "lastUpdatedSchedule": timestamp
            }

            # Insertar el nuevo cronograma en la base de datos
            result = schedule_collection.insert_one(schedule_data)

            # Obtener el ID del nuevo cronograma creado y convertirlo a str
            schedule_id = str(result.inserted_id)

            # Retornar el ID del nuevo cronograma creado como JSON
            return schedule_id if schedule_id else None
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.client.close()