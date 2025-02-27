import json
import socket
from view import View


HOST = "0.0.0.0"
PORTA = 4321

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor_socket.bind((HOST, PORTA))
servidor_socket.listen(20)  


while True:
    cliente, endereco = servidor_socket.accept()

    dados = json.loads(cliente.recv(1024).decode() )
    
    View.Inserir(dados)
    
    cliente.close()