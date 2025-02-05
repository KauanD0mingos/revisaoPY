# Crie um dicionário chamado “aluno” que represente um estudante com as seguintes informações:

# Nome
# Idade
# Curso
# Notas (uma lista de notas)

listaNotas = []

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
curso = input('Digite o curso que está cursando: ')

for i in range(3):
    notas = float(input('Informe suas notas: '))
    listaNotas.append(i)

aluno = {
    'nome': nome,
    'idade': idade,
    'curso': curso,
    'notas': notas   
}

for c in aluno.items():
    print(c)