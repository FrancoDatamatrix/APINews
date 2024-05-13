from .DBMongoHelper import DBmongoHelper

class GetUserWordsDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def get_words(self, user_id):
        # Buscar el usuario por ID
        user = self.users_collection.find_one({"_id": user_id})
        
        # Verificar si se encontró el usuario y si tiene palabras asociadas
        if user and "palabras" in user:
            palabras_string = user["palabras"]
            palabras_array = palabras_string.split(',')  # Dividir la cadena en un arreglo usando la coma como separador
            lugar = user.get("lugar")  # Obtener el lugar del usuario
            return palabras_array, lugar  # Devolver las palabras del usuario y el lugar
        else:
            return None, None  # Devolver None si el usuario no se encontró o no tiene palabras asociadas