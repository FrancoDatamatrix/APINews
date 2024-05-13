import bcrypt
from .DBMongoHelper import DBmongoHelper

class CreateUserDB:
    def __init__(self):
        # conexión a base de datos y a la colección users
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def create_user(self, user_data):
        # Hashear la contraseña antes de guardarla en la base de datos
        hashed_password = bcrypt.hashpw(user_data['contraseña'].encode('utf-8'), bcrypt.gensalt())

        # Actualizar el diccionario de datos del usuario con la contraseña hasheada
        user_data['contraseña'] = hashed_password.decode('utf-8')
        # insertamos el usuario a la base de datos y devolvemos su id
        result = self.users_collection.insert_one(user_data)
        return result.inserted_id
    