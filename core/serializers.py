from rest_framework import serializers
from core.models import Titulo, Livro, Emprestimo, Autor, Categoria, Editora
import datetime

class CategoriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'pk', 'nome', 'titulos'
        )


class EditoraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Editora
        fields = (
            'pk', 'nome', 'titulos'
        )


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = (
            'pk', 'nome', 'titulos'
        )


class TituloSerializer(serializers.HyperlinkedModelSerializer):
    estoque = serializers.ReadOnlyField()
    class Meta:
        model = Titulo
        fields = (
            'pk', 'nome', 'descricao','isbn', 'autor','estoque', 
            'categoria', 'preco_aluguel', 'editora','ano'
        )



    #def validate(self, data):
    #    pass
        #if Titulo.objects.filter(descricao=data['descricao']).exists():
        #    raise serializers.ValidationError('ja possui um titulo com essa descrição')
    


class LivroSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Livro
        fields = (
            'pk',
            'numero',
            'titulo',
            'data_cadastro'
        )

    def validate(self, data):
        if Livro.objects.filter(numero=data['numero']).exists():
            raise serializers.ValidationError('Esse livro já foi cadastrado.')
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

    def validate(self, data):
        if Emprestimo.objects.filter(usuario=data['usuario']).filter(devolvido=False):
            raise serializers.ValidationError('usuario ja possui emprestimos')
        if data['data_devolucao'].date <= datetime.date.today():
            raise serializers.ValidationError('verifique a data de devolução')
