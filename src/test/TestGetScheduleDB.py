import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from database.GetSchedule import GetScheduleDB  # Reemplaza 'your_module_name' con el nombre de tu archivo o módulo

class TestGetScheduleDB(unittest.TestCase):
    @patch('database.GetSchedule.datetime')
    @patch('database.GetSchedule.DBmongoHelper')
    def test_get_schedule(self, mock_db_helper, mock_datetime):
        # Mock de la fecha y hora actual
        current_timestamp = 1621285200  # Timestamp correspondiente a una fecha específica
        current_hour = 1230  # Hora específica
        mock_datetime.now.return_value.timestamp.return_value = current_timestamp
        mock_datetime.now.return_value.strftime.return_value = f'{current_hour:04d}'  # Formato de hora en HHMM

        # Mock de la colección y los datos simulados en la base de datos
        mock_collection = MagicMock()
        mock_db_helper.return_value.get_collection.return_value = mock_collection
        mock_cursor = MagicMock()
        mock_collection.find.return_value = mock_cursor
        mock_cursor_list = [{"usuario_id": "user1", "hora": 1000}, {"usuario_id": "user2", "hora": 1100}]
        mock_cursor.__iter__.return_value = iter(mock_cursor_list)

        # Llamada al método get_schedule
        get_schedule_db = GetScheduleDB()
        schedules_list = get_schedule_db.get_schedule()

        # Verificar que se llamó a find en la colección de cronogramas con los filtros adecuados
        mock_collection.find.assert_called_once_with({
            "$or": [
                {"procesado": None},  # Filtrar los schedules no procesados
                {"procesado": {"$ne": None, "$lte": current_timestamp - 86400}}  # Filtrar los schedules procesados y cuya diferencia de tiempo sea menor a 86400 segundos (24 horas)
            ],
            "hora": {"$lte": current_hour}  # Filtrar las horas iguales o menores a la actual
        })

        # Verificar el resultado
        self.assertEqual(schedules_list, mock_cursor_list)

if __name__ == '__main__':
    unittest.main()