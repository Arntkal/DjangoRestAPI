from django.contrib import admin
from .models import Arquivo, ArquivoBase64, DadosDoArquivo

# Register your models here.
admin.site.register(Arquivo)
admin.site.register(ArquivoBase64)
admin.site.register(DadosDoArquivo)
