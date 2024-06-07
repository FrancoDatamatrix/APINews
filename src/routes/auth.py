from flask import Blueprint, request, jsonify, make_response
from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, get_jwt_identity,set_access_cookies
from utils.credencialsValidator import CredencialsValidator
import logging

auth_blueprint = Blueprint('auth', __name__)


#Ruta para login
@auth_blueprint.route('/login', methods=['POST'])
def login():
    logging.info(request.json.get('usuario', None))
    usuario = request.json.get('usuario', None)
    contraseña = request.json.get('contraseña', None)

    user = CredencialsValidator.validar_credenciales(usuario, contraseña)
    if not user:
        return jsonify({"msg": "usuario o contraseña incorrectos"}), 401
     
    username = user["usuario"]
    access_token = create_access_token(identity=username)
    response = make_response(jsonify({
            "msg": "Login successful"
        }))
    
    set_access_cookies(response, access_token)
    return response



@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response