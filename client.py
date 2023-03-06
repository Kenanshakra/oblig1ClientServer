from socket import *


def main():
    message ="Hello world"

    # Serverens IP-adresse og port
    serverAddr = ('127.0.0.1', 12000)

    # Create a socket and connect to the server
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(serverAddr)

    # Send data
    clientSocket.send(message.encode())

    # Receive and print the response
    response = b""
    while True:
        data = clientSocket.recv(1024).decode()
        print (data)
        if not data:
            break
        response += data

    print(response.decode())
    clientSocket.close()

