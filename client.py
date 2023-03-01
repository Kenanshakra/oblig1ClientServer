from socket import *


def main():
    message ="Hello world"

    # Serverens IP-adresse og port
    server_ip = '127.0.0.1'
    port = 12000

    # Create a socket and connect to the server
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_ip, port))

    # Send data
    client_socket.send(message.encode())

    # Receive and print the response
    response = b""
    while True:
        data = client_socket.recv(1024).decode()
        print (data)
        if not data:
            break
        response += data

    print(response.decode())
    client_socket.close()

if __name__=='__main__':
    main()
