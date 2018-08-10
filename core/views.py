from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, status, filters, viewsets
from rest_framework.views import APIView
from core.models import Titulo, Livro, Emprestimo, Autor, Categoria, Editora, Reserva
from core.permissions import isLibrarian, isLibrarianOrReadOnly

from core.serializers import (
        TituloSerializer, EmprestimoSerializer, LivroSerializer, 
        TituloSerializer, AutorSerializer, EditoraSerializer, CategoriaSerializer, ReservaSerializer
    )


class AutorViewSet(viewsets.ModelViewSet):

    name='autor'
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer
    permission_classes = [isLibrarian,]

class CategoriaViewSet(viewsets.ModelViewSet):

    name='categoria'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [isLibrarian,]

class EditoraViewSet(viewsets.ModelViewSet):

    name='editora'
    queryset = Editora.objects.all()
    serializer_class = EditoraSerializer
    permission_classes = [isLibrarian,]

class TituloViewSet(viewsets.ModelViewSet):

    name='titulo'
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    permission_classes = [isLibrarianOrReadOnly,]


class LivroViewSet(viewsets.ModelViewSet):

    name='livro'
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    permission_classes = [isLibrarianOrReadOnly,]

class EmprestimoViewSet(viewsets.ModelViewSet):

    name='emprestimo'
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    permission_classes = [isLibrarianOrReadOnly,]


class ReservaViewSet(viewsets.ModelViewSet):

    name='reserva'
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

