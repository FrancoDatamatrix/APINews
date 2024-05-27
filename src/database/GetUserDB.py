from bson import ObjectId
from .DBMongoHelper import DBmongoHelper

class GetUserDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def get_user(self, identifier):
        # Intentar buscar el usuario por ObjectId (ID)
        try:
            user_oid = ObjectId(identifier)
            user = self.users_collection.find_one({"_id": user_oid})
            if user:
                return user
        except:
            pass  # Ignorar errores si identifier no es un ObjectId válido

        # Si no se encuentra por ID, buscar por nombre de usuario
        user = self.users_collection.find_one({"usuario": identifier})
        
        # Cerrar la conexión después de obtener los datos
        self.db_helper.close()
        
        return user