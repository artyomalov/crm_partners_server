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
from services.send_data_to_tg import send_data_to_tg
from services.send_data_to_google_sheets import send_data_to_googlesheets
from custom_exceptions.tg_data_has_not_been_send_exception import TgSendDataError


class ClientDetail(APIView):
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

            name = request.data.get("fullName")
            phone_numbger = request.data.get("phoneNumber")
            tg_username = request.data.get("tgUsername")
            comment = request.data.get("comment")

            text = f'Новый клиент:\n\
                                    Имя: {name}\n\
                                    Телефон: {phone_numbger}\n\
                                    Телеграм: {tg_username}\n\
                                    Комментарий: {comment}'

            response = send_data_to_tg(text=text, chat_id=tg_channel_id)
            if not response.get('ok'):
                raise TgSendDataError('data hasn\'t been sent.')
            # print(response)

            data_to_send_to_googlesheets = [name, phone_numbger, tg_username, comment, ]
            send_data_to_googlesheets(table_name=link.google_sheets_link, sending_data=data_to_send_to_googlesheets)

            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'created'}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except TgSendDataError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        except BadRequestError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
