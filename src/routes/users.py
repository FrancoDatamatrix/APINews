from flask import jsonify,Blueprint,Response, request, make_response
from flask_jwt_extended import get_jwt_identity, jwt_required
from database.GetScheduleByUserDB import GetScheduleByUserDB
from database.GetNewsByUserDB import GetNewsByUserDB
from database.GetAllUsersDB import GetAllUserDB
from database.GetUserDB import GetUserDB
from utils.GetUserRol import GetUserRol
from database.DBMongoHelper import DBmongoHelper
from services.CreateORUpdateUserService import CreateOrUpdateUserService
from services.DeleteUserService import DeleteUserService
from bson import json_util

users_blueprint = Blueprint('/users', __name__)

# Ruta para obtener todos los usuarios
@users_blueprint.route('/users', methods=['GET'])
@jwt_required()
def get_users():
    try:  
        #Autenticamos con JWT y verificamos que sea Admin
        current_user = get_jwt_identity()
        user_role = GetUserRol.get_user_role(current_user)
        if user_role != "admin":
            return jsonify({"msg": "Solo Administradores!"}), 403
         # Crear una instancia de GetAllUserDB
        getUsers = GetAllUserDB()
        
        # Llamar al método get_all_user
        users = getUsers.get_all_users()
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(users)
        
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
# Ruta para obtener un usuario por id
@users_blueprint.route('/users/<string:user_id>', methods=['GET'])
@jwt_required()
def get_users_by_id(user_id):
    try:
        page = int(request.args.get('page', 1))
        
        # Información completa del usuario
        user_complete = {}
          
        # Crear las instancias necesarias
        getUser = GetUserDB()
        getSchedule = GetScheduleByUserDB()
        getNews = GetNewsByUserDB()
        db_helper = DBmongoHelper()
        
        # Llamar al método get_user y pasarle el id
        user_complete = getUser.get_user(user_id)
        
        # Verificar si el usuario fue encontrado
        if "error" in user_complete:
            return jsonify(user_complete), 404
        
        id = user_complete["_id"]
        
        # Llamar al método get_user_schedule y pasarle el id
        user_complete["schedules"] = getSchedule.get_user_schedule(user_complete)
        
        # Llamar al método get_user_news y pasarle el id y la página
        user_complete["news"] = getNews.get_user_news(user_complete, page=page)
    
        # Convertir el resultado a un arreglo que contenga un solo objeto
        response_data = [user_complete]
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(response_data)
    
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
            # Asegurarse de cerrar la conexión después de completar la operación
            db_helper.close()
    

    
    
# Ruta para crear un usuario
@users_blueprint.route('/users', methods=['POST'])
@jwt_required()
def create_user():
    try:
        #Autenticamos con JWT y verificamos que sea Admin
        current_user = get_jwt_identity()
        user_role = GetUserRol.get_user_role(current_user)
        if user_role != "admin":
            return jsonify({"msg": "Solo Administradores!"}), 403
        
        # Obtener los datos del usuario de la solicitud
        user_data = request.json

         # Crear una instancia del service
        createOrUpdateUS = CreateOrUpdateUserService()
        
        # Llamar al método create_user y pasarle los datos del usuario
        response = createOrUpdateUS.create_or_update_user(user_data)
        
        # Devolver la respuesta
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
    
# Ruta para eliminar un usuario
@users_blueprint.route('/users', methods=['DELETE'])
@jwt_required()
def delete_user():
    try:
        #verificamos que sea admin antes de crear un nuevo usuario
        current_user = get_jwt_identity()
        user_role = GetUserRol.get_user_role(current_user)
        if user_role != 'admin':
            return jsonify({"msg": "Solo Administradores!"}), 403
        # Obtener el ID del usuario de la solicitud DELETE en formato JSON
        id = request.json.get('id')
        
        if not id:
            return jsonify({"error": "El ID del usuario es necesario."}), 400
        
        # Obtener los datos del usuario de la solicitud DELETE en formato JSON
        user_id = request.json.get("id")
        usuario = request.json.get("usuario")
        
        # Crear una instancia de DeleteUserService
        deleteUserService = DeleteUserService()
        
        # Llamar al método delete_user y pasarle los datos del usuario
        response = deleteUserService.delete_user(user_id, usuario)
        
        # Verificar el resultado de la eliminación y devolver la respuesta adecuada
        if response:
            return response
        else:
            return jsonify({"message": "No se encontró el usuario o no se pudo eliminar."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500