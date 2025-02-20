from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.CharField(max_length=19)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    desc = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome} (R${self.preco})"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) #Vincula um cliente ao pedido
    produtos = models.ManyToManyField(Produto, through='ProdutosPedido') #Vincula uma tabela associativa 
    data = models.DateField()

    def total_pedido(self):
        return sum(item.total_produto() for item in self.produtospedido_set.all()) #Retorna o valor total dos produtos e sua quantidade
    
    def __str__(self):
        return f"Cliente *{self.cliente.nome}*, R${self.total_pedido()} (Pedido {self.id})"

class ProdutosPedido(models.Model): #Tabela que permite com que o pedido possua varios produtos
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE) 
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
    
    def total_produto(self):
        return self.quantidade * self.produto.preco #Retorna o preco total do produto com base na sua quantidade

    def __str__(self):
        return f"{self.produto.nome} {self.quantidade}x Data: {self.pedido.data} Pedido Referente: {self.pedido.id}"
