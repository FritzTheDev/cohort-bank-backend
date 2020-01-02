from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Branch
class BranchSerializer(ModelSerializer):
  class Meta:
    fields = ['id', 'address', 'name']
    model = Branch