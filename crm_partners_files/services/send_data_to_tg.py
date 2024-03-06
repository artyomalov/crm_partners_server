__all__ = ['send_data_to_tg', ]

from os import environ
from requests import get

BOT_TOKEN_LINK_GENERATOR = environ.get('BOT_TOKEN_LINK_GENERATOR')

def send_data_to_tg(text, chat_id):
    url_req = "https://api.telegram.org/bot" + BOT_TOKEN_LINK_GENERATOR + "/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }

    response = get(url=url_req, params=params)
    return response.json()
