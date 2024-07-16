import os
from pymongo import MongoClient

class DropDB:
    def __init__(self):
        self.client = MongoClient(os.getenv("DB_URL"))    

    def drop_db(self, usuario):
        try:
            db_name = f"{usuario}_db"
            self.client.drop_database(db_name)  # MongoDB tiene el método drop_database directamente en el cliente
            
            #eliminar el usuario de la base de datos
            db = self.client[db_name]
            
            users = db.command('usersInfo')
            for user in users['users']:
                db.command('dropUser', user['user'])
                
            response = {
                "message": f"La base de datos '{db_name}' ha sido eliminada con éxito."
            }
        except Exception as e:
            response = {
                # "error": str(e),
                "message": f"No se pudo eliminar la base de datos '{db_name}'."
            }
        finally:
            self.client.close()

        return response
