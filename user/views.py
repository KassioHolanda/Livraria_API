from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from user.models import Usuario
from user.serializers import UserSerializer


class UsuarioList(generics.ListAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    name = 'usuario-list'

class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    name = 'usuario-detail'
