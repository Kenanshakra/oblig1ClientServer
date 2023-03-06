from socket import *
import sys
def main():
    # Create a server socket using IPv4 and TCP
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Define the IP address and port number the server will listen to
    # In this case, the server will listen to IP-adresse on port 12000
    serverAddr = ('127.0.0.1', 12000)

    # Bind the server socket to the IP address and port number
    serverSocket.bind(serverAddr)

    # Start listening for incoming connections
    serverSocket.listen(1)

    # Main loop that waits for incoming connections and handles them
    while True:
        # Print a message indicating that the server is ready to accept connections
        print('Ready to serve...')

        # Wait for an incoming connection
        connectionSocket, addr = serverSocket.accept()

        # Receive the request message from the client
        message = connectionSocket.recv(1024).decode()

        # Extract the filename from the request message
        filename = message.split()[1]
        print(filename)

        try:
            # Open the file and read its contents
            f = open(filename[1:])
            outputdata = f.read()

            # Send the HTTP response header with a status code of 200 (OK)
            response = "HTTP/1.1 200 OK :) \r\n\r\n"

            # Send the response header and the file contents to the client
            connectionSocket.send(response.encode())
            for i in range(0, len(outputdata)):
                connectionSocket.send(outputdata[i].encode())
            connectionSocket.send("\r\n".encode())

            # Close the connection socket
            connectionSocket.close()

        except IOError:
            # If the file cannot be opened, send a 404 (Not Found) error response
            response = "HTTP/1.1 404 :( Not Found\r\n\r\n"
            connectionSocket.send(response.encode())

            # Close the connection socket
            connectionSocket.close()

    # Close the server socket and exit the program
    serverSocket.close()
    sys.exit()
if __name__ == '__main__':
 main()
