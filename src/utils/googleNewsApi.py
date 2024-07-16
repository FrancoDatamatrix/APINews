import os
import requests
from dotenv import load_dotenv

load_dotenv()

class GoogleNewsAPI:
    @staticmethod
    def get_google_search_api(palabra, lugar, start=1):
        #quitamos las comillas de los string para evitar errores en la url
        if lugar:
            lugar_strip = lugar.strip('"')
        else:
            lugar_strip = lugar
            
        palabra_strip = palabra.strip('"')
        
        api_key = os.getenv("API_KEY_GOOGLE")
        url=f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx=4784fa47f38814b6d&q=noticias&hq={palabra_strip}&dateRestrict=d1&gl={lugar_strip}&cr=country{lugar_strip}&sort=date&start={start}"
        news_list = []
        news_id = 1

        while True:  # Continuará ejecutándose hasta que se rompa explícitamente
            response = requests.get(url)
            data = response.json()
            if 'items' in data:
                for item in data['items']:
                    item['_id'] = news_id  # Agregar un ID único
                    news_list.append(item)
                    news_id += 1  # Incrementar el contador de IDs
                start += 10
                url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx=4784fa47f38814b6d&q=noticias&hq={palabra_strip}&dateRestrict=d1&gl={lugar_strip}&cr=country{lugar_strip}&sort=date&start={start}"
            else:
                break  # Romper el bucle si 'items' no está presente en la respuesta

        return news_list