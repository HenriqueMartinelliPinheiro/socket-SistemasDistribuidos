import socket

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 12345

# Lista de questões com suas alternativas e respostas corretas
questions = [
    {
        'question': 'Qual é a capital do Brasil?',
        'options': ['A) Rio de Janeiro', 'B) São Paulo', 'C) Brasília', 'D) Salvador'],
        'answer': 'C'
    },
    {
        'question': 'Quem escreveu "Dom Quixote"?',
        'options': ['A) Miguel de Cervantes', 'B) William Shakespeare', 'C) Machado de Assis', 'D) Franz Kafka'],
        'answer': 'A'
    }
]

# Função para enviar questões ao cliente
def send_question(client_socket, question):
    client_socket.send(question['question'].encode())
    client_socket.send('\n'.encode())
    for option in question['options']:
        client_socket.send(option.encode())
        client_socket.send('\n'.encode())

# Criação do socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Aguardando conexão...')

# Aceita conexão do cliente
client_socket, addr = server_socket.accept()
print('Conexão estabelecida com', addr)

# Enviando e verificando respostas
correct_answers = 0
for question in questions:
    send_question(client_socket, question)
    answer = client_socket.recv(1024).decode().strip()
    if answer == question['answer']:
        correct_answers += 1

# Enviando feedback ao aluno
feedback = f'Você respondeu {len(questions)} questões. Acertou {correct_answers}.'
client_socket.send(feedback.encode())

# Fechamento da conexão
client_socket.close()
server_socket.close()