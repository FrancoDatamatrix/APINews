from flask import jsonify, Blueprint, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.GetAllNewsDB import GetAllNewsDB
from database.GetNewsDB import GetNewsDB
from database.DeleteNewsGoogleDB import DeleteNewsDB
from database.GetFilteredNewsDB import GetFilteredNewsDB
from utils.GetUserRol import GetUserRol
from bson import json_util

news_blueprint = Blueprint('news', __name__)

# Ruta para obtener y filtrar las noticias
@news_blueprint.route('/news', methods=['GET'])
@jwt_required()
def get_news():
    try:
        # Obtener los parámetros de la solicitud GET
        page = int(request.args.get('page', 1))
        page_size = int(request.args.get('page_size', 1))
        tema = request.args.get('tema')
        usuario_id = request.args.get('id')

        # Autenticar con JWT y verificar si es Admin
        current_user = get_jwt_identity()
        user_role = GetUserRol.get_user_role(current_user)
        
        if user_role != "admin" and not usuario_id:
            return jsonify({"msg": "ID es obligatorio para usuarios que no son administradores!"}), 403
        
        if tema or usuario_id:
            # Crear una instancia de GetFilteredNewsDB
            getNews = GetFilteredNewsDB()
            
            # Llamar al método get_filtered_news con los parámetros obtenidos
            news = getNews.get_filtered_news(tema=tema, usuario_id=usuario_id, page=page, page_size=page_size, sort_by='timestamp', sort_order=-1)
        else:
            # Crear una instancia de GetAllNewsDB
            getNews = GetAllNewsDB()
            
            # Llamar al método get_all_news
            news = getNews.get_all_news(page=page, page_size=page_size,sort_by='timestamp', sort_order=-1)
        
        # Convertir los resultados a JSON usando json_util
        response = json_util.dumps(news)
        
        # Devolver la respuesta
        return Response(response, mimetype='application/json')
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    

# Ruta para obtener una noticia por id
#GET /news/asdas78687asd56
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
        # Obtener la lista de noticias seleccionadas de la solicitud DELETE en formato JSON
        selected_news = request.json.get('selectedNews')
        print(f"selected_news: {selected_news}")  # Log para depuración
        if not selected_news:
            return jsonify({"error": "La lista de noticias seleccionadas es necesaria."}), 400
        
        # Crear una instancia de DeleteNewsDB
        deleteNews = DeleteNewsDB()
        
         # Convertir news_id a entero
        for news_item in selected_news:
            news_item['news_id'] = int(news_item['news_id'])
        
        # Llamar al método delete_news_by_id y pasarle la lista de noticias seleccionadas
        response = deleteNews.delete_news_by_id(selected_news)
        
        # Verificar el resultado de la eliminación y devolver la respuesta adecuada
        if response:
            return jsonify({"message": "Noticias eliminadas correctamente."}), 200
        else:
            return jsonify({"message": "No se encontraron las noticias o no se pudieron eliminar."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500