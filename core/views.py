from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from core.models import Titulo, Livro, Emprestimo
from core.serializers import TituloSerializer, EmprestimoSerializer


class TituloList(generics.ListCreateAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-list'


class TituloDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    name = 'titulo-detail'


class LivroList(generics.ListCreateAPIView):
    queryset = Livro.objects.all()
    serializer_class = TituloSerializer
    name = 'livro-list'


class LivroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Livro.objects.all()
    serializer_class = TituloSerializer
    name = 'livro-detail'


class EmprestimoList(generics.ListCreateAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-list'


class EmprestimoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer
    name = 'emprestimo-detail'
