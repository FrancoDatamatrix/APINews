from flask import jsonify, Blueprint, request
from ..services import DeleteUserService

delete_blueprint = Blueprint('delete', __name__)

# Ruta para crear un nuevo usuario
@delete_blueprint.route('/api/v1/delete-users', methods=['DELETE'])

def delete_user():
    try:
        # Obtener los datos del usuario de la solicitud DELETE en formato JSON
        user_data = request.json
        
        # Crear una instancia de UsersEndpoint
        deleteUserService = DeleteUserService()
        
        # Llamar al método delete_user y pasarle los datos del usuario
        response = deleteUserService.delete_user(user_data['id'])
        
        # Devolver la respuesta
        return response
    except Exception as e: 
        return jsonify({"error": str(e)}), 500