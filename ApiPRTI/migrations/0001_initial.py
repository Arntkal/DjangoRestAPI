# Generated by Django 3.2.8 on 2021-10-05 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base64', models.CharField(max_length=65535)),
                ('processado', models.IntegerField(default='0')),
                ('dataSolicitacao', models.DateTimeField(verbose_name='date published')),
                ('retorno', models.CharField(max_length=65535, null=True)),
                ('usuario', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'solicitacoes',
            },
        ),
    ]
