import unittest
from unittest.mock import patch, MagicMock
from database.CreateScheduleDB import CreateScheduleDB

class TestCreateScheduleDB(unittest.TestCase):

    @patch('database.CreateScheduleDB.DBmongoHelper')
    def test_create_schedule(self, mock_db_helper):
        # Configurar mocks
        mock_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_collection
        mock_result = MagicMock()
        mock_result.inserted_id = "example_id"
        mock_collection.insert_one.return_value = mock_result

        # Llamar al método create_schedule de CreateScheduleDB con datos simulados
        create_schedule_db = CreateScheduleDB()
        create_schedule_db.create_schedule("example_user", "12:00", ["word1", "word2"],"")

        # Verificar que se llame a la función de inserción en la colección de cronogramas
        mock_collection.insert_one.assert_called_once()

if __name__ == '__main__':
    unittest.main()