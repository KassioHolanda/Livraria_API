# Generated by Django 2.1 on 2018-08-10 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='titulo',
            name='estoque',
        ),
        migrations.AlterField(
            model_name='titulo',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titulos', to='core.Autor', verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='titulo',
            name='categoria',
            field=models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, related_name='titulos', to='core.Categoria', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='titulo',
            name='editora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titulos', to='core.Editora', verbose_name='Editora'),
        ),
    ]