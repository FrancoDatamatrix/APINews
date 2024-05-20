import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from routes.CreateORUpdateUser import create_update_blueprint  # Asegúrate de que la ruta sea correcta

# Crear una instancia de Flask para pruebas
app = Flask(__name__)
app.register_blueprint(create_update_blueprint)
app.config['TESTING'] = True

class TestCreateUpdateUserEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('routes.CreateORUpdateUser.CreateOrUpdateUserService')
    def test_create_user_success(self, MockCreateOrUpdateUserService):
        # Configurar el mock
        mock_service_instance = MagicMock()
        with app.app_context():
            mock_service_instance.create_or_update_user.return_value = jsonify({"message": "Usuario creado exitosamente", "user_id": "test_user_id"}), 201
        MockCreateOrUpdateUserService.return_value = mock_service_instance

        # Realizar la solicitud POST
        response = self.app.post('/api/v1/create-update-users', json={
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123",
            "api_key": "valid_api_key"
        })

        # Verificar los resultados
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Usuario creado exitosamente", "user_id": "test_user_id"})
        mock_service_instance.create_or_update_user.assert_called_once_with({
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123",
            "api_key": "valid_api_key"
        })

    @patch('routes.CreateORUpdateUser.CreateOrUpdateUserService')
    def test_create_user_invalid_data(self, MockCreateOrUpdateUserService):
        # Configurar el mock para devolver un error de validación
        mock_service_instance = MagicMock()
        with app.app_context():
            mock_service_instance.create_or_update_user.return_value = jsonify({"error": "Api_key, correo y contraseña son obligatorios"}), 400
        MockCreateOrUpdateUserService.return_value = mock_service_instance

        # Realizar la solicitud POST con datos inválidos
        response = self.app.post('/api/v1/create-update-users', json={
            "usuario": "test_user"
            # Falta correo, contraseña y api_key
        })

        # Verificar los resultados
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "Api_key, correo y contraseña son obligatorios"})
        mock_service_instance.create_or_update_user.assert_called_once_with({
            "usuario": "test_user"
        })

    @patch('routes.CreateORUpdateUser.CreateOrUpdateUserService')
    def test_create_user_exception(self, MockCreateOrUpdateUserService):
        # Configurar el mock para lanzar una excepción
        mock_service_instance = MagicMock()
        with app.app_context():
            mock_service_instance.create_or_update_user.side_effect = Exception("Unexpected error")
        MockCreateOrUpdateUserService.return_value = mock_service_instance

        # Realizar la solicitud POST
        response = self.app.post('/api/v1/create-update-users', json={
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123",
            "api_key": "valid_api_key"
        })

        # Verificar los resultados
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Unexpected error"})
        mock_service_instance.create_or_update_user.assert_called_once_with({
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123",
            "api_key": "valid_api_key"
        })

if __name__ == '__main__':
    unittest.main()