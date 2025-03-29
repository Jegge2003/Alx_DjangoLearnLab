from rest_framework import serializers
from .models import Notification
from django.contrib.contenttypes.models import ContentType

class NotificationSerializer(serializers.ModelSerializer):
    actor = serializers.StringRelatedField()
    target_object_id = serializers.IntegerField()
    target_content_type = serializers.StringRelatedField()
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Notification
        fields = ['id', 'actor', 'verb', 'target_object_id', 'target_content_type', 'timestamp', 'read']
