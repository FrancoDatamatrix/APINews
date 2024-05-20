import unittest
from unittest.mock import patch, MagicMock
from database.GetUserDB import GetUserDB
from bson import ObjectId

class TestGetUserDB(unittest.TestCase):
    @patch('database.GetUserDB.DBmongoHelper')
    def setUp(self, mock_db_helper):
        self.db_helper_mock = mock_db_helper.return_value
        self.users_collection_mock = MagicMock()
        self.db_helper_mock.get_collection.return_value = self.users_collection_mock
        self.get_user_db = GetUserDB()

    def test_get_user_by_id(self):
        # Configurar la colección simulada para devolver un usuario por ID
        user_id = "66427bba88f7b5a45aab85d9"
        user_data = {"_id": user_id, "username": "test_username"}
        self.users_collection_mock.find_one.return_value = user_data

        # Llamar a la función get_user con un ID de usuario simulado
        result = self.get_user_db.get_user(user_id)

        # Verificar que se llamó a find_one con la consulta correcta
        self.users_collection_mock.find_one.assert_called_once_with({'_id': ObjectId('66427bba88f7b5a45aab85d9')})

        # Verificar que se devolvió el usuario correcto
        self.assertEqual(result, user_data)

    def test_get_user_by_username(self):
        # Configurar la colección simulada para devolver un usuario por nombre de usuario
        username = "test_username"
        user_data = {"_id": "test_user_id", "username": username}
        self.users_collection_mock.find_one.return_value = user_data

        # Llamar a la función get_user con un nombre de usuario simulado
        result = self.get_user_db.get_user(username)

        # Verificar que se llamó a find_one con la consulta correcta
        self.users_collection_mock.find_one.assert_called_once_with({"usuario": username})

        # Verificar que se devolvió el usuario correcto
        self.assertEqual(result, user_data)

if __name__ == '__main__':
    unittest.main()