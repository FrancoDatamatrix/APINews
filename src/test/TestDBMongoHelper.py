import unittest
from unittest.mock import patch, MagicMock
from database.DBMongoHelper import DBmongoHelper 

class TestDBmongoHelper(unittest.TestCase):

    @patch('database.DBMongoHelper.MongoClient')
    @patch('database.DBMongoHelper.os.getenv')
    def test_get_collection(self, mock_getenv, mock_mongo_client):
        # Configura el mock de os.getenv
        mock_getenv.side_effect = lambda key: {
            'DB_URL': 'mongodb://your_db_url',
            'DB_NAME': 'test_db'
        }[key]

        # Configura el mock de MongoClient
        mock_db = mock_mongo_client.return_value['test_db']
        mock_collection = mock_db['test_collection']
        
        # Crea una instancia de DBmongoHelper
        db_helper = DBmongoHelper()

        # Llama al método get_collection
        collection = db_helper.get_collection('test_collection')

        # Verifica que se haya llamado a MongoClient con la URL correcta
        mock_mongo_client.assert_called_once_with('mongodb://your_db_url')

        # Verifica que se haya obtenido la colección correcta
        self.assertEqual(collection, mock_collection)

if __name__ == '__main__':
    unittest.main()