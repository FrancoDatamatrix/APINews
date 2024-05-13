from pymongo import MongoClient

class UserDB:
    def __init__(self, db_url, db_name):
        self.client = MongoClient(db_url)
        self.db = self.client[db_name]
        self.users_collection = self.db['users']
    def create_user(self, user_data):
        """
        Crea un nuevo registro de usuario en la base de datos.
        
        Args:
        - user_data (dict): Un diccionario que contiene los datos del nuevo usuario.
        
        Returns:
        - str: El ID del nuevo usuario creado.
        """
        result = self.users_collection.insert_one(user_data)
        return result.inserted_id
    def find_user_by_username(self, username):
        """
        Busca un usuario por su nombre de usuario en la base de datos.
        
        Args:
        - username (str): El nombre de usuario del usuario que se quiere buscar.
        
        Returns:
        - dict: El documento del usuario encontrado, o None si no se encuentra.
        """
        return self.users_collection.find_one({"username": username})
    def find_users_by_username(self, username):
        """
        Busca todos los usuarios con un nombre de usuario específico en la base de datos.
        
        Args:
        - username (str): El nombre de usuario que se quiere buscar.
        
        Returns:
        - list: Una lista de todos los documentos de usuario encontrados.
        """
        return list(self.users_collection.find({"username": username}))
