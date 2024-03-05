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


class ClientList(APIView):
    """
    Creates client's model instance and send client's data to TG and GoogleSheets
    """
    permission_classes = [AllowAny,]
    def _get_link(self, link_name):
        try:
            return Link.objects.get(link_name=link_name)
        except Link.DoesNotExist:
            raise Http404

    def post(self, request, link_name, format=None):
        print(link_name, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>2>>>>>>>>>>>>>>>>>>>')
        link: Link = self._get_link(link_name)

        # sent to services logic

        try:
            if not link_name:
                raise BadRequestError('"linkName" has\'s not been provided')

            serializer = ClientSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status': 'created'}, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except BadRequestError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)