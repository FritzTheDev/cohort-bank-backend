from django.db.models import Model, CharField
from uuid import uuid4

# Create your models here.

class Branch(Model):
  uid = CharField(max_length=50, primary_key=True, default=uuid4())
  address = CharField(max_length=255)
  name = CharField(max_length=255)