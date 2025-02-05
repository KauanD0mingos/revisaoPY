# Crie uma lista chamada “catalogo” que contenha dicionários representando filmes. Cada dicionário deve conter:

# Título
# Ano de lançamento
# Gênero

# Implemente uma função “filtrar_por_genero(catalogo: list, genero: str)” que recebe a lista de filmes e retorna apenas os filmes que pertencem ao gênero informado. Após retornar, imprima-os em tela.

def filtrar_por_genero(catalogo, genero):
    filmes_filtrados = []
    for filme in catalogo:
        if filme['Gênero'].lower() == genero.lower():
            filmes_filtrados.append(filme)
    return filmes_filtrados

catalogo = [
    {'Título': 'Interestelar', 'Ano de lançamento': 2014, 'Gênero': 'Ficção Científica'},
    {'Título': 'O Poderoso Chefão', 'Ano de lançamento': 1972, 'Gênero': 'Crime'},
    {'Título': 'A Origem', 'Ano de lançamento': 2010, 'Gênero': 'Ficção Científica'},
    {'Título': 'Titanic', 'Ano de lançamento': 1997, 'Gênero': 'Romance'},
    {'Título': 'Clube da Luta', 'Ano de lançamento': 1999, 'Gênero': 'Drama'}
]

genero_desejado = 'Ficção Científica'
filmes_filtrados = filtrar_por_genero(catalogo, genero_desejado)

print('Filmes do gênero', genero_desejado + ':')
for filme in filmes_filtrados:
    print('-', filme['Título'], '(', filme['Ano de lançamento'], ')')