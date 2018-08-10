from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class Usuario(AbstractUser):
    
    TIPO_USUARIO = (
        ('GERENTE', 'gerente'),
        ('CLIENTE', 'cliente'),
    )

    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField("E-mail", null=True, blank=True, verbose_name="Email")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    tipo_usuario = models.CharField(choices=TIPO_USUARIO, max_length=255, default='CLIENTE', verbose_name="Tipo do Usuário")
    

    REQUIRED_FIELDS = ["nome"]

    def save(self, **kwargs):
        self.set_password(self.password)
        super().save(**kwargs)

    def __str__(self):
        return str(self.nome)
