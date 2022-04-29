from django.db.models import signals
from django.dispatch import receiver
from .models import task, task_log

@receiver(signals.pre_save, sender=task)
def add_task_uuid(sender, instance, **kwargs):
    import uuid

    if not instance.uuid:
        instance.uuid = str(uuid.uuid1())

@receiver(signals.pre_save, sender=task_log)
def add_task_log_uuid(sender, instance, **kwargs):
    import uuid

    if not instance.uuid:
        instance.uuid = str(uuid.uuid1())