# Generated by Django 3.2.5 on 2021-07-05 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_do_arquivo', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='DadosDoArquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dados_do_arquivo', models.CharField(max_length=5000)),
                ('idArquivo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docFlexiCapture.arquivo')),
            ],
        ),
    ]
