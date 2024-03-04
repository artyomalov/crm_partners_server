from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.Serializer):
    linkName = serializers.CharField(source='link_name')
    tgChannelId = serializers.CharField(source='tg_channel_id')
    dealSource = serializers.CharField(source='deal_source')
    googleSheetsLink = serializers.CharField(source='google_sheets_link')
    generatedLink = serializers.CharField(source='generated_link')

    def create(self, validated_data):
        data = {
            'link_name': validated_data.get('linkName'),
            'tg_channel_id': validated_data.get('tgChannelId'),
            'deal_source': validated_data.get('dealSource'),
            'google_sheets_link': validated_data.get('googleSheetsLink'),
            'generated_link': validated_data.get('generatedLink'),
        }

        return Link.objects.creaate(**data)
