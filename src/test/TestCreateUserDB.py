import unittest
from unittest.mock import patch, MagicMock
import bcrypt
from database.DBMongoHelper import DBmongoHelper
from database.CreateUserDB import CreateUserDB

class TestCreateUserDB(unittest.TestCase):
    @patch('database.CreateUserDB.bcrypt')
    @patch('database.CreateUserDB.DBmongoHelper')
    def test_create_user(self, mock_db_helper, mock_bcrypt):
        # Configurar mock de DBmongoHelper
        mock_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_collection

        # Configurar mock de bcrypt
        mock_bcrypt.hashpw.return_value = b'hashed_password'

        # Configurar inserción simulada en la colección
        mock_inserted_id = "123abc"
        mock_collection.insert_one.return_value.inserted_id = mock_inserted_id

        # Datos de usuario de ejemplo
        user_data = {
            "username": "example_user",
            "contraseña": "example_password",
        }

        # Llamar al método create_user con datos de usuario simulados
        create_user_db = CreateUserDB()
        result = create_user_db.create_user(user_data)

        # Verificar llamadas a los mocks
        mock_bcrypt.hashpw.assert_called_once_with(b'example_password', mock_bcrypt.gensalt())
        mock_db_helper.return_value.get_collection.assert_called_once_with("users")
        mock_collection.insert_one.assert_called_once()

        # Ajusta este valor según lo que esperas que devuelva el método create_user
        self.assertEqual(result, mock_inserted_id)

if __name__ == "__main__":
    unittest.main()