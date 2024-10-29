import socket

HOST = "127.0.0.1"
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Digite algo: ")
    n = input()
    data = s.recv(1024)
    print(f"recebido: {data!r}")  # !r transforma b em str