from django.contrib import admin
from .models import Cliente, Produto, Pedido, ProdutosPedido


#Perimite adicionar Produto ao pedido diretamente
class ProdutosPedidoInline(admin.TabularInline):  
    model = ProdutosPedido
    extra = 1
class PedidoAdmin(admin.ModelAdmin):
    inlines = [ProdutosPedidoInline]


admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Pedido, PedidoAdmin)
