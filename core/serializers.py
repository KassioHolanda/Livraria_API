from rest_framework import serializers

from core.models import Titulo, Livro, Emprestimo
import datetime


class TituloSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Titulo
        fields = (
            'pk',
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

    def validate(self, data):
        pass
        #if Titulo.objects.filter(descricao=data['descricao']).exists():
        #    raise serializers.ValidationError('ja possui um titulo com essa descrição')
    


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

    def validate(self, data):
        if Emprestimo.objects.filter(usuario=data['usuario']).filter(devolvido=False):
            raise serializers.ValidationError('usuario ja possui emprestimos')
        if data['data_devolucao'].date <= datetime.date.today():
            raise serializers.ValidationError('verifique a data de devolução')
