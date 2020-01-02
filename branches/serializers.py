from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Branch
class BranchSerializer(ModelSerializer):
  branch_id = IntegerField(write_only=True)
  class Meta:
    fields = ['branch_id', 'address', 'name']
    model = Branch