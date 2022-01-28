from django.db import models
import uuid
from django.utils import timezone
# Create your models here.

class Pastes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    paste_body = models.TextField()

    class Meta:
        verbose_name_plural = "Pastes"
