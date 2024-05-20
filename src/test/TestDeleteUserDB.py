import unittest
from database.DeleteUserDB import DeleteUserDB
from unittest.mock import patch, MagicMock
from bson import ObjectId

class TestDeleteUserDB(unittest.TestCase):

    @patch('database.DeleteUserDB.DBmongoHelper')
    def test_delete_user_by_id(self, mock_db_helper):
        # Configurar mocks
        mock_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_collection
        mock_delete_result = MagicMock(deleted_count=1)
        mock_collection.delete_one.return_value = mock_delete_result

        # Llamar al método delete_user_by_id de DeleteUserDB con un ID de usuario simulado
        delete_user_db = DeleteUserDB()
        result = delete_user_db.delete_user_by_id('66427bba88f7b5a45aab85d9')

        # Verificar que se llame a la función de eliminación en la colección de usuarios
        mock_collection.delete_one.assert_called_once_with({'_id': ObjectId('66427bba88f7b5a45aab85d9')})

        # Verificar que se devuelva True si se elimina al menos un usuario
        self.assertTrue(result)

    @patch('database.DeleteUserDB.DBmongoHelper')
    def test_delete_user_by_id_not_found(self, mock_db_helper):
        # Configurar mocks
        mock_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_collection
        mock_delete_result = MagicMock(deleted_count=0)
        mock_collection.delete_one.return_value = mock_delete_result

        # Llamar al método delete_user_by_id de DeleteUserDB con un ID de usuario simulado
        delete_user_db = DeleteUserDB()
        result = delete_user_db.delete_user_by_id("66427bba88f7b5a45aab85d9")

        # Verificar que se llame a la función de eliminación en la colección de usuarios
        mock_collection.delete_one.assert_called_once_with({'_id': ObjectId('66427bba88f7b5a45aab85d9')})

        # Verificar que se devuelva False si no se elimina ningún usuario
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()