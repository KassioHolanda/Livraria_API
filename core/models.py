from django.db import models


# Create your models here.
class Livro(models.Model):
    registro = models.IntegerField('Registro', null=False)
    titulo = models.ForeignKey('Titulo', null=False, on_delete=models.CASCADE)

    # emprestado = models.BooleanField('Emprestado?', null=False, default=False)

    def __str__(self):
        return self.registro


class Titulo(models.Model):
    descricao = models.CharField('Descricao', max_length=255, null=False)
    autor = models.CharField('Autor', max_length=255, null=False)
    preco = models.FloatField('Preço Livro', null=False)
    genero = models.CharField('Genero Livro', null=False, max_length=255)
    quantidade_estoque = models.IntegerField('Quantidade Estoque', null=False, default=0)
    gerente = models.ForeignKey('user.Usuario', null=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ('descricao',)

    # @property
    # def quantidade_estoque(self):
    #     return Livro.objects.filter(titulo=self).filter(emprestado=False).count()

    def __str__(self):
        return self.descricao


class Emprestimo(models.Model):
    titulo = models.ForeignKey(Titulo, related_name='titulo_emprestimo', on_delete=models.CASCADE)
    usuario = models.ForeignKey('user.Usuario', related_name='meus_emprestimos', on_delete=models.CASCADE)
    data = models.DateField('Data Emprestimo', auto_now_add=True)
    devolvido = models.BooleanField('Emprestimo Devolvido', default=False)
    data_devolucao = models.DateField('Data Devolução', null=True)



    # def __str__(self):
    #     if self.devolvido:
    #         return 'O titulo ' + self.titulo + ' foi Devolvido.'
    #     return 'O titulo ' + self.titulo + ' ainda esta em empretimo.'
