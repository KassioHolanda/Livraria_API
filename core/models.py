from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Editora')

    @property
    def titulos(self):
        return Titulo.objects.filter(editora=self)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Autor(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Autor')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')

    @property
    def titulos(self):
        return Titulo.objects.filter(autor=self)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Categoria(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome da Categoria')

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Livro(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    titulo = models.ForeignKey('Titulo', on_delete=models.CASCADE, verbose_name="Título")
    data_cadastro =  models.DateField(auto_now_add=True, verbose_name="Data do Cadastro")


    def __str__(self):
        return str(self.numero)

    class Meta:
        ordering = ['numero']


class Titulo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    isbn = models.CharField(max_length=255, verbose_name="ISBN")
    autor = models.ForeignKey('core.Autor', related_name="titulos", on_delete=models.CASCADE, verbose_name="Autor")
    preco_aluguel = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Preço do Aluguel")
    categoria = models.ForeignKey('core.Categoria', related_name="titulos", max_length=255, on_delete=models.CASCADE, verbose_name="Categoria")
    editora = models.ForeignKey('core.Editora', related_name="titulos", on_delete=models.CASCADE, verbose_name="Editora")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ano = models.IntegerField(verbose_name="Ano do Livro")
    estoque = models.IntegerField(verbose_name='Estoque', default=0)

    # @property
    # def estoque(self):
    #     from core.models import Livro, Emprestimo
    #     emprestados = Emprestimo.objects.filter(livro__titulo=self).count()
    #     estoque = Livro.objects.filter(titulo=self).count()
    #     return estoque - emprestados


    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']


class Emprestimo(models.Model):
    titulo = models.ForeignKey('core.Titulo', related_name='emprestimos', on_delete=models.CASCADE, verbose_name="Titulo")
    usuario = models.ForeignKey('user.Usuario', related_name='emprestimos', on_delete=models.CASCADE, verbose_name="Usuário")
    quantidade_dias = models.IntegerField(default=1, verbose_name="Dias Emprestado")
    data_emprestimo = models.DateTimeField(auto_now_add=True, verbose_name="Data do Emprestimo")
    data_devolucao = models.DateTimeField(null=True, blank=True, verbose_name="Data da devolução")

    class Meta:
        ordering = ['-id']


class Reserva(models.Model):
    titulo = models.ForeignKey('core.Titulo', related_name='reservas', on_delete=models.CASCADE, verbose_name="Título")
    usuario = models.ForeignKey('user.Usuario', related_name='reservas', on_delete=models.CASCADE, verbose_name="Usuário")
    data_reserva = models.DateField(auto_now_add=True, verbose_name="Data da Reserva")
    ativa = models.BooleanField(default=True, verbose_name="Reserva Ativa ?")

    class Meta:
        ordering = ['-id']

