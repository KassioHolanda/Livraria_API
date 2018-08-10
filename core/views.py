from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, status, filters, viewsets
from rest_framework.views import APIView
from core.models import Titulo, Livro, Emprestimo
#from core.permissions import RegisteredByGerenteOrReadOnly, IsGerenteOrReadOnly, IsClienteOrReadOnly
from core.serializers import TituloSerializer, EmprestimoSerializer, LivroSerializer, TituloSerializer
from user.views import UsuarioList


class TituloViewSet(viewsets.ModelViewSet):

    name='titulo-viewset'
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer
    #permission_classes = []



class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            #'Livros': reverse(LivroList.name, request=request),
            'Títulos': reverse(TituloViewSet.name, request=request),
            #'Usuários': reverse(UsuarioList.name, request=request),
            #'Empréstimos': reverse(EmprestimoList.name, request=request)
        })
