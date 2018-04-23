import socket
import select
import sys

if __name__ == "__main__":

    clients = []
    receive_buffer = 1024
    port = int(sys.argv[1])

    server_socket = socket.socket()

    server_socket.bind(("", port))
    server_socket.listen()
    clients.append(server_socket)
    print("Server is started on port " + str(port))
    while 1:
        read_sockets, write_sockets, error_sockets = select.select(clients, [], [])
        for sock in read_sockets:
            if sock == server_socket:
                newsocket, addr = server_socket.accept()
                clients.append(newsocket)
            else:
                try:
                    data = sock.recv(receive_buffer)
                    if data:
                        sock.send(data)
                    else:
                        raise ConnectionResetError()
                except:
                    continue



