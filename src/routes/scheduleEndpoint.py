from flask import jsonify, Blueprint, request
from ..services import scheduleService

schedule_blueprint = Blueprint('schedule', __name__)

@schedule_blueprint.route('/api/v1/query', methods=['POST'])
def endpoint_query():
    try:
        # Obtener los datos de la solicitud
        user_data = request.json

        
        # Crear una instancia del servicio
        servicio = scheduleService()

        # Procesar la petición utilizando el servicio
        resultado = servicio.query(user_data)

        return jsonify(resultado)
    except Exception as e:
        return jsonify({"error": str(e)})
