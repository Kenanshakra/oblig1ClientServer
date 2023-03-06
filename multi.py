import socket
import threading

def handleClient(clientSocket, clientAddr):
    # Receive the request message from the client
    request = clientSocket.recv(1024).decode()
    print(f"Received request from {clientAddr}: {request}")

    # Extract the requested file name from the request
    filename = request.split()[1]
    try:
        # Open the file and read its contents
        with open(filename, 'rb') as file:
            response = b"HTTP/1.1 200 :) OK\r\n\r\n" + file.read()
    except FileNotFoundError:
        response = b"HTTP/1.1 404 :( Not Found\r\n\r\n"
    # Send the response header and the file contents to the client
    clientSocket.sendall(response)
    clientSocket.close()

def main():
    # Create a server socket using IPv4 and TCP
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Define the IP address and port number the server will listen to
    # In this case, the server will listen to IP-adresse on port 12000
    serverAddr = ('127.0.0.1', 12000)
    # Bind the server socket to the IP address and port number
    serverSocket.bind(serverAddr)
    # Start listening for incoming connections
    serverSocket.listen(3)
    print(f"Started server at {'127.0.0.1'}:{12000}")
    # Main loop that waits for incoming connections and handles them
    while True:
        # Wait for an incoming connection
        clientSocket, clientAddr = serverSocket.accept()
        print(f"Accepted connection from {clientAddr}")
        t = threading.Thread(target=handleClient, args=(clientSocket, clientAddr))
        t.start()

if __name__ == '__main__':
    main()
