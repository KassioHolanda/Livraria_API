from django.db import models


# Create your models here.
class Livro(models.Model):
    preco = models.FloatField('Preço Livro', null=False)
    # quantidade = models.IntegerField('Quantidade Estoque', null=False, default=0)
    genero = models.CharField('Genero Livro', null=False, max_length=255)
    titulo = models.ForeignKey('Titulo', null=False, on_delete=models.CASCADE)



class Titulo(models.Model):
    descricao = models.CharField('Descricao', max_length=255, null=False)
    autor = models.CharField('Autor', max_length=255, null=False)
    quantidade_estoque = models.IntegerField('Quantidade Estoque', null=False, default=0)
    gerente = models.ForeignKey('user.User', null=False, on_delete=models.CASCADE)

    # titulo =

    def __str__(self):
        return self.descricao


class Emprestimo(models.Model):
    titulo = models.ForeignKey(Titulo, related_name='titulo_emprestimo', on_delete=models.CASCADE)
    usuario = models.ForeignKey('user.User', related_name='meus_emprestimos', on_delete=models.CASCADE)
    quantidade_dias_emprestimo = models.IntegerField('Quantidade De Dias de Emprestimo', null=False)
    data = models.DateTimeField('Data Emprestimo', auto_now_add=True)
    devolvido = models.BooleanField('Emprestimo Devolvido', default=False, null=False)
    data_devolucao = models.DateTimeField('Data Devolução', null=True)

    # def __str__(self):
    #     if self.devolvido:
    #         return 'O titulo ' + self.titulo + ' foi Devolvido.'
    #     return 'O titulo ' + self.titulo + ' ainda esta em empretimo.'
