from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.admin.decorators import register
from .models import Usuario

@register(Usuario)
class UsuarioAdmin(ModelAdmin):
    fields = ('nome','username' ,'email', 'tipo_usuario', 'password')

