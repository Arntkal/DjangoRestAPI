from django import forms
#from json2table import convert
import base64
import json
import pandas as pd

# My forms
class CarregamentoDoArquivo(forms.Form):
    # formulario = forms.CharField(max_length=50)
    arquivo = forms.FileField()
    
#Conversor de PDF para Base64    
def PDFParaBase64(file):
    fileRead = file.read()
    arquivobase64 = base64.encodebytes(fileRead)
    arquivobase64 = arquivobase64.decode('unicode_escape')
    arquivobase64 = arquivobase64.replace("\n", "")
    return arquivobase64


#Conversor de Base64 para UTF8
def Base64ParaUTF8(file):
    utf8 = file.encode("utf-8")
    utf8 = base64.b64encode(utf8)
    utf8 = base64.decodebytes(utf8)
    utf8 = base64.b64decode(utf8).decode('utf-8-sig')
    return utf8

#Organizador de JSON em Tabela
def JSONParaTabela(json_object):
    json_object = json_object.replace("\n", "")
    json_object = json.loads(json_object)
    json_object = json_object['Documents'][0]['DocumentData']['Fields']
    # t_atrib = {"style" : "width:100%"}
    # html = convert(json_object, build_direction="LEFT_TO_RIGHT", table_attributes=t_atrib)
    tabela = "<table class='table table-striped'>"
    for campo in json_object:
        tabela = f"{tabela}<tr><th scope='row'>{campo['Name']}</th><td>{campo['Value']}</td></tr>"
        
    tabela = f"{tabela}</table>"    
    
    #Definindo o local de salvamento dos arquivos
    path_arquivo = 'docFlexiCapture/files/arquivo.xlsx'
    path_arquivo2 = '../arquivo.xlsx'
    
    table = pd.read_html(tabela)[0]
    table.to_excel(path_arquivo, index=False)
    
    resultado = f"{tabela}<br><div style='width:140px;margin:0 auto;'><a href='{path_arquivo2}' class='btn btn-primary'>Baixar Planilha</a></div>"
    
    return resultado