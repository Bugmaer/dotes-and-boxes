# https://realpython.com/python-sockets/#tcp-sockets
import socket

# ECHO SERVICE

# hostname, é o nome do computador na qual a
# aplicação vai rodar. TODA E QUALQUER ESTAÇÃO,
# se chama, internamente, de LOCALHOST ou,
# alternativamente, pelo endereço "127.0.0.1"
HOST = "127.0.0.1"
PORT = 1234


# existem 3 tipos de socket
# SOCK_STREAM => TCP
# SOCK_DGRAM  => UDP (user datagram protocol)
# SOCK_RAW    => precisa fazer os cabeçalhos no braço
# AF_INET => IPv4
# AF_INET => IPv6
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # aloca a porta designada
    s.listen()  # começa a escutar na porta designada

    # conn => descritor da conexão
    # addr => endereço de quem conectou
    conn, addr = s.accept()  # aceita uma conexão

    with conn:  # conexão é "fechável"
        print(f"conexão veio de: {addr}")

        while True:
            data = conn.recv(1024)  # recebe até 1024 bytes
            if not data:
                break
            conn.sendall(data)


exit(0)


# exemplo 1: abrindo, escrevendo e fechando no braço
file = open("arquivo.txt", "w+")
file.write("string qualquer")
file.close()

# exemplo 2: abrindo e escrevendo com 'with'
with open("arquivo.txt") as file:
    file.write("string qualquer")


# exemplo de função que retorna dois valores
def bhaskara(a, b, c):
    r1 = 1
    r2 = 2
    return r1, r2


r1, r2 = bhaskara(1, 3, 2)