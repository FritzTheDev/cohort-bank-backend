from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Branch
from .serializers import BranchSerializer
# Create your views here.

class BranchViewSet(ModelViewSet):
  queryset = Branch.objects.all()
  serializer_class = BranchSerializer