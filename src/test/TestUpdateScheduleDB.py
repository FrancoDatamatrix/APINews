import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from bson import ObjectId
from database.UpdateScheduleDB import UpdateScheduleDB

class TestUpdateScheduleDB(unittest.TestCase):

    @patch('database.UpdateScheduleDB.DBmongoHelper')
    @patch('database.UpdateScheduleDB.datetime')
    def test_update_processed_date(self, mock_datetime, mock_db_helper):
        # Configurar mock para datetime
        mock_current_timestamp = 1625247600.0  # Usar un timestamp fijo para la prueba
        mock_datetime.now.return_value.timestamp.return_value = mock_current_timestamp

        # Configurar el mock de DBmongoHelper
        mock_schedule_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_schedule_collection

        # Crear instancia de UpdateScheduleDB
        update_schedule_db = UpdateScheduleDB()

        # ID del schedule para actualizar
        schedule_id = "60d5ec49f72e4b1c4c8d87a6"  # Ejemplo de ObjectId como string
        schedule_object_id = ObjectId(schedule_id)

        # Configurar el resultado del mock update_one
        mock_schedule_collection.update_one.return_value.modified_count = 1

        # Llamar al método update_processed_date
        modified_count = update_schedule_db.update_processed_date(schedule_id)

        # Verificar que datetime.now().timestamp() fue llamado
        mock_datetime.now.return_value.timestamp.assert_called_once()

        # Verificar que get_collection fue llamado con "Schedule"
        mock_db_helper.return_value.get_collection.assert_called_once_with("Schedule")

        # Verificar que update_one fue llamado con los argumentos correctos
        mock_schedule_collection.update_one.assert_called_once_with(
            {"_id": schedule_object_id},
            {"$set": {"procesado": mock_current_timestamp}}
        )

        # Verificar el valor de retorno
        self.assertEqual(modified_count, 1)

if __name__ == '__main__':
    unittest.main()