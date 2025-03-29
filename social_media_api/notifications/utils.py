from .models import Notification
from django.contrib.contenttypes.models import ContentType

def create_notification(actor, recipient, verb, target):
    Notification.objects.create(
        actor=actor,
        recipient=recipient,
        verb=verb,
        target_content_type=ContentType.objects.get_for_model(target),
        target_object_id=target.id
    )
