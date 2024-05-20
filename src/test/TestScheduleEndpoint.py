import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, jsonify
from routes.scheduleEndpoint import schedule_blueprint

class TestScheduleEndpoint(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(schedule_blueprint)
        self.app.config['TESTING'] = True

    @patch('routes.scheduleEndpoint.ScheduleService')  # Asegúrate de que el parcheo sea correcto
    def test_endpoint_query(self, mock_schedule_service):
        # Configurar mocks
        mock_service_instance = MagicMock()

        with self.app.app_context():
            mock_service_instance.query.return_value = jsonify({"schedule_id": "123", "mensaje": "Petición recibida correctamente"})

        mock_schedule_service.return_value = mock_service_instance

        # Simular la solicitud POST al endpoint con el contexto de la aplicación
        with self.app.test_client() as client:
            response = client.post('/api/v1/query', json={
                "usuario": "test_user",
                "contraseña": "password",
                "hora": "12:00",
                "palabras": "hola, adios",
                "lugar": "casa"
            })

        # Verificar el comportamiento y los resultados
        mock_schedule_service.assert_called_once()
        mock_service_instance.query.assert_called_once_with({
            "usuario": "test_user",
            "contraseña": "password",
            "hora": "12:00",
            "palabras": "hola, adios",
            "lugar": "casa"
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"schedule_id": "123", "mensaje": "Petición recibida correctamente"})

if __name__ == '__main__':
    unittest.main()