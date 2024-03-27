import socket

HOST = '127.0.0.1'
PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

total_questoes = int(client_socket.recv(1024).decode())
print("Serão feitas ",total_questoes," perguntas.")

for i in range(total_questoes):
    question = client_socket.recv(2048).decode()
    print(question.replace("/",""))
    print("Digite a resposta: ")
    answer = input()
    client_socket.send(answer.encode())

feedback = client_socket.recv(2048).decode()
print(feedback)

client_socket.close()
