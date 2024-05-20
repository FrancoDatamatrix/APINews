import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify, request
from services.scheduleService import ScheduleService

class TestScheduleService(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True

    @patch('services.scheduleService.UpdateUserDB')
    @patch('services.scheduleService.CreateScheduleDB')
    @patch('services.scheduleService.CredencialsValidator')
    def test_query(self, mock_credencials_validator, mock_create_schedule_db, mock_update_user_db):
        # Configurar mocks
        mock_credencials_validator.validar_credenciales.return_value = {"_id": "user_id"}
        mock_update_user_db_instance = MagicMock()
        mock_update_user_db_instance.update_user.return_value = True
        mock_update_user_db.return_value = mock_update_user_db_instance
        mock_create_schedule_db_instance = MagicMock()
        mock_create_schedule_db_instance.create_schedule.return_value = "schedule_id"
        mock_create_schedule_db.return_value = mock_create_schedule_db_instance

        # Simular la solicitud POST con datos de usuario válidos
        with self.app.test_request_context('/api/v1/query', method='POST', json={
            "usuario": "test_user",
            "contraseña": "password",
            "hora": "12:00",
            "palabras": "hola, adios",
            "lugar": "casa"
        }):
            service = ScheduleService()
            response = service.query(request.json)

            # Verificar el comportamiento y los resultados
            mock_credencials_validator.validar_credenciales.assert_called_once_with("test_user", "password")
            mock_update_user_db_instance.update_user.assert_called_once_with("user_id", {"palabras": "hola, adios", "lugar": "casa"})
            mock_create_schedule_db_instance.create_schedule.assert_called_once_with("user_id", "12:00", "hola, adios", "casa")
            self.assertEqual(response[1], 200)
            

if __name__ == '__main__':
    unittest.main()