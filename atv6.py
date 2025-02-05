def depositar(conta, valor):
    if valor > 0:
        conta['Saldo'] += valor

def sacar(conta, valor):
    if 0 < valor <= conta['Saldo']:
        conta['Saldo'] -= valor
        return True
    return False

conta_bancaria = {
    'Nome do titular': 'João Silva',
    'Número da conta': '123456-7',
    'Saldo': 1000.00
}

depositar(conta_bancaria, 500)
print('Saldo após depósito:', conta_bancaria['Saldo'])  
if sacar(conta_bancaria, 200):
    print('Saque realizado com sucesso!')
else:
    print('Saldo insuficiente!')

print('Saldo final:', conta_bancaria['Saldo']) 