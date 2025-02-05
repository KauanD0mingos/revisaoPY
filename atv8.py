def buscar_contato(agenda_telefonica, nome):
    for contato in agenda_telefonica:
        if contato['Nome'].lower() == nome.lower():
            return contato
    return None

agenda_telefonica = [
    {'Nome': 'Alice Souza', 'Telefone': '11987654321', 'Email': 'alice@email.com'},
    {'Nome': 'Bruno Mendes', 'Telefone': '11912345678', 'Email': 'bruno@email.com'},
    {'Nome': 'Carla Lima', 'Telefone': '21987651234', 'Email': 'carla@email.com'}
]

nome_busca = 'Bruno Mendes'
contato_encontrado = buscar_contato(agenda_telefonica, nome_busca)

if contato_encontrado:
    print('Contato encontrado:', contato_encontrado)
else:
    print('Contato não encontrado.')
