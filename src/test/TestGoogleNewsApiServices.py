import unittest
from unittest.mock import patch, MagicMock
from services.googleNewsApiService import GoogleNewsApiService  # Reemplaza 'your_module_path' con el camino correcto a tu servicio

class TestGoogleNewsApiService(unittest.TestCase):

    @patch('services.googleNewsApiService.UpdateScheduleDB')
    @patch('services.googleNewsApiService.GoogleNewsAPI.get_google_search_api')
    @patch('services.googleNewsApiService.CreateNewsDB')
    @patch('services.googleNewsApiService.GetUserWordsDB')
    @patch('services.googleNewsApiService.GetScheduleDB')
    def test_get_news_success(self, mock_get_schedule_db, mock_get_user_words_db, mock_create_news_db, mock_get_google_search_api, mock_update_schedule_db):
        # Configurar los mocks
        mock_get_schedule_db.return_value.get_schedule.return_value = [
            {"hora": "08:00", "usuario_id": 1, "_id": "schedule1"}
        ]
        mock_get_user_words_db.return_value.get_words.return_value = (["palabra1"], "lugar1")
        mock_get_google_search_api.return_value = {"some": "news_data"}
        mock_create_news_db.return_value.create_news.return_value = True

        # Instanciar el servicio
        service = GoogleNewsApiService()

        # Realizar la solicitud
        result = service.get_news()
        
        # Verificar los resultados
        self.assertTrue(result)
        mock_get_schedule_db.return_value.get_schedule.assert_called_once()
        mock_get_user_words_db.return_value.get_words.assert_called_once_with(1)
        mock_get_google_search_api.assert_called_once_with("palabra1", "lugar1")
        mock_create_news_db.return_value.create_news.assert_called_once_with("palabra1", 1, {"some": "news_data"})
        mock_update_schedule_db.return_value.update_processed_date.assert_called_once_with("schedule1")

    @patch('services.googleNewsApiService.UpdateScheduleDB')
    @patch('services.googleNewsApiService.GoogleNewsAPI.get_google_search_api')
    @patch('services.googleNewsApiService.CreateNewsDB')
    @patch('services.googleNewsApiService.GetUserWordsDB')
    @patch('services.googleNewsApiService.GetScheduleDB')
    def test_get_news_no_schedules(self, mock_get_schedule_db, mock_get_user_words_db, mock_create_news_db, mock_get_google_search_api, mock_update_schedule_db):
        # Configurar los mocks
        mock_get_schedule_db.return_value.get_schedule.return_value = []

        # Instanciar el servicio
        service = GoogleNewsApiService()

        # Realizar la solicitud
        result = service.get_news()
        
        # Verificar los resultados
        self.assertFalse(result)
        mock_get_schedule_db.return_value.get_schedule.assert_called_once()
        mock_get_user_words_db.return_value.get_words.assert_not_called()
        mock_get_google_search_api.assert_not_called()
        mock_create_news_db.return_value.create_news.assert_not_called()
        mock_update_schedule_db.return_value.update_processed_date.assert_not_called()

    @patch('services.googleNewsApiService.UpdateScheduleDB')
    @patch('services.googleNewsApiService.GoogleNewsAPI.get_google_search_api')
    @patch('services.googleNewsApiService.CreateNewsDB')
    @patch('services.googleNewsApiService.GetUserWordsDB')
    @patch('services.googleNewsApiService.GetScheduleDB')
    def test_get_news_create_news_fails(self, mock_get_schedule_db, mock_get_user_words_db, mock_create_news_db, mock_get_google_search_api, mock_update_schedule_db):
        # Configurar los mocks
        mock_get_schedule_db.return_value.get_schedule.return_value = [
            {"hora": "08:00", "usuario_id": 1, "_id": "schedule1"}
        ]
        mock_get_user_words_db.return_value.get_words.return_value = (["palabra1"], "lugar1")
        mock_get_google_search_api.return_value = {"some": "news_data"}
        mock_create_news_db.return_value.create_news.return_value = False

        # Instanciar el servicio
        service = GoogleNewsApiService()

        # Realizar la solicitud
        result = service.get_news()
        
        # Verificar los resultados
        self.assertFalse(result)
        mock_get_schedule_db.return_value.get_schedule.assert_called_once()
        mock_get_user_words_db.return_value.get_words.assert_called_once_with(1)
        mock_get_google_search_api.assert_called_once_with("palabra1", "lugar1")
        mock_create_news_db.return_value.create_news.assert_called_once_with("palabra1", 1, {"some": "news_data"})
        mock_update_schedule_db.return_value.update_processed_date.assert_called_once_with("schedule1")

if __name__ == '__main__':
    unittest.main()