from flask import Flask
import unittest
from unittest.mock import MagicMock
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname("D:/Desarrollo web/Proyecto Api rest phyton/API REST NEWS/src"))))
from src.services.user_services import UsersEndpoint

class TestUsersEndpoint(unittest.TestCase):
    def setUp(self):
        # Creamos un objeto UsersEndpoint para cada prueba
        self.db_url = "your_db_url"
        self.db_name = "your_db_name"
        self.users_endpoint = UsersEndpoint(self.db_url, self.db_name)

        # Creamos una aplicación Flask para las pruebas
        self.app = Flask(__name__)

    def test_create_user_success(self):
        # Configuramos una solicitud de ejemplo con un usuario válido
        request = MagicMock()
        request.json = {'email': 'test@example.com', 'password': '123456'}
        
        # Configuramos un mock para UserManager.create_user que devuelve un ID de usuario
        user_id = 'user_id'
        self.users_endpoint.user_manager.create_user = MagicMock(return_value=user_id)

        # Ejecutamos el código dentro del contexto de la aplicación
        with self.app.app_context():
            # Llamamos al método create_user del endpoint
            response = self.users_endpoint.create_user(request)

            # Verificamos que se devuelva el código de estado 201 (Created)
            self.assertEqual(response[1], 201)

            # Verificamos que se devuelva el mensaje y el ID de usuario correctos
            expected_response = {"message": "Usuario creado exitosamente", "user_id": user_id}
            self.assertEqual(response[0].json, expected_response)

    def test_create_user_missing_fields(self):
        # Configuramos una solicitud de ejemplo con un usuario que falta un campo obligatorio
        request = MagicMock()
        request.json = {'password': '123456'}

        # Ejecutamos el código dentro del contexto de la aplicación
        with self.app.app_context():
            # Llamamos al método create_user del endpoint
            response = self.users_endpoint.create_user(request)

            # Verificamos que se devuelva el código de estado 400 (Bad Request)
            self.assertEqual(response[1], 400)

            # Verificamos que se devuelva el mensaje de error correcto
            expected_response = {"error": "Correo y contraseña son obligatorios"}
            self.assertEqual(response[0].json, expected_response)

if __name__ == '__main__':
    unittest.main()