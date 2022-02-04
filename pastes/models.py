from django.db import models
import uuid
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Pastes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(default=timezone.now)
    paste_body = models.TextField()
    encrypted_flag = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('pastes-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Pastes"
