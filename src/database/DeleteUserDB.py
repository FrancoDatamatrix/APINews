from .DBMongoHelper import DBmongoHelper
from bson import ObjectId

class DeleteUserDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def delete_user_by_id(self, user_id):
        try:
            # Convertir el user_id a ObjectId
            user_oid = ObjectId(user_id)
            
            # Buscar y eliminar el usuario por su ObjectId
            result = self.users_collection.delete_one({"_id": user_oid})
            
            # Verificar si se eliminó algún usuario
            return result.deleted_count > 0
        finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            self.db_helper.close()
