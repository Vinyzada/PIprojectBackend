from rest_framework.serializers import ModelSerializer
from .models import Produto, Pedido, Cliente

class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'


class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'