from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Produto, Pedido, Cliente
from .serializers import ProdutoSerializer, PedidoSerializer, ClienteSerializer

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class PedidoViewSet(ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
