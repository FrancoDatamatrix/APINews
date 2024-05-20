import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from services.CreateORUpdateUserService import CreateOrUpdateUserService 

# Crear una instancia de Flask para pruebas
app = Flask(__name__)

class TestCreateOrUpdateUserService(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.service = CreateOrUpdateUserService()

    @patch('services.CreateORUpdateUserService.InputValidator.validate_user_data')
    @patch('services.CreateORUpdateUserService.APIKeyValidator.validate_api_key')
    @patch('services.CreateORUpdateUserService.GetUserDB')
    @patch('services.CreateORUpdateUserService.UpdateUserDB')
    @patch('services.CreateORUpdateUserService.CreateUserDB')
    def test_create_user_success(self, mock_create_user_db, mock_update_user_db, mock_get_user_db, mock_validate_api_key, mock_validate_user_data):
        # Configurar los mocks
        mock_validate_user_data.return_value = True
        mock_validate_api_key.return_value = True
        mock_get_user_db.return_value.get_user.return_value = None
        mock_create_user_db.return_value.create_user.return_value = "new_user_id"

        user_data = {
            "api_key": "valid_api_key",
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123"
        }

        # Realizar la solicitud
        with app.app_context():
            response = self.service.create_or_update_user(user_data)
        
        # Verificar los resultados
        self.assertEqual(response[1], 201)
        self.assertEqual(response[0].json, {"message": "Usuario creado exitosamente", "user_id": "new_user_id"})
        mock_create_user_db.return_value.create_user.assert_called_once_with(user_data)
    
    @patch('services.CreateORUpdateUserService.InputValidator.validate_user_data')
    @patch('services.CreateORUpdateUserService.APIKeyValidator.validate_api_key')
    @patch('services.CreateORUpdateUserService.GetUserDB')
    @patch('services.CreateORUpdateUserService.UpdateUserDB')
    @patch('services.CreateORUpdateUserService.CreateUserDB')
    def test_update_user_success(self, mock_create_user_db, mock_update_user_db, mock_get_user_db, mock_validate_api_key, mock_validate_user_data):
        # Configurar los mocks
        mock_validate_user_data.return_value = True
        mock_validate_api_key.return_value = True
        existing_user = {"_id": "existing_user_id"}
        mock_get_user_db.return_value.get_user.return_value = existing_user

        user_data = {
            "api_key": "valid_api_key",
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123"
        }

        # Realizar la solicitud
        with app.app_context():
            response = self.service.create_or_update_user(user_data)
        
        # Verificar los resultados
        self.assertEqual(response[1], 200)
        self.assertEqual(response[0].json, {"message": "Usuario actualizado exitosamente", "user_id": "existing_user_id"})
        mock_update_user_db.return_value.update_user.assert_called_once_with("existing_user_id", user_data)

    @patch('services.CreateORUpdateUserService.InputValidator.validate_user_data')
    @patch('services.CreateORUpdateUserService.APIKeyValidator.validate_api_key')
    @patch('services.CreateORUpdateUserService.GetUserDB')
    @patch('services.CreateORUpdateUserService.UpdateUserDB')
    @patch('services.CreateORUpdateUserService.CreateUserDB')
    def test_invalid_user_data(self, mock_create_user_db, mock_update_user_db, mock_get_user_db, mock_validate_api_key, mock_validate_user_data):
        # Configurar los mocks
        mock_validate_user_data.return_value = False

        user_data = {
            "api_key": "valid_api_key",
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123"
        }

        # Realizar la solicitud
        with app.app_context():
            response = self.service.create_or_update_user(user_data)
        
        # Verificar los resultados
        self.assertEqual(response[1], 400)
        self.assertEqual(response[0].json, {"error": "Api_key, correo y contraseña son obligatorios"})
        mock_create_user_db.return_value.create_user.assert_not_called()
        mock_update_user_db.return_value.update_user.assert_not_called()

    @patch('services.CreateORUpdateUserService.InputValidator.validate_user_data')
    @patch('services.CreateORUpdateUserService.APIKeyValidator.validate_api_key')
    @patch('services.CreateORUpdateUserService.GetUserDB')
    @patch('services.CreateORUpdateUserService.UpdateUserDB')
    @patch('services.CreateORUpdateUserService.CreateUserDB')
    def test_invalid_api_key(self, mock_create_user_db, mock_update_user_db, mock_get_user_db, mock_validate_api_key, mock_validate_user_data):
        # Configurar los mocks
        mock_validate_user_data.return_value = True
        mock_validate_api_key.return_value = False

        user_data = {
            "api_key": "invalid_api_key",
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123"
        }

        # Realizar la solicitud
        with app.app_context():
            response = self.service.create_or_update_user(user_data)
        
        # Verificar los resultados
        self.assertEqual(response[1], 401)
        self.assertEqual(response[0].json, {"error": "Api_key invalida"})
        mock_create_user_db.return_value.create_user.assert_not_called()
        mock_update_user_db.return_value.update_user.assert_not_called()

    @patch('services.CreateORUpdateUserService.InputValidator.validate_user_data')
    @patch('services.CreateORUpdateUserService.APIKeyValidator.validate_api_key')
    @patch('services.CreateORUpdateUserService.GetUserDB')
    @patch('services.CreateORUpdateUserService.UpdateUserDB')
    @patch('services.CreateORUpdateUserService.CreateUserDB')
    def test_exception_handling(self, mock_create_user_db, mock_update_user_db, mock_get_user_db, mock_validate_api_key, mock_validate_user_data):
        # Configurar los mocks
        mock_validate_user_data.return_value = True
        mock_validate_api_key.return_value = True
        mock_get_user_db.return_value.get_user.side_effect = Exception("Database error")

        user_data = {
            "api_key": "valid_api_key",
            "usuario": "test_user",
            "correo": "test_user@example.com",
            "contraseña": "password123"
        }

        # Realizar la solicitud
        with app.app_context():
            response = self.service.create_or_update_user(user_data)
        
        # Verificar los resultados
        self.assertEqual(response[1], 500)
        self.assertEqual(response[0].json, {"error": "Database error"})
        mock_create_user_db.return_value.create_user.assert_not_called()
        mock_update_user_db.return_value.update_user.assert_not_called()

if __name__ == '__main__':
    unittest.main()