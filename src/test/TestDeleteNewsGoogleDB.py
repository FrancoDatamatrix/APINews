import unittest
from unittest.mock import patch, MagicMock
from bson import ObjectId
from database.DeleteNewsGoogleDB import DeleteNewsDB  # Asegúrate de importar correctamente tu módulo

class TestDeleteNewsDB(unittest.TestCase):

    @patch('database.DeleteNewsGoogleDB.DBmongoHelper')
    def test_delete_news_by_id_success(self, MockDBmongoHelper):
        # Configurar el mock para DBmongoHelper
        mock_db_helper = MockDBmongoHelper.return_value
        mock_collection = mock_db_helper.get_collection.return_value
        mock_collection.delete_one.return_value.deleted_count = 1

        # Instanciar el servicio
        delete_news_db = DeleteNewsDB()

        # Llamar al método que se está probando
        result = delete_news_db.delete_news_by_id("60f7c6e2b75a2e3d8c8b4567")

        # Verificar que el método delete_one fue llamado con el ObjectId correcto
        mock_collection.delete_one.assert_called_once_with({"_id": ObjectId("60f7c6e2b75a2e3d8c8b4567")})

        # Verificar el resultado
        self.assertTrue(result)

    @patch('database.DeleteNewsGoogleDB.DBmongoHelper')
    def test_delete_news_by_id_failure(self, MockDBmongoHelper):
        # Configurar el mock para DBmongoHelper
        mock_db_helper = MockDBmongoHelper.return_value
        mock_collection = mock_db_helper.get_collection.return_value
        mock_collection.delete_one.return_value.deleted_count = 0

        # Instanciar el servicio
        delete_news_db = DeleteNewsDB()

        # Llamar al método que se está probando
        result = delete_news_db.delete_news_by_id("60f7c6e2b75a2e3d8c8b4567")

        # Verificar que el método delete_one fue llamado con el ObjectId correcto
        mock_collection.delete_one.assert_called_once_with({"_id": ObjectId("60f7c6e2b75a2e3d8c8b4567")})

        # Verificar el resultado
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()