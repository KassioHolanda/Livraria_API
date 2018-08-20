from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from core.models import Reserva, Emprestimo


class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('BIBLIOTECÁRIO', 'BIBLIOTECÁRIO'),
        ('USUÁRIO', 'USUÁRIO'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=255, default='USUARIO',
                                    verbose_name="Tipo do Usuário")

    REQUIRED_FIELDS = ["nome"]

    @property
    def minhas_reservas(self):
        return Reserva.objects.filter(usuario=self)

    @property
    def meus_emprestimos(self):
        return Emprestimo.objects.filter(usuario=self)

    def save(self, **kwargs):
        self.set_password(self.password)
        super().save(**kwargs)

    def __str__(self):
        return str(self.nome)

    class Meta:
        ordering = ['-id']
