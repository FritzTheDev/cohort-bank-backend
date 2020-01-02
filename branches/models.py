from django.db.models import Model, CharField
from uuid import uuid4
from django.db.models.signals import pre_save

# Create your models here.

class Branch(Model):
  address = CharField(max_length=255)
  name = CharField(max_length=255)
