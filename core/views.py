from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, status
from rest_framework.views import APIView

from core.models import Titulo, Livro, Emprestimo
from core.permissions import RegisteredByGerenteOrReadOnly, UserGerenteOrReadOnly
from core.serializers import TituloSerializer, EmprestimoSerializer, LivroSerializer, TituloDetailSerializer
from user.views import UsuarioList

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope


class TituloList(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        RegisteredByGerenteOrReadOnly,
        UserGerenteOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(gerente=self.request.user)


class TituloDetail(generics.RetrieveUpdateDestroyAPIView):

    #
    # def get(self, request, pk_titulo):
    #     titulo = Titulo.objects.get(id=pk_titulo)
    #     titulo_serializer = TituloDetailSerializer(titulo, context={'request': request})
    #     return Response(titulo_serializer.data)
    #
    # def post(self, request):
    #     titulo_serializer = TituloDetailSerializer(data=request.data)
    #     if titulo_serializer.is_valid():
    #         request.data.gerente = request.user
    #         titulo_serializer.save()
    #         return Response(titulo_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(titulo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        RegisteredByGerenteOrReadOnly,
        UserGerenteOrReadOnly,
    )


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-list'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        UserGerenteOrReadOnly,
    )

    def perform_create(self, serializer):
        serializer.save(gerente=self.request.user)


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    name = 'livro-detail'

    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        UserGerenteOrReadOnly,
    )


class EmprestimoList(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-list'

    permission_classes = (
        permissions.IsAuthenticated,
    )


class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-detail'

    permission_classes = (
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
