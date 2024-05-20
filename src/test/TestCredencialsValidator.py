import unittest
from unittest.mock import patch, MagicMock
from database.GetUserDB import GetUserDB
import bcrypt
from utils.credencialsValidator import CredencialsValidator

class TestCredencialsValidator(unittest.TestCase):

    @patch('utils.credencialsValidator.GetUserDB')
    @patch('utils.credencialsValidator.bcrypt.checkpw')
    def test_validar_credenciales(self, mock_checkpw, mock_get_user_db):
        # Configurar mocks
        mock_user_data = {'usuario': 'test_user', 'contraseña': 'hashed_password'}
        mock_get_user_db_instance = MagicMock()
        mock_get_user_db_instance.get_user.return_value = mock_user_data
        mock_get_user_db.return_value = mock_get_user_db_instance
        mock_checkpw.return_value = True

        # Llamar a la función a testear
        resultado = CredencialsValidator.validar_credenciales('test_user', 'password')

        # Verificar el comportamiento y los resultados
        mock_get_user_db_instance.get_user.assert_called_once_with('test_user')
        mock_checkpw.assert_called_once_with('password'.encode('utf-8'), 'hashed_password'.encode('utf-8'))
        self.assertEqual(resultado, mock_user_data)

if __name__ == '__main__':
    unittest.main()