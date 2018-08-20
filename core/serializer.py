from rest_framework import serializers
from core.models import Titulo, Livro, Emprestimo, Autor, Categoria, Editora, Reserva
import datetime

from user.models import Usuario
from user.serializer import UsuarioSerializer


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id', 'nome'
        )

    def validate(self, data):
        if Categoria.objects.filter(nome=data['nome']).exists():
            raise serializers.ValidationError('Já possui um categoria com esse nome')
        return data


class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = (
            'id', 'nome'
        )

    def validate(self, data):
        if Editora.objects.filter(nome=data['nome']).exists():
            raise serializers.ValidationError('Já possui uma editora com esse nome')
        return data


class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = (
            'id', 'nome'
        )


class TituloSerializer(serializers.ModelSerializer):
    # categoria = CategoriaSerializer(many=False,read_only=True)
    # editora = EditoraSerializer(many=False,read_only=True)
    # autor = AutorSerializer(many=False,read_only=True)

    class Meta:
        model = Titulo
        fields = (
            'id',
            'nome',
            'descricao',
            'isbn',
            'autor',
            'estoque',
            'categoria',
            'preco_aluguel',
            'editora',
            'ano'
        )


class LivroSerializer(serializers.ModelSerializer):
    # titulo = TituloSerializer(many=False, read_only=True)

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


class ReservaSerializer(serializers.ModelSerializer):
    # titulo = TituloSerializer(many=False, read_only=True)
    # usuario = UsuarioSerializer(many=False, read_only=True)

    class Meta:
        model = Reserva
        fields = (
            'id',
            'titulo',
            'usuario',
            'data_reserva',
            'ativa'
        )


class EmprestimoSerializer(serializers.ModelSerializer):
    # usuario = UsuarioSerializer(many=False, read_only=True)
    # livro = LivroSerializer(many=False, read_only=True)

    class Meta:
        model = Emprestimo
        fields = (
            'id',
            'titulo',
            'usuario',
            'quantidade_dias',
            'data_emprestimo',
            'data_devolucao'
        )

    # def validate(self, data):
    #     from core.models import Emprestimo
    #
    #     if Emprestimo.objects.filter(usuario=data['usuario']).filter(data_devolucao__isnull=True):
    #         raise serializers.ValidationError('Voce já fez um emprestimo. O limite máximo é 1')
    #     return data


class UsuarioSerializerNovo(serializers.ModelSerializer):
    meus_emprestimos = EmprestimoSerializer(many=True, read_only=True)
    minhas_reservas = ReservaSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'password',
            'email',
            'nome',
            'tipo_usuario',
            'meus_emprestimos',
            'minhas_reservas'
        )
