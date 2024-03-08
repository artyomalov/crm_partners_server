from django.http import Http404
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LinkSerializer
from django.conf import settings
from .models import Link
from custom_exceptions.bad_request_exception import BadRequestError
from services.get_links_list import get_links_list_data


class LinkList(APIView):

    def get(self, request, format=None):
        """
        Get filtered records from database according to filter value
        :param request:
        :param format:
        :return: Response
        """

        category = request.query_params.get('category')
        page_number = request.query_params.get('page')

        data = get_links_list_data(page_number=page_number, category=category)

        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, format=None):
        """
        Gets list of links that must be deleted, selected category and
        page number. Deletes selected links from database and returns
        list of the remaining links, page number, selected category and pagination data.
        :param request:
        :param format:
        :return: Response
        """
        delete_links_queryset = Link.objects.filter(id__in=[*request.query_params.get('id').split('-')])
        delete_links_queryset.delete()

        category = request.query_params.get('category')
        page_number = request.query_params.get('page')

        data = get_links_list_data(page_number=page_number, category=category)

        return Response(data, status=status.HTTP_200_OK)


class LinkSearch(APIView):
    def get(self, request, format=None):
        """
         Get filtered records from database according to filter value
        :param request:
        :param format:
        :return:
        """
        deal_source = request.query_params.get('dealSource')
        data = get_links_list_data(deal_source=deal_source)

        return Response(data, status=status.HTTP_200_OK)


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
        link_name = request.data.get('linkName')
        try:
            if not link_name:
                raise BadRequestError('"linkName" has\'s not been provided')

            generated_link = settings.GENERATED_LINK_BASE_URL + link_name

            data = {
                **request.data,
                'generatedLink': generated_link
            }

            serializer = LinkSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'generatedLink': serializer.data.get(
                        'generatedLink',
                        'Что-то пошло не так. Пожалуйста, напишите администратору для решения этой проблемы.'
                    )
                },
                    status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except BadRequestError as error:
            return Response({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
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
