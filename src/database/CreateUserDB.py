import bcrypt
from .DBMongoHelper import DBmongoHelper

class CreateUserDB:
    def __init__(self):
        # conexión a base de datos y a la colección users
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def create_user(self, user_data):
        
        #obtenemos los datos para almacenarlo sin el api-key
        usuario = user_data.get("usuario")
        contraseña = user_data.get("contraseña")
        
        # Hashear la contraseña
        hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt())
        
        new_user = {
            "usuario" : usuario,
            "contraseña": hashed_password.decode('utf-8')
        }

        # Insertamos el usuario a la base de datos y devolvemos su id
        result = self.users_collection.insert_one(new_user)
        return result.inserted_id
    