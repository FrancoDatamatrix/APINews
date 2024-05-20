from cryptohash import md5

class APIKeyValidator:
    @staticmethod
    def validate_api_key(user_data):
        #obtenemos los datos del usuario
        usuario = user_data.get("usuario")
        contraseña = user_data.get("contraseña")
        api_key = user_data.get("api_key")
        
        # comparamos las key concatenando usuario + constraseña
        key = usuario + contraseña
        return api_key == md5(key)
