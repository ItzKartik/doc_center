from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime

class types(models.Model):
    type_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type_name = models.CharField(max_length=200)

class docs(models.Model):
    doc_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=200)
    doc = models.FileField(upload_to='docs/')

class bids(models.Model):
    linker = models.ForeignKey(docs, on_delete=models.CASCADE)
    bid_amt = models.IntegerField()
    bid_date = models.DateTimeField(auto_now=True)