# Generated by Django 3.2.5 on 2021-07-05 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docFlexiCapture', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArquivoBase64',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo_base64', models.CharField(max_length=10000)),
                ('idArquivo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='docFlexiCapture.arquivo')),
            ],
        ),
    ]
