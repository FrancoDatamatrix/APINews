import unittest
from unittest.mock import patch
from utils.queryInputValidator import QueryValidator

class TestQueryValidator(unittest.TestCase):

    def test_validate_user_data(self):
        # Caso de prueba 1: datos de usuario completos
        user_data_complete = {'usuario': 'test_user', 'contraseña': 'password', 'hora': '12:00', 'palabras': ['hola', 'adios'], 'lugar': 'casa'}
        resultado1 = QueryValidator.validate_user_data(user_data_complete)
        self.assertTrue(resultado1)

        # Caso de prueba 2: falta el lugar en los datos de usuario
        user_data_missing_lugar = {'usuario': 'test_user', 'contraseña': 'password', 'hora': '12:00', 'palabras': ['hola', 'adios']}
        resultado2 = QueryValidator.validate_user_data(user_data_missing_lugar)
        self.assertFalse(resultado2)

        # Caso de prueba 3: falta la contraseña en los datos de usuario
        user_data_missing_contraseña = {'usuario': 'test_user', 'hora': '12:00', 'palabras': ['hola', 'adios'], 'lugar': 'casa'}
        resultado3 = QueryValidator.validate_user_data(user_data_missing_contraseña)
        self.assertFalse(resultado3)

if __name__ == '__main__':
    unittest.main()