from rest_framework import serializers

from user.models import Usuario


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'pk',
            'username',
            'email',
            'nome',
            'tipo_usuario',
        )

class UserDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = (
            'url',
            'username',
            'email',
            'nome',
            'tipo_usuario',
        )
