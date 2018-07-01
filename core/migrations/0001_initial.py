from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_dias_emprestimo', models.IntegerField(verbose_name='Quantidade De Dias de Emprestimo')),
                ('data', models.DateTimeField(auto_now_add=True, verbose_name='Data Emprestimo')),
                ('devolvido', models.BooleanField(default=False, verbose_name='Emprestimo Devolvido')),
                ('data_devolucao', models.DateTimeField(null=True, verbose_name='Data Devolução')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registro', models.IntegerField(verbose_name='Registro')),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255, verbose_name='Descricao')),
                ('autor', models.CharField(max_length=255, verbose_name='Autor')),
                ('preco', models.FloatField(verbose_name='Preço Livro')),
                ('genero', models.CharField(max_length=255, verbose_name='Genero Livro')),
                ('quantidade_estoque', models.IntegerField(default=0, verbose_name='Quantidade Estoque')),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('descricao',),
            },
        ),
        migrations.AddField(
            model_name='livro',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Titulo'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='titulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titulo_emprestimo', to='core.Titulo'),
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meus_emprestimos', to=settings.AUTH_USER_MODEL),

        ),
    ]
