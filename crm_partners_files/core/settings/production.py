from .base import *

base_url = 'https://mp-search.ru'

SECRET_KEY = environ.get('SECRET_KEY')

ALLOWED_HOSTS = [base_url]

GENERATED_LINK_BASE_URL = f'{base_url}/client/'

CORS_ALLOW_ALL_ORIGINS = True
