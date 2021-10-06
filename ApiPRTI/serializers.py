
from rest_framework import serializers
from .models import Solicitacoes

class SolicitacoesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Solicitacoes
        fields = '__all__'
        read_only_fields = ['usuario', 'processado', 'dataSolicitacao', 'retorno']

    def validate(self, attrs):
        attrs['usuario'] = self.context['request'].user
        return attrs