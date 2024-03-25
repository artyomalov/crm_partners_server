import services
import custom_exceptions
from django.http import Http404
from googleapiclient.errors import HttpError
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from link.models import Link
from .serializers import ClientSerializer


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
            link_category = link.category
            if not link_name:
                raise custom_exceptions.BadRequestError('link_name_error')

            name = request.data.get("fullName")
            phone_number = request.data.get("phoneNumber")
            tg_username = request.data.get("tgUsername")
            comment = request.data.get("comment")

            text = f'Новый клиент:\n\
                                    Имя: {name}\n\
                                    Телефон: {phone_number}\n\
                                    Телеграм: {tg_username}\n\
                                    Комментарий: {comment}'

            response = services.send_data_to_tg(text=text, chat_id=tg_channel_id)
            if not response.get('ok'):
                raise custom_exceptions.TgSendDataError(response.get('description'))

            data_to_send_to_googlesheets = [name, phone_number, tg_username, comment, ]
            services.send_data_to_googlesheets(table_name=link.google_sheets_link,
                                               sending_data=data_to_send_to_googlesheets)

            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'category': link_category}, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Http404 as error:
            return Response(str(error), status=status.HTTP_404_NOT_FOUND)
        except custom_exceptions.TgSendDataError as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        except custom_exceptions.BadRequestError as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        except HttpError as error:
            return Response(str(error), status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response(str(error), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
