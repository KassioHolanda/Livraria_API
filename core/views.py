from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from core.models import Titulo, Livro, Emprestimo
from core.permissions import RegisteredByGerenteOrReadOnly, IsGerenteOrReadOnly, IsClienteOrReadOnly
from core.serializers import TituloSerializer, EmprestimoSerializer, LivroSerializer, TituloSerializer
from user.views import UsuarioList


# from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class TituloList(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsGerenteOrReadOnly,
    )

    filter_backends = (
        DjangoFilterBackend,
    )

    filter_fields = ('descricao', 'genero')

    def perform_create(self, serializer):
        serializer.save(gerente=self.request.user)


class TituloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        IsGerenteOrReadOnly,
    )


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-list'

    permission_classes = (
        # UserGerenteLivroOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-detail'

    permission_classes = (
        # UserGerenteLivroOrReadOnly,
        permissions.IsAuthenticatedOrReadOnly,
    )


class EmprestimoList(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-list'

    permission_classes = (
        IsClienteOrReadOnly,
        permissions.IsAuthenticated,
    )

    filter_backends = (
        DjangoFilterBackend,
    )

    filter_fields = ('titulo', 'usuario')


class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-detail'

    permission_classes = (
        IsClienteOrReadOnly,
        permissions.IsAuthenticated,
    )


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({
            'Livros': reverse(LivroList.name, request=request),
            'Titulos': reverse(TituloList.name, request=request),
            'Usuarios': reverse(UsuarioList.name, request=request),
            'Emprestimos': reverse(EmprestimoList.name, request=request)
        })
