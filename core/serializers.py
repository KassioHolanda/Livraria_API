from rest_framework import serializers

from core.models import Titulo, Livro, Emprestimo
import datetime


class TituloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titulo
        fields = (
            'pk',
            'descricao',
            'autor',
            'quantidade_estoque',
            'gerente',
            'genero',
            'preco',
            'gerente',
        )

    def validate(self, data):
        if Titulo.objects.filter(descricao=data['descricao']).exists():
            raise serializers.ValidationError('ja possui um titulo com essa descrição')
        if data['quantidade_estoque'] < 0:
            raise serializers.ValidationError('quantidade em estoque não pode ser negativo')

        return data


class LivroSerializer(serializers.HyperlinkedModelSerializer):
    # titulo = serializers.SlugRelatedField(queryset=Titulo.objects.all(), slug_field='descricao')

    class Meta:
        model = Livro
        fields = (
            'pk',
            'registro',
            'titulo',
        )

    def validate(self, data):
        if Livro.objects.filter(registro=data['registro']).exists():
            raise serializers.ValidationError('ja possui livro com esse registro')
        return data


class EmprestimoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Emprestimo
        fields = (
            'pk',
            'titulo',
            'usuario',
            'devolvido',
            'data_devolucao',
        )
