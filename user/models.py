import re

from django.contrib.auth.models import AbstractUser, UserManager
from django.core import validators
from django.db import models


# Create your models here.
class Usuario(AbstractUser):
    TIPO_USUARIO = (
        ('GERENTE', 'gerente'),
        ('CLIENTE', 'cliente'),
    )
    username = models.CharField(
        "Nome do Usuário",
        max_length=30,
        unique=True,
        validators=[validators.RegexValidator(re.compile(r"^[\w.@+-]+$"),
                                              "O nome do user so pode conter letras, digitos ou os""seguintes caracteres @/./+/-/_"
                                              "invalid")])
    email = models.EmailField("E-mail", unique=True)
    nome = models.CharField("Nome", max_length=100, blank=False)
    data_de_entrada = models.DateTimeField("Data de entrada", auto_now_add=True)
    tipo_usuario = models.CharField('Tipo Usuario', choices=TIPO_USUARIO, null=False, default='CLIENTE', max_length=255)
    # objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    
    def save(self, **kwargs):
        self.set_password(self.password)
        super().save(**kwargs)

    
    def __str__(self):
        return self.username
