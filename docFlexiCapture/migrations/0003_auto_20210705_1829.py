# Generated by Django 3.2.5 on 2021-07-05 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docFlexiCapture', '0002_arquivobase64'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='arquivobase64',
            name='idArquivo',
        ),
        migrations.RemoveField(
            model_name='dadosdoarquivo',
            name='idArquivo',
        ),
        migrations.DeleteModel(
            name='Arquivo',
        ),
        migrations.DeleteModel(
            name='ArquivoBase64',
        ),
        migrations.DeleteModel(
            name='DadosDoArquivo',
        ),
    ]
