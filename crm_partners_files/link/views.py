from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LinkSerializer
from django.conf import settings
from .models import Link


class LinkDetail(APIView):
    """
    Creates, deletes links.
    """

    def _get_link(self, id):
        try:
            return Link.objects.get(id=id)
        except Link.DoesNotExist:
            raise Http404
        i

    def post(self, request, format=None):



        try:

            generated_link =

            serializer = LinkSerializer(data=request.data)
            if serializer.is_valid():
                return Response({
                    'generatedLink': serializer.data.get(
                        'generated_link',
                        'Что-то пошло не так. Пожалуйста, напишите администратору для решения этой проблемы.'
                    )
                },
                    status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, format=None):
        try:
            link = self._get_link(request.data.get('id'))
            link_id = link.id
            link.delete()
            return Response({'linkId': link_id}, status=status.HTTP_200_OK)

        except Exception as error:
            return Response({'error': str(error)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
