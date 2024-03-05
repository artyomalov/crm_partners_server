import json

from requests import get, post
from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ClientSerializer
from django.conf import settings
from .models import Client
from link.models import Link
from custom_exceptions.bad_request_exception import BadRequestError
from django.conf import settings


# chat_id={channel_id}&chat_type=private

# URL = f'https://api.telegram.org/bot{settings.BOT_TOKEN}/sendMessage?'
#
#
# def send_msg(chat_id, text):
#     url_req = "https://api.telegram.org/bot" + settings.BOT_TOKEN + "/sendMessage"
#     params = {
#         "chat_id": '886177470',
#         "text": 'text'
#     }
#
#     results = get(url=url_req, params=params)
#     print(results.json())


def send_msg(text, chat_id):
    url_req = "https://api.telegram.org/bot" + settings.BOT_TOKEN_CRM + "/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": text
    }

    results = get(url=url_req, params=params)
    print(results.json())


class ClientList(APIView):
    """
    Creates client's model instance and send client's data to TG and GoogleSheets
    """
    permission_classes = [AllowAny, ]

    def _get_link(self, link_name):
        try:
            return Link.objects.get(link_name=link_name)
        except Link.DoesNotExist:
            raise Http404

    def post(self, request, link_name, format=None):

        # sent to services logic

        try:
            link: Link = self._get_link(link_name)
            tg_channel_id = str(link.tg_channel_id)
            if not link_name:
                raise BadRequestError('"linkName" has\'s not been provided')

            text = f'Новый клиент:\n\
                                    Имя: {request.data.get("fullName")}\n\
                                    Телефон: {request.data.get("phoneNumber")}\n\
                                    Телеграм: {request.data.get("tgUsername")}\n\
                                    Комментарий: {request.data.get("comment")}'

            send_msg(text=text, chat_id=tg_channel_id)
            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({'status': 'created'}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except BadRequestError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
