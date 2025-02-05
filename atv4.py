# Implemente um dicionário chamado “produto” que represente um item no estoque de uma loja com as seguintes propriedades:

# Nome do produto
# Quantidade em estoque
# Preço unitário

# Crie uma função “atualiza_estoque(produto: dict, quantidade: int)” que recebe o dicionário do produto e some a quantidade informada ao estoque, após isso, retorne o produto atualizado e imprima na tela.

def atualiza_estoque(produto, nova_quantidade):
    produto['quantidade em estoque'] += nova_quantidade
    
produto = {
    'nome':'Café',
    'quantidade em estoque':100,
    'preço':16.00
}

novaqtd = 10
    
atualiza_estoque(produto, novaqtd)
print(produto)
    