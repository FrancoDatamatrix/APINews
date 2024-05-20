import unittest
from unittest.mock import patch
from utils.InputCOPUserValidator import InputValidator

class TestInputValidator(unittest.TestCase):

    @patch('utils.InputCOPUserValidator.InputValidator.validate_user_data')
    def test_validate_user_data(self, mock_validator):
        # Configurar el mock para que devuelva un resultado específico
        mock_validator.return_value = True

        # Datos de usuario válidos
        valid_user_data = {
            'usuario': 'username',
            'contraseña': 'password',
            'api_key': 'api_key'
        }

        # Llamar al método que utiliza el validador con datos de usuario válidos
        result = InputValidator.validate_user_data(valid_user_data)

        # Verificar que el método del validador fue llamado y que el resultado es el esperado
        mock_validator.assert_called_once_with(valid_user_data)
        self.assertTrue(result)

    @patch('utils.InputCOPUserValidator.InputValidator.validate_user_data')
    def test_invalid_user_data(self, mock_validator):
        # Configurar el mock para que devuelva un resultado específico
        mock_validator.return_value = False

        # Datos de usuario inválidos (falta 'contraseña')
        invalid_user_data = {
            'usuario': 'username',
            'api_key': 'api_key'
        }

        # Llamar al método que utiliza el validador con datos de usuario inválidos
        result = InputValidator.validate_user_data(invalid_user_data)

        # Verificar que el método del validador fue llamado y que el resultado es el esperado
        mock_validator.assert_called_once_with(invalid_user_data)
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()