from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from ControlePedidos.views import PedidoViewSet, ClienteViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]