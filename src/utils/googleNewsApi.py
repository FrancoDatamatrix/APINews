import requests

class GoogleNewsAPI:
    @staticmethod
    def get_google_search_api(palabra, lugar, start=1):
        # Eliminar las comillas de la palabra y el lugar
        palabra_sin_comillas = palabra.replace('"', '')
        lugar_sin_comillas = lugar.replace('"', '')
        apikey = "Tu_API_Key"  # Reemplaza "Tu_API_Key" con tu propia clave de API
        news_list = []

        while len(news_list) < 100:  # Ejemplo de condición de salida
            response = requests.get(f"https://www.googleapis.com/customsearch/v1?key={apikey}&q=noticias&hq={palabra_sin_comillas}&dateRestrict=d1&gl={lugar_sin_comillas}&cr=country{lugar_sin_comillas}&sort=date&start={start}")
            data = response.json()

            if 'items' in data:
                news_list.extend(data['items'])
                start += 10
            else:
                break

        return news_list