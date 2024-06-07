from .DBMongoHelper import DBmongoHelper

class GetAllUserDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.users_collection = self.db_helper.get_collection("users")

    def get_all_users(self):
        # Inicializar la variable users
        users = []
    
        try:
            # Traemos todos los usuarios de la base de datos
            users_cursor = self.users_collection.find({})
            users = list(users_cursor)
        except Exception as e:
            # Manejar excepciones específicas si es necesario
            print(f"Se produjo un error al obtener los usuarios: {e}")
        finally:
            # Cerrar la conexión después de obtener los datos
            self.db_helper.close()
        
        return users