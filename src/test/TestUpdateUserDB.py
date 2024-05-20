import unittest
from unittest.mock import ANY, patch, MagicMock
from database.DBMongoHelper import DBmongoHelper
from database.UpdateUserDB import UpdateUserDB
from bson import ObjectId
import bcrypt

class TestUpdateUserDB(unittest.TestCase):
    @patch('database.UpdateUserDB.bcrypt.hashpw')
    @patch('database.UpdateUserDB.DBmongoHelper')
    def test_update_user_with_password(self, mock_db_helper, mock_hashpw):
        # Configuración de mocks y datos de prueba
        user_id = "66427bba88f7b5a45aab85d9"
        updated_data = {"contraseña": "new_password"}

        mock_collection = MagicMock()
        mock_result = MagicMock()
        mock_result.modified_count = 1
        mock_collection.update_one.return_value = mock_result

        mock_db_helper.return_value.get_collection.return_value = mock_collection

        # Configurar el valor de retorno de hashpw para la comparación
        mock_hashpw.return_value = b'hashed_password'

        # Ejecutar el método a probar
        update_user_db = UpdateUserDB()
        update_user_db.db_helper = mock_db_helper

        result = update_user_db.update_user(user_id, updated_data)

        # Verificar que se llamó a bcrypt.hashpw con la contraseña actualizada y el retorno correcto
        mock_hashpw.assert_called_once_with(b'new_password', ANY)
        self.assertEqual(result, "Usuario actualizado correctamente.")
        mock_collection.update_one.assert_called_once_with({'_id': ObjectId('66427bba88f7b5a45aab85d9')}, {'$set': {'contraseña': 'hashed_password'}})

if __name__ == '__main__':
    unittest.main()