from flask import Flask
from services.googleNewsApiService import GoogleNewsApiService

# app = Flask(__name__)

def tarea():
    google_api_services = GoogleNewsApiService()
    return  google_api_services.get_news()
     

# if __name__ == '__main__':
#     tarea()
#     app.run(debug=True)  # Ejecuta el servidor Flask en modo debug
    
if __name__ == "__main__":
    result = tarea()
    print(result)
        