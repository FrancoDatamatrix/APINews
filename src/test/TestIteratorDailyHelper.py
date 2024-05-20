import unittest
from unittest.mock import patch, MagicMock
from helper.iteratoDailyHelper import tarea

class TestTarea(unittest.TestCase):

    @patch('your_module.time.sleep')  # Mockeamos la función time.sleep
    def test_tarea(self, mock_sleep):
        # Simulamos el bucle infinito ejecutando tarea 3 veces
        mock_sleep.side_effect = [None, None, None]  # Simulamos 3 iteraciones del bucle
        tarea()  # Ejecutamos la función tarea

        # Verificamos que se llame a time.sleep 3 veces (1 vez por cada iteración)
        self.assertEqual(mock_sleep.call_count, 3)

if __name__ == '__main__':
    unittest.main()