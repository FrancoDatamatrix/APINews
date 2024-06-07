from bson import ObjectId
from bson.errors import InvalidId
from .DBMongoHelper import DBmongoHelper
import logging

class GetUserDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def get_user(self, identifier):
        user = None
        logging.info("intentando obtener usuario")
        try:
            # Intentar convertir el identificador a ObjectId y buscar por ID
            if ObjectId.is_valid(identifier):
                logging.info("intentando convertir el identifier en objectid")
                user_oid = ObjectId(identifier)
                user = self.users_collection.find_one({"_id": user_oid})
            # Si no se encuentra por ID o si el identifier no es un ObjectId válido, buscar por nombre de usuario
            if not user:
                logging.info("intentando buscar el user por nombre")
                user = self.users_collection.find_one({"usuario": identifier})

        except Exception as e:
            print(f"Se produjo un error al obtener el usuario: {e}")
            return {"error": "Error al obtener el usuario"}
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()
        return user