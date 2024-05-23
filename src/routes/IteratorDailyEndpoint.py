from flask import jsonify, Blueprint
from helper.iteratoDailyHelper import tarea

start_schedule_blueprint = Blueprint('start_schedule', __name__)

@start_schedule_blueprint.route('/', methods=['GET'])
def endpoint_query():
    try:
        print("ejecutando script de ejecucion diaria...")
        result = "funciono 200" if tarea() else "fallo 400"
        return result
    except Exception as e:
        return jsonify({"error": str(e)})