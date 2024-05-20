import unittest
from unittest.mock import patch, MagicMock
from database.StopScheduleDB import StopScheduleDB
from bson import ObjectId

class TestStopScheduleDB(unittest.TestCase):

    @patch('database.StopScheduleDB.DBmongoHelper')
    def test_stop_schedule(self, mock_db_helper):
        # Configurar el mock de la colección y el resultado
        mock_collection = MagicMock()
        mock_result = MagicMock()
        mock_result.deleted_count = 1
        mock_collection.delete_many.return_value = mock_result

        # Configurar el mock del DBmongoHelper
        mock_db_helper.return_value.get_collection.return_value = mock_collection

        # Llamar al método stop_schedule de StopScheduleDB con datos simulados
        stop_schedule_db = StopScheduleDB()
        result = stop_schedule_db.stop_schedule(ObjectId("60d5ec49f72e4b1c4c8d87a6"))

        # Verificar que se llamó a delete_many en la colección de cronogramas
        mock_collection.delete_many.assert_called_once_with({"_id": ObjectId("60d5ec49f72e4b1c4c8d87a6")})

        # Verificar el resultado
        self.assertEqual(result, 1)  # Se espera que se haya eliminado 1 documento

if __name__ == '__main__':
    unittest.main()