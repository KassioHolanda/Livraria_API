from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions

from core.models import Titulo, Livro, Emprestimo
from core.permissions import GerenteOrReadOnly
from core.serializers import TituloSerializer, EmprestimoSerializer, LivroSerializer
from user.views import UsuarioList


class TituloList(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-list'

    # permission_classes = (
    #     permissions.IsAuthenticated,
    #     permissions.IsAuthenticatedOrReadOnly,
    #     # IsOwnerOrReadOnly
    # )


class TituloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # permissions.IsAuthenticated,
        # IsOwnerOrReadOnly
    )


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
    )


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
    )


class EmprestimoList(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-list'

    # permission_classes = (
    #     GerenteOrReadOnly,
    #     permissions.IsAuthenticated,
    #     permissions.IsAuthenticatedOrReadOnly,
    #     # IsOwnerOrReadOnly
    #
    # )


class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-detail'

    # permission_classes = (
    #     permissions.IsAuthenticated,
    #     # IsOwnerOrReadOnly
    # )


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Livros': reverse(LivroList.name, request=request),
            'Titulos': reverse(TituloList.name, request=request),
            'Usuarios': reverse(UsuarioList.name, request=request),
            'Emprestimos': reverse(EmprestimoList.name, request=request)
        })
