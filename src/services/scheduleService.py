from ..utils import QueryValidator, CredencialsValidator
from flask import jsonify, request
from ..database import CreateScheduleDB, UpdateUserDB

class ScheduleService:
    def __init__(self):
        pass

    def query(self, user_data):
        # Validar que se proporcionen los datos obligatorios
        required_fields = ["usuario", "contraseña", "hora", "palabras"]
        if not all(field in user_data for field in required_fields):
            return jsonify({"error": "usuario, contraseña, hora y palabras clave son obligatorios"}), 400

        usuario = user_data.get("usuario")
        contraseña = user_data.get("contraseña")
        hora = user_data.get("hora")
        palabras = user_data.get("palabras")
        lugar = user_data.get("lugar")

        # Validar las credenciales del usuario
        user = CredencialsValidator.validar_credenciales(usuario, contraseña)
        if not user:
            return jsonify({"error": "Credenciales de usuario incorrectas"}), 401

        # Actualizar el usuario para agregar las palabras clave
        update_user_db = UpdateUserDB()
        updated_data = {"palabras": palabras}
        if lugar:  # Verifica si se proporcionó el campo "lugar"
            updated_data["lugar"] = lugar
        user_id = user['_id']
        print(user_id)
        update_user_db.update_user(user_id, updated_data)

        # Crear el cronograma
        create_schedule_db = CreateScheduleDB()
        schedule_id = create_schedule_db.create_schedule(user_id, hora, palabras)

        if schedule_id is None:
            # Manejar el error, ya que no se devolvió un schedule_id válido
            return jsonify({"error": "Hubo un problema al crear el cronograma"}), 500

        # Si create_schedule() fue exitoso, devuelve el ID del cronograma y mensaje de éxito
        return jsonify({"schedule_id": schedule_id, "mensaje": "Petición recibida correctamente"}), 200