from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.files.storage import default_storage
from .forms import CarregamentoDoArquivo, JSONParaTabela
from .script import ChamadaAPI
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
def index(request):
    template = loader.get_template('base/index.html')
    context = {'texto' : ' Maurício'}
    return HttpResponse(template.render(context, request))

# View de formulário de envio de arquivo
@staff_member_required
def formUpload(request):
    if request.method == 'POST':
        form = CarregamentoDoArquivo(request.POST, request.FILES)
        if form.is_valid():
            #tratamento API
            base64 = ChamadaAPI(request.FILES['arquivo'])
            json = JSONParaTabela(base64)
            #tratamento PDF
            file = request.FILES['arquivo']
            pathFile = file.name
            file_name = default_storage.save(pathFile, file)
            #Reading file from storage
            file = default_storage.open(file_name)
            file_url = default_storage.url(file_name)
            #Mostrar no template a URL do PNG
            PeDeEfe = f'<embed src="..{file_url}" type="application/pdf" height="1000" width="100%">'
            
            #return HttpResponseRedirect('/success/url/')
            template = loader.get_template('base/formUpload.html')
            context = {'texto' : json, 'image' : PeDeEfe }
            return HttpResponse(template.render(context, request))
    else:
        form = CarregamentoDoArquivo()
        return render(request, 'base/formUpload.html', {'form': form})
    
