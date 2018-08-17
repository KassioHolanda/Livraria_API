from rest_framework import serializers

from core.models import Autor
from user.models import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'pk',
            'username',
            'password',
            'email',
            'nome',
            'tipo_usuario',
        )

