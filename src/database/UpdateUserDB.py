import bcrypt
from .DBMongoHelper import DBmongoHelper

class UpdateUserDB:
        def __init__(self):
        #conexion a base de datos y a la coleccion users
         self.db_helper = DBmongoHelper()
         self.users_collection = self.db_helper.get_collection("users")

        def update_user(self, user_id, updated_data):
        # Si la contraseña está presente en los datos actualizados, la hasheamos antes de actualizarla
         if 'contraseña' in updated_data:
            hashed_password = bcrypt.hashpw(updated_data['contraseña'].encode('utf-8'), bcrypt.gensalt())
            updated_data['contraseña'] = hashed_password.decode('utf-8')

        # Actualizamos el usuario en la base de datos
         result = self.users_collection.update_one({'_id': user_id}, {'$set': updated_data})
        
        # Comprobamos si se realizó la actualización correctamente
         if result.modified_count > 0:
            return "Usuario actualizado correctamente."
         else:
            return "No se encontró el usuario o no se realizaron cambios."    