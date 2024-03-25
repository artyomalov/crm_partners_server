from .base import *

base_url = 'localhost'

SECRET_KEY = 'django-insecure-2f4vl+=d=+w-er9w2o1boj76r^wb%)44d8ug^y6vr(r&6(i_e0'

ALLOWED_HOSTS = [f'{base_url}']

GENERATED_LINK_BASE_URL = f'{base_url}:3000/client/'

# CORS
CORS_ALLOWED_ORIGINS = [
    f'http://{base_url}:3000',
]
