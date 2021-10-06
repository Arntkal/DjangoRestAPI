from django.shortcuts import render
from rest_framework import generics
from .models import Solicitacoes
from .serializers import SolicitacoesSerializer

# Create your views here.
class listaDeSolicitacoes(generics.ListCreateAPIView):

    queryset = Solicitacoes.objects.all()
    serializer_class = SolicitacoesSerializer
