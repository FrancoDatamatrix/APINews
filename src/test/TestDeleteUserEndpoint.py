import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from routes.DeleteUser import delete_blueprint 

# Crear una instancia de Flask para pruebas
app = Flask(__name__)
app.register_blueprint(delete_blueprint)
app.config['TESTING'] = True

class TestDeleteUserEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    @patch('routes.DeleteUser.DeleteUserService')
    def test_delete_user_success(self, mock_delete_user_service):
        # Configurar el mock
        mock_service_instance = MagicMock()
        with app.app_context():
            mock_service_instance.delete_user.return_value = jsonify({"message": "Usuario eliminado exitosamente", "user_id": "test_user_id"}), 200
        mock_delete_user_service.return_value = mock_service_instance

        # Realizar la solicitud DELETE
        response = self.app.delete('/api/v1/delete-user', json={"id": "test_user_id"})

        # Verificar los resultados
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Usuario eliminado exitosamente", "user_id": "test_user_id"})
        mock_service_instance.delete_user.assert_called_once_with("test_user_id")

    @patch('routes.DeleteUser.DeleteUserService')
    def test_delete_user_not_found(self, mock_delete_user_service):
        # Configurar el mock para devolver un error de usuario no encontrado
        mock_service_instance = MagicMock()
        with app.app_context():
            mock_service_instance.delete_user.return_value = jsonify({"error": "No se encontró ningún usuario con el ID proporcionado"}), 400
        mock_delete_user_service.return_value = mock_service_instance

        # Realizar la solicitud DELETE
        response = self.app.delete('/api/v1/delete-user', json={"id": "non_existing_user_id"})

        # Verificar los resultados
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {"error": "No se encontró ningún usuario con el ID proporcionado"})
        mock_service_instance.delete_user.assert_called_once_with("non_existing_user_id")

    @patch('routes.DeleteUser.DeleteUserService')
    def test_delete_user_missing_id(self, mock_delete_user_service):
        # Realizar la solicitud DELETE sin ID
        response = self.app.delete('/api/v1/delete-user', json={})

        # Verificar los resultados
        self.assertEqual(response.status_code, 500)
        self.assertIn("error", response.json)

    @patch('routes.DeleteUser.DeleteUserService')
    def test_delete_user_exception(self, mock_delete_user_service):
        # Configurar el mock para lanzar una excepción
        mock_service_instance = MagicMock()
        with app.app_context():
            mock_service_instance.delete_user.side_effect = Exception("Unexpected error")
        mock_delete_user_service.return_value = mock_service_instance

        # Realizar la solicitud DELETE
        response = self.app.delete('/api/v1/delete-user', json={"id": "test_user_id"})

        # Verificar los resultados
        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {"error": "Unexpected error"})
        mock_service_instance.delete_user.assert_called_once_with("test_user_id")

if __name__ == '__main__':
    unittest.main()