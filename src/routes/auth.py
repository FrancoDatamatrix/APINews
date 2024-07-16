from flask import Blueprint, request, jsonify, make_response,Response
from flask_jwt_extended import create_access_token, create_refresh_token, unset_jwt_cookies, jwt_required, get_jwt_identity,set_access_cookies
from utils.credencialsValidator import CredencialsValidator

from bson import json_util
import logging

auth_blueprint = Blueprint('auth', __name__)


#Ruta para login
@auth_blueprint.route('/login', methods=['POST'])
def login():
    usuario = request.json.get('usuario', None)
    contraseña = request.json.get('contraseña', None)

    user = CredencialsValidator.validar_credenciales(usuario, contraseña)
    if not user:
        return jsonify({"msg": "usuario o contraseña incorrectos"}), 401
     
    username = user["usuario"]
    
    user_response = {
        "usuario": username,
        "role": user["rol"]
    }
    access_token = create_access_token(identity=username)
    
    response = make_response(jsonify({
            "msg": "Login successful",
            "usuario": user_response
        }))
    
    set_access_cookies(response, access_token)
    return response



@auth_blueprint.route('/logout', methods=['POST'])
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response