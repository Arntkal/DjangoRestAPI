from django.db import models

# Create your models here.
class Arquivo(models.Model):
    nome_do_arquivo = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class ArquivoBase64(models.Model):
    idArquivo = models.ForeignKey(Arquivo, on_delete=models.PROTECT)
    arquivo_base64 = models.CharField(max_length=10000)
    
class DadosDoArquivo(models.Model):
    idArquivo = models.ForeignKey(Arquivo, on_delete=models.PROTECT)
    dados_do_arquivo = models.CharField(max_length=5000) 