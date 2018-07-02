from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
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

    filter_backends = (
        filters.SearchFilter,
        filters.OrderingFilter,
    )

    search_fields = ('username', 'email')
    ordering_fields = ('username', 'email')

    # filter_backends = (
    #     DjangoFilterBackend,
    # )
    #
    # filter_fields = ('nome', 'tipo_usuario')


class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UserDetailSerializer
    name = 'usuario-detail'

    permission_classes = (
        GerenteOrReadOnly,
        permissions.IsAuthenticated,

    )
