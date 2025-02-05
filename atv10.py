def calcular_total(carrinho):
    total = 0
    for item in carrinho:
        total += item['Preço'] * item['Quantidade']
    return total

carrinho = [
    {'Nome': 'Notebook', 'Preço': 3500.00, 'Quantidade': 1},
    {'Nome': 'Mouse', 'Preço': 150.00, 'Quantidade': 2},
    {'Nome': 'Teclado', 'Preço': 200.00, 'Quantidade': 1}
]

total_compra = calcular_total(carrinho)

print('Total da compra: R$', total_compra)