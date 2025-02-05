def marcar_como_lida(notificacao):
    notificacao['Status'] = 'LIDA'

notificacao = {
    'Remetente': 'Sistema',
    'Destinatário': 'Usuário',
    'Mensagem': 'Você tem uma nova atualização disponível.',
    'Status': 'NAO_LIDA'
}

print('Status antes:', notificacao['Status'])

marcar_como_lida(notificacao)

print('Status depois:', notificacao['Status'])