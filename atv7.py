def emprestar_livro(livro):
    if livro['Quantidade de cópias disponíveis'] > 0:
        livro['Quantidade de cópias disponíveis'] -= 1
        return True
    return False

livro = {
    'Título': 'Dom Quixote',
    'Autor': 'Miguel de Cervantes',
    'Ano de publicação': 1605,
    'Quantidade de cópias disponíveis': 3
}

if emprestar_livro(livro):
    print('Empréstimo realizado com sucesso!')
else:
    print('Livro indisponível para empréstimo.')

print('Cópias disponíveis após empréstimo:', livro['Quantidade de cópias disponíveis'])