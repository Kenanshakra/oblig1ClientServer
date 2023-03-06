# oblig1ClientServer
Kenan Abou Shakra, s345510
Task2:
Implement a Simple Web Server:

1.Import the socket module and create a server socket object with AF_INET (IPv4) and SOCK_STREAM (TCP) parameters.
2.Set a fixed port number (e.g., 12345) and bind the socket to the local host with the given port number.
3.Listen for incoming client connections and accept them using the accept() method of the server socket object.
4.Parse the incoming HTTP request message and get the requested file name from it.
5.Check if the requested file is present in the server's file system or not. If present, open the file and read its contents.
6.If the file is not found, send an HTTP 404 Not Found error message to the client.
7.Create an HTTP response message with the requested file preceded by header lines, and send it to the client using the send() method of the connection socket object.
8.Close the connection socket and go back to listening for incoming client connections.
Task2:
Implement a Web Client:

1.Import the socket module and create a client socket object with AF_INET and SOCK_STREAM parameters.
2.Set the server IP address, port number, and the file path to request from the server as command-line arguments.
3.Connect to the server using the connect() method of the client socket object.
4.Send an HTTP GET request to the server for the requested file using the sendall() method of the client socket object.
5.Receive the HTTP response message from the server using the recv() method of the client socket object.
6.Print the HTTP response message on the console.

Task 3: Making a multi-threaded web server
to implement a multithreaded server that is capable of serving multiple requests simultaneously. Using threading, first i created a main thread in which my modified server listens for clients at a fixed port. When it receives a TCP connection request from a client, it will set up the TCP connection through another port and services the client request in a separate thread. There will be a separate TCP connection in a separate thread for each request/response pair.
