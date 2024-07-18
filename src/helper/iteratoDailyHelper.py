from flask import Flask
from services.googleNewsApiService import GoogleNewsApiService


def tarea():
    google_api_services = GoogleNewsApiService()
    return  google_api_services.get_news()
     
    
if __name__ == "__main__":
    result = tarea()
    print(result)
        