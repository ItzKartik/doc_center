from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime

class types(models.Model):
    type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_name = models.CharField(max_length=200)