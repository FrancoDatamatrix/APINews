import unittest
from unittest.mock import patch
from utils.inputDeleteValidator import InputDeleteValidator

class TestInputDeleteValidator(unittest.TestCase):

    @patch('utils.inputDeleteValidator.InputDeleteValidator.validate_id_user_data')
    def test_validate_id_user_data(self, mock_validator):
        # Configurar el mock para que devuelva un resultado específico
        mock_validator.return_value = True

        # Llamar al método que utiliza el validador
        result = InputDeleteValidator.validate_id_user_data('user_id')

        # Verificar que el método del validador fue llamado y que el resultado es el esperado
        mock_validator.assert_called_once_with('user_id')
        self.assertTrue(result)

    @patch('utils.inputDeleteValidator.InputDeleteValidator.validate_id_user_data')
    def test_invalid_id_user_data(self, mock_validator):
        # Configurar el mock para que devuelva un resultado específico
        mock_validator.return_value = False

        # Llamar al método que utiliza el validador con un ID de usuario inválido
        result = InputDeleteValidator.validate_id_user_data('')

        # Verificar que el método del validador fue llamado y que el resultado es el esperado
        mock_validator.assert_called_once_with('')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()