from .models import Room
from rest_framework import serializers


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'code',
            'host',
            'guest_can_pause',
            'votes_to_skip',
            'created_at',
        ]


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'guest_can_pause',
            'votes_to_skip',
        ]


class UpdateRoomSerializer(serializers.ModelSerializer):
    #redefines the code field in the serializer to remove the UNIQUE requirement
    code = serializers.CharField(validators=[])

    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip', 'code')