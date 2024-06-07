from flask import jsonify, Blueprint, Response, request
from flask_jwt_extended import jwt_required
from database.GetAllNewsDB import GetAllNewsDB
from database.GetNewsDB import GetNewsDB
from database.DeleteNewsGoogleDB import DeleteNewsDB
from bson import json_util

news_blueprint = Blueprint('news', __name__)

# Ruta para obtener todas las noticias
@news_blueprint.route('/news', methods=['GET'])
@jwt_required()
def get_news():
    try:
        # Obtener los parámetros de paginacion de la solicitud GET
        page = int(request.args.get('page', 1))
        
        # Crear una instancia de GetAllNewsDB
        getNews = GetAllNewsDB()
        
        # Llamar al método get_all_news
        news = getNews.get_all_news(page=page)
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(news)
        
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

# Ruta para obtener una noticia por id
@news_blueprint.route('/news/<string:news_id>', methods=['GET'])
@jwt_required()
def get_news_by_id(news_id):
    try:  
         # Crear una instancia de GetNewsDB
        getNews = GetNewsDB()
        
        # Llamar al método get_news y pasarle el id
        schedule = getNews.get_news(news_id)
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(schedule)
        
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

# Ruta para eliminar una noticias
@news_blueprint.route('/news', methods=['DELETE'])
@jwt_required()
def delete_news():
    try:
        # Obtener el ID de la noticia de la solicitud DELETE en formato JSON
        id = request.json.get('id')
        
        if not id:
            return jsonify({"error": "El ID de la noticia es necesario."}), 400
        
        # Crear una instancia de DeleteNewsDB
        deleteNews = DeleteNewsDB()
        
        # Llamar al método delete_news_by_id y pasarle el ID del usuario
        response = deleteNews.delete_news_by_id(id)
        
        # Verificar el resultado de la eliminación y devolver la respuesta adecuada
        if response:
            return jsonify({"message": "Noticia eliminada correctamente."}), 200
        else:
            return jsonify({"message": "No se encontró la noticia o no se pudo eliminar."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500