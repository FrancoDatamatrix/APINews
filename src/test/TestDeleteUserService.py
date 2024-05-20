import unittest
from unittest.mock import patch, MagicMock
from flask import Flask
from services.DeleteUserService import DeleteUserService  

# Crear una instancia de Flask para pruebas
app = Flask(__name__)

class TestDeleteUserService(unittest.TestCase):

    @patch('services.DeleteUserService.DeleteUserDB')
    @patch('services.DeleteUserService.StopScheduleDB')
    @patch('services.DeleteUserService.InputDeleteValidator.validate_id_user_data')
    def test_delete_user_success(self, mock_validate_id, mock_stop_schedule_db, mock_delete_user_db):
        # Configurar los mocks
        mock_validate_id.return_value = True
        mock_delete_user_db.return_value.delete_user_by_id.return_value = 1
        mock_stop_schedule_db.return_value.stop_schedule.return_value = 3

        # Instanciar el servicio
        service = DeleteUserService()

        # Realizar la solicitud
        with app.test_request_context():
            response = service.delete_user(123)
        
        # Verificar los resultados
        self.assertEqual(response[1], 200)
        self.assertEqual(response[0].json, {
            "message": "Usuario eliminado exitosamente",
            "user_id": 123,
            "deleted_schedules_count": 3
        })

    @patch('services.DeleteUserService.DeleteUserDB')
    @patch('services.DeleteUserService.StopScheduleDB')
    @patch('services.DeleteUserService.InputDeleteValidator.validate_id_user_data')
    def test_delete_user_invalid_id(self, mock_validate_id, mock_stop_schedule_db, mock_delete_user_db):
        # Configurar los mocks
        mock_validate_id.return_value = False

        # Instanciar el servicio
        service = DeleteUserService()

        # Realizar la solicitud
        with app.test_request_context():
            response = service.delete_user(123)
        
        # Verificar los resultados
        self.assertEqual(response[1], 400)
        self.assertEqual(response[0].json, {
            "error": "Se requiere el ID del usuario"
        })

    @patch('services.DeleteUserService.DeleteUserDB')
    @patch('services.DeleteUserService.StopScheduleDB')
    @patch('services.DeleteUserService.InputDeleteValidator.validate_id_user_data')
    def test_delete_user_not_found(self, mock_validate_id, mock_stop_schedule_db, mock_delete_user_db):
        # Configurar los mocks
        mock_validate_id.return_value = True
        mock_delete_user_db.return_value.delete_user_by_id.return_value = 0

        # Instanciar el servicio
        service = DeleteUserService()

        # Realizar la solicitud
        with app.test_request_context():
            response = service.delete_user(123)
        
        # Verificar los resultados
        self.assertEqual(response[1], 400)
        self.assertEqual(response[0].json, {
            "error": "No se encontró ningún usuario con el ID proporcionado"
        })

    @patch('services.DeleteUserService.DeleteUserDB')
    @patch('services.DeleteUserService.StopScheduleDB')
    @patch('services.DeleteUserService.InputDeleteValidator.validate_id_user_data')
    def test_delete_user_exception(self, mock_validate_id, mock_stop_schedule_db, mock_delete_user_db):
        # Configurar los mocks
        mock_validate_id.return_value = True
        mock_delete_user_db.return_value.delete_user_by_id.side_effect = Exception('Database error')

        # Instanciar el servicio
        service = DeleteUserService()

        # Realizar la solicitud
        with app.test_request_context():
            response = service.delete_user(123)
        
        # Verificar los resultados
        self.assertEqual(response[1], 500)
        self.assertEqual(response[0].json, {
            "error": "Database error"
        })

if __name__ == '__main__':
    unittest.main()