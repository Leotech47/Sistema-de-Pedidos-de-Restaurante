class Pedido:
    def __init__(self):
        self.itens = []  
    
    # Método para adicionar item
    def adicionar_item(self, preco):
        # Adiciona o preço do item à lista
        self.itens.append(preco)

    # Método para calcular o total
    def calcular_total(self):
        # Retorna a soma de todos os preços
        return sum(self.itens)


quantidade_pedidos = int(input().strip())

pedido = Pedido()

for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    preco = float(preco)
    # Chamada correta do método adicionar_item
    pedido.adicionar_item(preco)

# Exibe o total formatado com duas casas decimais
print(f"{pedido.calcular_total():.2f}")

