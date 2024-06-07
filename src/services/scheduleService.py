from utils.queryInputValidator import QueryValidator
from utils.credencialsValidator import CredencialsValidator
from flask import jsonify
from database.CreateScheduleDB import CreateScheduleDB
from database.UpdateUserDB import UpdateUserDB

class ScheduleService:
    def __init__(self):
        pass

    def query(self, schedule_data,user):
        # Validar que se proporcionen los datos obligatorios
        required_fields = ["hora","tema","palabras"]
        if not all(field in schedule_data for field in required_fields):
            return jsonify({"error": "hora, tema y palabras clave son obligatorios"}), 400

        hora = schedule_data.get("hora")
        tema = schedule_data.get("tema")
        palabras = schedule_data.get("palabras")
        lugar = schedule_data.get("lugar")

        # Verificar que los campos no estén vacíos
        if any(value.strip() == "" for value in [palabras,tema,hora]):
            return jsonify({"error": "Los campos no pueden estar vacíos"}), 400

        # Actualizar el usuario para agregar las palabras clave
        update_user_db = UpdateUserDB()
        updated_data = {"palabras": palabras}
        if lugar:  # Verifica si se proporcionó el campo "lugar"
            updated_data["lugar"] = lugar
        user_id = user['_id']
        update_user_db.update_user(user_id, updated_data)

        # Crear el cronograma
        create_schedule_db = CreateScheduleDB()
        schedule_id = create_schedule_db.create_schedule(user_id, hora,tema, palabras,lugar)

        if schedule_id is None:
            # Manejar el error, ya que no se devolvió un schedule_id válido
            return jsonify({"error": "Hubo un problema al crear el cronograma"}), 500

        # Si create_schedule() fue exitoso, devuelve el ID del cronograma y mensaje de éxito
        return jsonify({"schedule_id": schedule_id, "mensaje": "Petición recibida correctamente"}), 200