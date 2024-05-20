import unittest
from unittest.mock import patch, Mock
from utils.googleNewsApi import GoogleNewsAPI

class TestGoogleNewsAPI(unittest.TestCase):
    @patch('utils.googleNewsApi.os.getenv')
    @patch('utils.googleNewsApi.requests.get')
    def test_get_google_search_api(self, mock_get, mock_getenv):
        # Configurar el valor de retorno de os.getenv para API_KEY_GOOGLE
        mock_getenv.return_value = 'API_KEY_GOOGLE'

        # Definir el comportamiento esperado para las respuestas de la API
        mock_responses = [
            Mock(),  # Primera respuesta
            Mock(),
            
            # Agrega más respuestas simuladas según sea necesario para la paginación
        ]
        mock_responses[0].json.return_value = {'items': [{'title': 'Noticia 1'}]}
        mock_responses[1].json.return_value = {}
        
        # Define el efecto de repetir las respuestas simuladas
        mock_get.side_effect = mock_responses

        # Ejecutar el método a probar
        palabra = 'Python'
        lugar = 'USA'
        start = 1
        news_list = GoogleNewsAPI.get_google_search_api(palabra, lugar, start)

        # Verificar que se llamó a os.getenv con el nombre correcto de la variable de entorno
        mock_getenv.assert_called_once_with('API_KEY_GOOGLE')

        # Verificar que se hicieron las llamadas esperadas a requests.get con las URL correctas
        expected_urls = [
            f"https://www.googleapis.com/customsearch/v1?key=API_KEY_GOOGLE&cx=4784fa47f38814b6d&q=noticias&hq=Python&dateRestrict=d1&gl=USA&cr=countryUSA&sort=date&start={start}",
            f"https://www.googleapis.com/customsearch/v1?key=API_KEY_GOOGLE&cx=4784fa47f38814b6d&q=noticias&hq=Python&dateRestrict=d1&gl=USA&cr=countryUSA&sort=date&start={start+10}"
            # Agrega más URLs esperadas según la paginación de la API
        ]
        mock_get.assert_has_calls([unittest.mock.call(url) for url in expected_urls])

        # Verificar que la lista de noticias contiene los datos esperados
        self.assertEqual(len(news_list), 1)  # Cambia el valor según el número de noticias simuladas
        self.assertEqual(news_list[0]['title'], 'Noticia 1')
        # Agrega más aserciones según sea necesario para verificar los datos de las noticias simuladas

if __name__ == '__main__':
    unittest.main()