from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from user.models import Usuario
from user.permissions import GerenteOrReadOnly
from user.serializers import UserSerializer, UserDetailSerializer


class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer
    name = 'usuario-list'

    permission_classes = (
        GerenteOrReadOnly,
        permissions.IsAuthenticated,

    )


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserDetailSerializer
    name = 'usuario-detail'

    permission_classes = (
        GerenteOrReadOnly,
        permissions.IsAuthenticated,

    )
