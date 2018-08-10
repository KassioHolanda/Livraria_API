from django.db import models

class Editora(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Editora')

class Autor(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Autor')
    data_nascimento = models.DateField(null=True, blank=True, verbose_name='Data de Nascimento')


class Categoria(models.Model):
    nome = models.CharField(max_length=255, verbose_name='Nome da Categoria')

class Livro(models.Model):
    numero = models.IntegerField(verbose_name="Número")
    titulo = models.ForeignKey('Titulo', on_delete=models.CASCADE, verbose_name="Título")
    data_cadastro =  models.DateField(auto_now_add=True, verbose_name="Data do Cadastro")


    def __str__(self):
        return str(self.numero)


class Titulo(models.Model):
    nome = models.CharField(max_length=255, verbose_name="Nome")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    isbn = models.CharField(max_length=255, verbose_name="ISBN")
    autor = models.ForeignKey('core.Autor', on_delete=models.CASCADE, verbose_name="Autor")
    preco_aluguel = models.DecimalField(max_digits=20, decimal_places=2, verbose_name="Preço do Aluguel")
    categoria = models.ForeignKey('core.Categoria', max_length=255, on_delete=models.CASCADE, verbose_name="Categoria")
    estoque = models.IntegerField(default=0, verbose_name="Quantidade em Estoque")
    editora = models.ForeignKey('core.Editora', on_delete=models.CASCADE, verbose_name="Editora")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")
    ano = models.IntegerField(verbose_name="Ano do Livro")


    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


class Emprestimo(models.Model):
    livro = models.ForeignKey('core.Livro', related_name='emprestimos', on_delete=models.CASCADE, verbose_name="Livro")
    usuario = models.ForeignKey('user.Usuario', related_name='emprestimos', on_delete=models.CASCADE, verbose_name="Usuário")
    quantidade_dias = models.IntegerField(default=1, verbose_name="Dias Emprestado")
    data_emprestimo = models.DateField(auto_now_add=True, verbose_name="Data do Emprestimo")
    data_devolucao = models.DateField(auto_now_add=True, verbose_name="Data da devolução")
    devolvido = models.BooleanField(default=False, verbose_name="Emprestimo já devolvido ?")


class Reserva(models.Model):
    titulo = models.ForeignKey('core.Titulo', related_name='reservas', on_delete=models.CASCADE, verbose_name="Título")
    usuario = models.ForeignKey('user.Usuario', related_name='reservas', on_delete=models.CASCADE, verbose_name="Usuário")
    data_reserva = models.DateField(auto_now_add=True, verbose_name="Data da Reserva")
    ativa = models.BooleanField(default=False, verbose_name="Reserva Ativa ?")



