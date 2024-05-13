import schedule
import time
from ..services import GoogleNewsApiService

def tarea():
    google_api_services = GoogleNewsApiService()
    google_api_services.get_news()

# Definir la acción que se realizará cada 5 minutos
schedule.every(5).minutes.do(tarea)

# Programar la acción diariamente
schedule.every().day.at("00:00").do(lambda: schedule.run_pending())

# Bucle infinito para ejecutar el programa
while True:
    schedule.run_pending()
    time.sleep(1)