import socket

def main():
    HOST = '127.0.0.1'  # O mesmo endereço IP do servidor
    PORT = 65432        # A mesma porta do servidor

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    while True:
        message = client_socket.recv(1024).decode()
        if message == 'VEZ_DE_JOGAR':
            jogada = input("Digite sua jogada (coluna origem, linha origem, coluna destino, linha destino): ")
            client_socket.sendall(jogada.encode())
        elif message == 'JOGO_TERMINADO':
            print("O jogo terminou. Você pode sair.")
            break

    client_socket.close()

if __name__ == "__main__":
    main()