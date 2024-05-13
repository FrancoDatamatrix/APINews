from flask import jsonify, request
from ..utils import inputDeleteValidator
from ..database import DeleteUserDB, GetUserDB, StopScheduleDB


class DeleteUserService:
    def delete_user(self,user_id):
        try:
            # Verificar que se proporcionen el ID utilizando InputValidator
            if not inputDeleteValidator.validate_id_user_data(user_id):
                return jsonify({"error": "Se requiere el ID del usuario"}), 400

            # Eliminar el usuario
            delete_user_db = DeleteUserDB()
            deleted_user_id = delete_user_db.delete_user_by_id(user_id)
            # Eliminar los schedules asociados al usuario
            stop_schedule_db = StopScheduleDB()
            deleted_schedules_count = stop_schedule_db.stop_schedule(user_id)

            return jsonify({
                "message": "Usuario eliminado exitosamente",
                "user_id": str(deleted_user_id),
                "deleted_schedules_count": deleted_schedules_count
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500