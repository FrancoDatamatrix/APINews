from ..utils import QueryValidator,CredencialsValidator
from flask import jsonify, request
from ..database import CreateScheduleDB

class ScheduleService:
    def __init__(self):
        # Puedes inicializar aquí cualquier estado necesario para tu controlador
        pass

    def query(self, user_data):
        
        # Validar que se proporcionen los datos utilizando QueryInputValidator
        if not QueryValidator.validate_user_data(user_data):
                return jsonify({"error": "usuario, contraseña, hora y palabras clave son obligatorios"}), 400

        # Extraer usuario, contraseña y hora de user_data
        usuario = user_data.get("usuario")
        contraseña = user_data.get("contraseña")
        hora = user_data.get("hora")
        palabras = user_data.get("palabras")
        lugar = user_data.get("lugar")

        # Validar las credenciales del usuario utilizando CredencialValidator
        if not CredencialsValidator.validar_credenciales(usuario, contraseña):
            raise ValueError("Credenciales de usuario incorrectas")

        # Actualizar el usuario para agregar las palabras clave
            update_user_db = UpdateUserDB()
            user = update_user_db.get_user_by_username(usuario)
            if user:
                updated_data = {"palabras": palabras, "lugar":lugar}
                user_id = user['_id']
                update_user_db.update_user(user_id, updated_data)
                
                # Crear una instancia de CreateScheduleDB y crear el cronograma
                create_schedule_db = CreateScheduleDB()
                create_schedule_db.create_schedule(hora, user_id)
            else:
                raise ValueError("Usuario no encontrado")

        respuesta = {"mensaje": "Petición recibida correctamente"}
        return respuesta