from flask import jsonify,Blueprint, request
from ..services import CreateOrUpdateUserService

create_update_blueprint = Blueprint('create_update', __name__)

# Ruta para crear un nuevo usuario
@create_update_blueprint.route('/api/v1/create-update-users', methods=['POST'])
def create_user():
    try:
        #Autenticacio para cada request (flask oAuthlib)
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