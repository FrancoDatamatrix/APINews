import bcrypt
from bson import ObjectId
from .DBMongoHelper import DBmongoHelper

class UpdateUserDB:
    def __init__(self):
        # Conexión a la base de datos y a la colección users
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def update_user(self, user_id, updated_data):
        # Convertir el ID de usuario a ObjectId
        user_oid = ObjectId(user_id)
        
        # Campos permitidos para actualización
        allowed_fields = {'contraseña', 'rol', 'palabras', 'lugar'}
    
        # Eliminar campos no permitidos
        filtered_data = {key: value for key, value in updated_data.items() if key in allowed_fields}

        # Si la contraseña está presente en los datos actualizados, la hasheamos antes de actualizarla
        if 'contraseña' in updated_data:
            hashed_password = bcrypt.hashpw(updated_data['contraseña'].encode('utf-8'), bcrypt.gensalt())
            filtered_data['contraseña'] = hashed_password.decode('utf-8')
           

        # Actualizar el usuario en la base de datos
        result = self.users_collection.update_one({'_id': user_oid}, {'$set': filtered_data})
        
        # Asegurarse de cerrar la conexión después de completar la operación
        self.db_helper.close()
        
        # Comprobar si se realizó la actualización correctamente
        if result.modified_count > 0:
            return "Usuario actualizado correctamente."
        else:
            return "No se encontró el usuario o no se realizaron cambios."   