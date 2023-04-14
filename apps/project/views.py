from django.shortcuts import render

from rest_framework import viewsets

from apps.project.models import Establishments, Category, QA
from apps.project.serializers import (EstablishmentsSerializer, 
                                      CategorySerializer, 
                                      QASerializer
                                      )


class EstablishmentsViewSet(viewsets.ModelViewSet):
    queryset = Establishments.objects.all()
    serializer_class = EstablishmentsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QAViewSet(viewsets.ModelViewSet):
    queryset = QA.objects.all()
    serializer_class = QASerializer
