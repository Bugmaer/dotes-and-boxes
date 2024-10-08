import socket

HOST = "127.0.0.1"
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"Teste")   # o "B" significa bytes
    data = s.recv(1024)
    print(f"recebido: {data!r}")  # !r transforma b em str