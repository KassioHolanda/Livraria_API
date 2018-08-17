from rest_framework import serializers
from core.models import Titulo, Livro, Emprestimo, Autor, Categoria, Editora, Reserva
import datetime

from user.models import Usuario
from user.serializer import UsuarioSerializer


class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id', 'nome'
        )

    def validate(self, data):
        if Categoria.objects.filter(nome=data['nome']).exists():
            raise serializers.ValidationError('Já possui um categoria com esse nome')
        return data


class EditoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Editora
        fields = (
            'id', 'nome'
        )

    def validate(self, data):
        if Editora.objects.filter(nome=data['nome']).exists():
            raise serializers.ValidationError('Já possui uma editora com esse nome')
        return data


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = (
            'id', 'nome'
        )


class TituloSerializer(serializers.HyperlinkedModelSerializer):
    estoque = serializers.ReadOnlyField()
    categoria = CategoriaSerializer(many=False, read_only=True)
    editora = EditoraSerializer(many=False, read_only=True)
    autor = AutorSerializer(many=False, read_only=True)

    class Meta:
        model = Titulo
        fields = (
            'id', 'nome', 'descricao', 'isbn', 'autor', 'estoque',
            'categoria', 'preco_aluguel', 'editora', 'ano'
        )

    def validate(self, data):
        if Titulo.objects.filter(nome=data['nome']).exists():
            raise serializers.ValidationError('Já possui um título com esse nome')
        return data


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    titulo = TituloSerializer(many=False, read_only=True)

    class Meta:
        model = Livro
        fields = (
            'id',
            'numero',
            'titulo',
            'data_cadastro'
        )

    def validate(self, data):
        if Livro.objects.filter(numero=data['numero']).exists():
            raise serializers.ValidationError('Esse livro já foi cadastrado.')
        return data


class ReservaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reserva
        fields = (
            'id',
            'titulo',
            'usuario',
            'data_reserva',
            'ativa'
        )


class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UsuarioSerializer(many=False, read_only=True)
    livro = LivroSerializer(many=False, read_only=True)

    class Meta:
        model = Emprestimo
        fields = (
            'id',
            'livro',
            'usuario',
            'quantidade_dias',
            'data_emprestimo',
            'data_devolucao'
        )

    def validate(self, data):
        from core.models import Emprestimo

        if Emprestimo.objects.filter(usuario=data['usuario']).filter(data_devolucao__isnull=True):
            raise serializers.ValidationError('O já fez 1 Livro emprestimo. O limite máximo é 1')
        return data
