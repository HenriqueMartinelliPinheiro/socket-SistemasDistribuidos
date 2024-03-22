import socket
import os

HOST = "127.0.0.1"
PORT = 8088

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))

servidor.listen()

cliente, endereco = servidor.accept()

nome_arquivo = cliente.recv(1024).decode()

if not os.path.exists(nome_arquivo):
    cliente.send("Arquivo não encontrado".encode())
    cliente.close()
    servidor.close()
    exit()

arquivo = open(nome_arquivo, "rb")

tamanho_arquivo = os.path.getsize(nome_arquivo)
cliente.send(str(tamanho_arquivo).encode())

while True:
    buffer = arquivo.read(1024)
    if not buffer:
        break
    cliente.send(buffer)

arquivo.close()
cliente.close()
servidor.close()

print("Arquivo enviado com sucesso!")
