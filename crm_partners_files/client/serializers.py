from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullName = serializers.CharField(source='full_name')
    phoneNumber = serializers.CharField(source='phone_number')
    tgUsername = serializers.CharField(source='tg_username')
    comment = serializers.CharField()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)
