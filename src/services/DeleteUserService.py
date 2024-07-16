from flask import jsonify
from utils.inputDeleteValidator import InputDeleteValidator
from database.DeleteUserDB import DeleteUserDB
from database.GetUserDB import GetUserDB
from database.StopScheduleDB import StopScheduleDB
from database.DropDatabaseUser import DropDB


class DeleteUserService:
    def delete_user(self, user_id, usuario):
        try:
            # Verificar que se proporcionen el ID utilizando InputValidator
            if not InputDeleteValidator.validate_id_user_data(user_id):
                return jsonify({"error": "Se requiere el ID del usuario"}), 400

            # Eliminar el usuario
            delete_user_db = DeleteUserDB()
            deleted_user_count = delete_user_db.delete_user_by_id(user_id)
            
            # Verificar si se eliminó algún usuario
            if deleted_user_count == 0:
                return jsonify({"error": "No se encontró ningún usuario con el ID proporcionado"}), 400
            
            # Eliminar los schedules asociados al usuario
            stop_schedule_db = StopScheduleDB()
            deleted_schedules_count = stop_schedule_db.stop_schedule(user_id)
            
            #Eliminar la base de datos
            drop_database = DropDB()
            drop_response = drop_database.drop_db(usuario)
            
            return jsonify({
                "message": "Usuario eliminado exitosamente",
                "user_id": user_id,
                "deleted_schedules_count": deleted_schedules_count,
                "database": drop_response
            }), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500