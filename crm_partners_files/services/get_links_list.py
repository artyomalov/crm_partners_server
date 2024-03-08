__all__ = ['get_links_list_data', ]

"""
    Gets links list according to page number and selected filter.
"""
from link.models import Link
from link.serializers import LinkSerializer
from django.core.paginator import Paginator


def get_links_list_data(category: str = '', deal_source: str = '', page_number: int = 1, ):
    links_queryset = Link.objects

    if (category == '' and deal_source == '') or (category != '' and deal_source != ''):
        links_list = links_queryset.all()
    elif category == '':
        links_list = links_queryset.filter(deal_source__icontains=deal_source)
    elif deal_source == '':
        links_list = links_queryset.filter(category=category)

    if page_number is None:
        page_number = 1

    paginator = Paginator(links_list, per_page=50)

    serializer = LinkSerializer(paginator.page(page_number), many=True)

    data = {
        'links': serializer.data,
        'pagesCount': paginator.num_pages,
        'hasNext': paginator.page(page_number).has_next(),
        'hasPrevious': paginator.page(page_number).has_previous(),
        'page': page_number,
    }

    return data
