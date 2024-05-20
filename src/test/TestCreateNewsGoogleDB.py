import unittest
from unittest.mock import patch, MagicMock
from database.CreateNewsGoogleDB import CreateNewsDB
from datetime import datetime
from bson import ObjectId

class TestCreateNewsDB(unittest.TestCase):

    @patch('database.CreateNewsGoogleDB.DBmongoHelper')
    def test_create_news(self, mock_db_helper):
        # Configurar el mock de la colección y los datos simulados
        mock_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_collection
        mock_insert_result = MagicMock()
        mock_insert_result.inserted_id = ObjectId('66427bba88f7b5a45aab85d9')
        mock_collection.insert_one.return_value = mock_insert_result

        # Datos simulados para crear una noticia
        news = {"Example news content"}
        usuario = "example_user"
        palabra = "example_word"

        # Llamar al método create_news de CreateNewsDB
        create_news_db = CreateNewsDB()
        news_id = create_news_db.create_news(palabra, usuario, news )

        # Verificar que se llamó a insert_one en la colección de noticias con los parámetros adecuados
        mock_collection.insert_one.assert_called_once_with({
            "usuario": usuario,
            "palabra": palabra,
            "news": news,
            "timestamp": datetime.now()  # Verificar que el timestamp sea el actual
        })

        # Verificar el resultado
        self.assertEqual(news_id, '66427bba88f7b5a45aab85d9')

if __name__ == '__main__':
    unittest.main()