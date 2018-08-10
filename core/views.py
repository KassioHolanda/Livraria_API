from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, status, filters, viewsets
from rest_framework.views import APIView
from core.models import Titulo, Livro, Emprestimo, Autor, Categoria, Editora
#from core.permissions import RegisteredByGerenteOrReadOnly, IsGerenteOrReadOnly, IsClienteOrReadOnly
from core.serializers import (TituloSerializer, EmprestimoSerializer, LivroSerializer, 
    TituloSerializer, AutorSerializer, EditoraSerializer, CategoriaSerializer)
from user.views import UsuarioList


class AutorViewSet(viewsets.ModelViewSet):

    name='autor'
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    #permission_classes = []

class CategoriaViewSet(viewsets.ModelViewSet):

    name='categoria'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #permission_classes = []

class EditoraViewSet(viewsets.ModelViewSet):

    name='editora'
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    #permission_classes = []

class TituloViewSet(viewsets.ModelViewSet):

    name='titulo'
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    #permission_classes = []


class LivroViewSet(viewsets.ModelViewSet):

    name='livro'
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    #permission_classes = []


"""
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            #'Livros': reverse(LivroList.name, request=request),
            'Títulos': reverse(TituloViewSet.name, request=request),
            'Autores': reverse(AutorViewSet.name, request=request),
            'Categorias': reverse(CategoriaViewSet.name, request=request),
            'Editoras': reverse(EditoraViewSet.name, request=request),
            #'Usuários': reverse(UsuarioList.name, request=request),
            #'Empréstimos': reverse(EmprestimoList.name, request=request)
        })
"""
