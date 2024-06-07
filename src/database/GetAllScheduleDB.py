from .DBMongoHelper import DBmongoHelper

class GetAllScheduleDB:
    def __init__(self):
        self.db_helper = DBmongoHelper()
        self.schedule_collection = self.db_helper.get_collection("Schedule")

    def get_all_schedule(self):
        # Inicializar la variable schedule
        schedule = []
    
        try:
            # Traemos todos los schedules de la base de datos
            schedule_cursor = self.schedule_collection.find({})
            users = list(schedule_cursor)
        except Exception as e:
            # Manejar excepciones específicas si es necesario
            print(f"Se produjo un error al obtener los schedules: {e}")
        finally:
            # Cerrar la conexión después de obtener los datos
            self.db_helper.close()
        
        return users