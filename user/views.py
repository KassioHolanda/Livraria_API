from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework import  permissions

from core.serializer import UsuarioSerializer, UsuarioSerializerNovo
from user.models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):

    name='usuario'
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializerNovo


