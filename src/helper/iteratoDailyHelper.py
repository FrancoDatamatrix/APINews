from flask import Flask
import schedule
import time
from services.googleNewsApiService import GoogleNewsApiService

app = Flask(__name__)

def tarea():
    google_api_services = GoogleNewsApiService()
    google_api_services.get_news()

def start_schedule():
    # Definir la acción que se realizará cada 10 minutos
    schedule.every(10).minutes.do(tarea)

    # Programar la acción diariamente
    schedule.every().day.at("00:00").do(lambda: schedule.run_pending())

    # Bucle infinito para ejecutar el programa
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == '__main__':
    start_schedule()
    app.run(debug=True)  # Ejecuta el servidor Flask en modo debug
        