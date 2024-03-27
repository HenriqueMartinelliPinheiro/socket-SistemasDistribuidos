import socket

HOST = '127.0.0.1'
PORT = 8080

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
    },
    {
        'question': 'Quem pintou a Mona Lisa?',
        'options': ['A) Leonardo da Vinci', 'B) Pablo Picasso', 'C) Vincent van Gogh', 'D) Michelangelo'],
        'answer': 'A'
    },
    {
        'question': 'Qual é o maior planeta do sistema solar?',
        'options': ['A) Terra', 'B) Júpiter', 'C) Saturno', 'D) Marte'],
        'answer': 'B'
    },
    {
        'question': 'Quem foi o primeiro presidente dos Estados Unidos?',
        'options': ['A) Abraham Lincoln', 'B) George Washington', 'C) Thomas Jefferson', 'D) John F. Kennedy'],
        'answer': 'B'
    },
    {
        'question': 'Qual é a montanha mais alta do mundo?',
        'options': ['A) Monte Everest', 'B) Monte Kilimanjaro', 'C) Monte Fuji', 'D) Monte McKinley'],
        'answer': 'A'
    }
]


def send_question(client_socket, question):
    client_socket.send(question['question'].encode())
    client_socket.send('\n'.encode())
    for option in question['options']:
        client_socket.send(option.encode())
        client_socket.send('\n'.encode())

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print('Aguardando conexão...')

client_socket, addr = server_socket.accept()
print('Conexão estabelecida com', addr)

client_socket.sendall(str(len(questions)).encode())

correct_answers = 0
for question in questions:
    send_question(client_socket, question)
    answer = client_socket.recv(1024).decode()
    if answer == question['answer']:
        correct_answers += 1

# Enviando feedback ao aluno
feedback = f'Você respondeu {len(questions)} questões. Acertou {correct_answers}.'
client_socket.send(feedback.encode())

# Fechamento da conexão
client_socket.close()
server_socket.close()
