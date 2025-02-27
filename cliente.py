import socket

from view import View

HOST = "127.0.0.1"
PORTA = 4321

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente_socket.connect((HOST, PORTA))

# View.ExtrairDados() retorna um json
cliente_socket.send(View.ExtrairDados().encode())  

cliente_socket.close()
