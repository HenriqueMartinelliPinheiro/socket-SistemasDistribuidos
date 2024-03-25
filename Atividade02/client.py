import socket

# Configurações do cliente
HOST = '127.0.0.1'
PORT = 12345

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Recebendo e respondendo às questões
while True:
    question = client_socket.recv(1024).decode()
    if not question:
        break
    
    print(question)
    print(client_socket.recv(1024).decode())
    print("Digite a resposta: ")
    answer = input()
    client_socket.send(answer.encode())

# Recebendo feedback
feedback = client_socket.recv(1024).decode()
print("teste")
print(feedback)

# Fechamento da conexão
client_socket.close()
