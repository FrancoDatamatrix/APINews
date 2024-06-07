from flask import jsonify
from utils.InputCOPUserValidator import InputValidator
from utils.RolValidator import RolValidator
from database.GetUserDB import GetUserDB
from database.UpdateUserDB import UpdateUserDB
from database.CreateUserDB import CreateUserDB
import logging

class CreateOrUpdateUserService:
    def create_or_update_user(self, user_data):
        try:
            
            # Verificar que se proporcionen los datos utilizando InputValidator
            if not InputValidator.validate_user_data(user_data):
                return jsonify({"error": "Correo, contraseña y rol son obligatorios"}), 400
            
            
            #Verificacion de rol
            if not RolValidator.validate_rol(user_data["rol"]):
                return jsonify({"error": "Rol invalido"}), 401

            # Verificar si el usuario ya existe
            get_user_db = GetUserDB()
            existing_user = get_user_db.get_user(user_data['usuario'])
            
            if existing_user:
                logging.info(f"El usuario existe ${existing_user}")
                # Si el usuario ya existe, actualízalo
                update_user_db = UpdateUserDB()
                user_id = existing_user['_id']
                update_user_db.update_user(user_id, user_data)
                return jsonify({"message": "Usuario actualizado exitosamente", "user_id": str(user_id)}), 200
            else:
                # Si el usuario no existe, créalo
                logging.info("El usuario no existe")
                create_user_db = CreateUserDB()
                user_id = create_user_db.create_user(user_data)
                return jsonify({"message": "Usuario creado exitosamente", "user_id": str(user_id)}), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

