from django.db import models
from datetime import datetime

class Solicitacoes(models.Model):
    class Meta:
        db_table = 'solicitacoes'

    base64 = models.CharField(max_length=65535)
    processado = models.IntegerField(default='0')
    dataSolicitacao = models.DateTimeField(blank=True, null=True, default=datetime.now)
    retorno = models.CharField(max_length=65535, null=True)
    usuario = models.CharField(max_length=20)

    def __str__(self):
        return self.usuario, self.dataSolicitacao
