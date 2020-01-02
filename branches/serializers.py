from rest_framework.serializers import ModelSerializer

class BranchSerializer(ModelSerializer):
  class Meta:
    fields = ['uid', 'address', 'name']
