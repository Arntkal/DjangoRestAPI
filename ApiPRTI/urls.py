from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^API/$', views.listaDeSolicitacoes.as_view(), name='lista-solicitacoes'),
]