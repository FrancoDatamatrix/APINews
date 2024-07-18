from dotenv import load_dotenv
from datetime import timedelta
import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1) # Expiracion access token
    JWT_TOKEN_LOCATION = ['cookies']  # Manejo de tokens en cookies
    JWT_COOKIE_SECURE = True #habilitar en produccion
    JWT_ACCESS_COOKIE_PATH = '/'
    JWT_COOKIE_CSRF_PROTECT = True  #habilitar en producción