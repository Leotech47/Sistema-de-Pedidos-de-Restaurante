Claro! Aqui está o texto explicativo em **Markdown** sobre o funcionamento do código:

````markdown
# Explicação do Código - Classe Pedido

O objetivo deste código é representar um pedido em um restaurante utilizando programação orientada a objetos, somando os valores dos itens adicionados e exibindo o total da conta.

---

## Estrutura do Código

### 1. Classe `Pedido`

```python
class Pedido:
    def __init__(self):
        self.itens = []
````

* O construtor `__init__` inicializa uma lista vazia `self.itens` para armazenar os preços dos itens pedidos.

---

### 2. Método `adicionar_item`

```python
def adicionar_item(self, preco):
    self.itens.append(preco)
```

* Esse método recebe um valor `preco` e o adiciona à lista de itens.

---

### 3. Método `calcular_total`

```python
def calcular_total(self):
    return sum(self.itens)
```

* Retorna a **soma de todos os preços** contidos na lista `self.itens`.

---

## Lógica Principal do Programa

### 4. Leitura da Quantidade de Itens

```python
quantidade_pedidos = int(input().strip())
```

* Lê a quantidade de itens que serão inseridos no pedido.

---

### 5. Criação de um Objeto da Classe `Pedido`

```python
pedido = Pedido()
```

* Instancia a classe `Pedido`.

---

### 6. Leitura dos Itens

```python
for _ in range(quantidade_pedidos):
    entrada = input().strip()
    nome, preco = entrada.rsplit(" ", 1)
    preco = float(preco)
    pedido.adicionar_item(preco)
```

* Para cada item:

  * Lê uma linha com o nome do item e o preço.
  * Separa o nome do preço usando `rsplit(" ", 1)`.
  * Converte o preço para `float`.
  * Adiciona o preço ao pedido.

---

### 7. Exibição do Total

```python
print(f"{pedido.calcular_total():.2f}")
```

* Chama o método `calcular_total` da instância `pedido` e imprime o total com **duas casas decimais**, no formato exigido.

---

## Exemplo de Entrada e Saída

### Entrada:

```
3
Hamburguer 15.50
Refrigerante 5.00
Batata 8.00
```

### Saída:

```
28.50
```

---

## Observação Importante

> **Atenção**: As entradas e saídas devem seguir rigorosamente o formato definido para que o código funcione corretamente e passe em testes automatizados.

```
```
