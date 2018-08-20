from rest_framework import serializers

from core.serializer import *
from user.models import Usuario


class UsuarioSerializer(serializers.HyperlinkedModelSerializer):

    # meus_emprestimos = EmprestimoSerializer(many=True, read_only=True)
    # minhas_reservas = ReservaSerializer(many=True, read_only=True)

    class Meta:
        model = Usuario
        fields = (
            'id',
            'username',
            'password',
            'email',
            'nome',
            'tipo_usuario',
            # 'meus_emprestimos',
            # 'minhas_reservas'
        )

