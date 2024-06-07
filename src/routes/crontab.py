from flask import Blueprint, request, jsonify
from flask_jwt_extended import get_jwt_identity, jwt_required
from utils.GetUserRol import GetUserRol
from crontab import CronTab


cron_blueprint = Blueprint('cron', __name__)

#Nombre del comando del cronjon que necesitamos
COMMAND = "python3 /home/data-news/APINews/src/rotes/iterator.py"

#Ruta para obtener el Cronjob
@cron_blueprint.route('/cronjob', methods=['GET'])
# @jwt_required()
def get_cronjob():
    #Autenticamos con JWT y verificamos que sea Admin
    # current_user = get_jwt_identity()
    # user_role = GetUserRol.get_user_role(current_user)
    # if user_role != "admin":
    #     return jsonify({"msg": "Solo Administradores!"}), 403
    
    cron = CronTab()
    for job in cron:
        if job.command == COMMAND:
            return jsonify({
                'minute': job.minute.render(),
                'hour': job.hour.render(),
                'day_of_month': job.day.render(),
                'month': job.month.render(),
                'day_of_week': job.dow.render()
            })
    return jsonify({'error': 'Cronjob no encontrado'})



#Ruta para modificar el Cronjob
@cron_blueprint.route('/cronjob', methods=['PUT'])
@jwt_required()
def update_cronjob():
    #Autenticamos con JWT y verificamos que sea Admin
    current_user = get_jwt_identity()
    user_role = GetUserRol.get_user_role(current_user)
    if user_role != "admin":
        return jsonify({"msg": "Solo Administradores!"}), 403
        
    data = request.get_json()
    new_hour = data.get('horas')
    new_day_of_month = data.get('dias')
    new_month = data.get('meses')
    new_day_of_week = data.get('dias_de_la_semana')

    cron = CronTab(user=True)
    job_updated = False
    for job in cron:
        if job.command == COMMAND:
            job.hour.on(new_hour)
            job.day.on(new_day_of_month)
            job.month.on(new_month)
            job.dow.on(new_day_of_week)
            job_updated = True
            cron.write()
            break

    if job_updated:
        return jsonify({'message': 'Cronjob actualizado correctamente'})
    else:
        return jsonify({'error': 'Cronjob no encontrado'}), 404