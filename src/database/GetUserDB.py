from .DBMongoHelper import DBmongoHelper

class GetUserDB:
        def __init__(self):
         self.db_helper = DBmongoHelper()
         self.users_collection = self.db_helper.get_collection("users")
 
        def get_user(self, identifier):
        # Intentar buscar el usuario por ID
         user = self.users_collection.find_one({"_id": identifier})
         if user:
            return user

        # Si no se encuentra por ID, buscar por nombre de usuario
         user = self.users_collection.find_one({"username": identifier})
         return user