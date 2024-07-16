from flask import jsonify, Blueprint, request, Response
from flask_jwt_extended import get_jwt_identity, jwt_required
from services.scheduleService import ScheduleService
from utils.GetUserRol import GetUserRol
from database.GetAllScheduleDB import GetAllScheduleDB
from database.DeleteScheduleDB import DeleteScheduleDB
from database.GetScheduleByID import GetScheduleByID
from database.UpdateScheduleDB import UpdateScheduleDB
from database.GetUserDB import GetUserDB

from bson import json_util

schedule_blueprint = Blueprint('schedule', __name__)

#Ruta para obtener Schedules
@schedule_blueprint.route('/schedule', methods=['GET'])
@jwt_required()
def get_schedule():
    try:
        current_user = get_jwt_identity()
        user_role = GetUserRol.get_user_role(current_user)
        
        if user_role != "admin":
            return jsonify({"msg": "Solo Administradores!"}), 403
        
         # Crear una instancia de GetAllScheduleDB
        getSchedule = GetAllScheduleDB()
        
        # Llamar al método get_all_schedule 
        schedule = getSchedule.get_all_schedule()
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(schedule)
        
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500



#Ruta para obtener Schedules por ID
@schedule_blueprint.route('/schedule/<string:schedule_id>', methods=['GET'])
@jwt_required()
def get_schedule_by_id(schedule_id):
    try:  
         # Crear una instancia de GetscheduleByID
        getSchedule = GetScheduleByID()
        
        # Llamar al método get_schedule y pasarle el id
        schedule = getSchedule.get_schedule(schedule_id)
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(schedule)
        
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500



#Ruta para crear Schedules
@schedule_blueprint.route('/schedule', methods=['POST'])
@jwt_required()
def endpoint_query():
    try: 
        #Autenticamos con JWT y obtenemos el user_id
        current_user = get_jwt_identity()
        
        #creamos una instancia de GetUserDB y obtenemos el user
        get_user = GetUserDB()
        user = get_user.get_user(current_user)
        if not user:
            return jsonify({"msg": "Solo Usuarios registrados!"}), 403
        
        # Obtener los datos de la solicitud
        schedule_data = request.json

        
        # Crear una instancia del servicio
        servicio = ScheduleService()

        # Procesar la petición utilizando el servicio
        resultado = servicio.query(schedule_data,user)

        return resultado
    except Exception as e:
        return jsonify({"error": str(e)})



#Ruta para modificar Schedules
@schedule_blueprint.route('/schedule', methods=['PUT'])
@jwt_required()
def update_schedule():
    try:
        
        # Obtener los de la solicitud PUT en formato JSON
        update_data = request.json
        
        if not update_data["id"]:
            return jsonify({"error": "ID del schedule y datos de actualización son necesarios"}), 400
        
        # Crear una instancia de UpdateScheduleDB
        updateSchedule = UpdateScheduleDB()
        
        # Llamar al método update y pasarle la data
        response = updateSchedule.update(update_data)
        
        # Verificar el resultado de la eliminación y devolver la respuesta adecuada
        if response:
            return jsonify({"message": "Schedule actualizado correctamente."}), 200
        else:
            return jsonify({"message": "No se encontró el Schedule o no se pudo actualizar."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    


#Ruta para borrar Schedules
@schedule_blueprint.route('/schedule', methods=['DELETE'])
@jwt_required()
def delete_schedule():
    try:
        # Obtener el ID del schedule de la solicitud DELETE en formato JSON
        id = request.json.get('id')
        
        if not id:
            return jsonify({"error": "El ID del schedule es necesario."}), 400
        
        # Crear una instancia de DeleteScheduleDB
        deleteSchedule = DeleteScheduleDB()
        
        # Llamar al método delete_schedule y pasarle el ID del usuario
        response = deleteSchedule.delete_schedule(id)
        
        # Verificar el resultado de la eliminación y devolver la respuesta adecuada
        if response:
            return jsonify({"message": "Schedule eliminado correctamente."}), 200
        else:
            return jsonify({"message": "No se encontró el Schedule o no se pudo eliminar."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500