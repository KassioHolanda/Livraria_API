from rest_framework import serializers

from core.models import Titulo, Livro, Emprestimo


class TituloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titulo
        fields = (
            'descricao',
            'autor',
            'quantidade_estoque',
            'gerente',
        )


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    titulo = serializers.SlugRelatedField(queryset=Titulo.objects.all(), slug_field='descricao')

    class Meta:
        model = Livro
        fields = (
            'pk',
            'preco',
            'genero',
            'titulo',

        )


class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    usuario = serializers.SlugRelatedField(queryset=Emprestimo.objects.all(), slug_field='nome')

    class Meta:
        model = Emprestimo
        fields = (
            'pk',
            'titulo',
            'usuario',
            'quantidade_dias_emprestimo',
            'data',
            'devolvido',
            'data_devolucao',
        )
