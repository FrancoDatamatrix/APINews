import unittest
from unittest.mock import patch
from database.GetUserWordsDB import GetUserWordsDB

class TestGetUserWordsDB(unittest.TestCase):
    @patch('database.GetUserWordsDB.DBmongoHelper')
    def setUp(self, mock_db_helper):
        self.mock_db_helper = mock_db_helper.return_value
        self.mock_users_collection = self.mock_db_helper.get_collection.return_value
        self.get_user_words_db = GetUserWordsDB()
        self.get_user_words_db.db_helper = self.mock_db_helper

    def test_get_words_existing_user(self):
        # Datos de usuario de ejemplo
        user_id = "66427bba88f7b5a45aab85d9"
        user_data = {
            "_id": user_id,
            "palabras": "example1,example2,example3",
            "lugar": "example_location"
        }
        # Configurar el mock de la colección para devolver los datos de usuario de ejemplo
        self.mock_users_collection.find_one.return_value = user_data

        # Llamar al método get_words con el ID de usuario
        palabras, lugar = self.get_user_words_db.get_words(user_id)

        # Verificar que las palabras y el lugar se devuelvan correctamente
        self.assertIsNotNone(palabras)
        self.assertEqual(palabras, ["example1", "example2", "example3"])
        self.assertIsNotNone(lugar)
        self.assertEqual(lugar, "example_location")

if __name__ == "__main__":
    unittest.main()