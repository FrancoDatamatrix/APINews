from database.GetUserDB import GetUserDB
import bcrypt

class CredencialsValidator:
    @staticmethod
    def validar_credenciales(usuario, contraseña):
        # Obtener el usuario de la base de datos
        get_user_db = GetUserDB()
        usuario_encontrado = get_user_db.get_user(usuario)

        if usuario_encontrado:
            # Obtener la contraseña hash almacenada en la base de datos
            hash_contraseña = usuario_encontrado.get('contraseña', '')

            # Verificar si la contraseña coincide utilizando bcrypt
            if bcrypt.checkpw(contraseña.encode('utf-8'), hash_contraseña.encode('utf-8')):
                return usuario_encontrado

        return False
     
