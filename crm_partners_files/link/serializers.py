from rest_framework import serializers
from .models import Link


class LinkSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    linkName = serializers.CharField(source='link_name')
    tgChannelId = serializers.CharField(source='tg_channel_id')
    dealSource = serializers.CharField(source='deal_source')
    googleSheetsLink = serializers.CharField(source='google_sheets_link')
    generatedLink = serializers.CharField(source='generated_link')
    category = serializers.CharField()

    def create(self, validated_data):
        return Link.objects.create(**validated_data)
