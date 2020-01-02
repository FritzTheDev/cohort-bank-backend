from rest_framework.serializers import ModelSerializer
from .models import Branch
class BranchSerializer(ModelSerializer):
  class Meta:
    fields = ['uid', 'address', 'name']
    model = Branch