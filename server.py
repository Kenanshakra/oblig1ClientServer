from socket import *
import sys



def main():
    # Serverens IP-adresse og port
    port = 12000
    server_ip = '127.0.0.1'

    # Opprett en socket
    server_socket = socket(AF_INET, SOCK_STREAM)

    # Bind socket til IP-adresse og port
    try:
        server_socket.bind((server_ip, port))
    except:
        print("feil pinding")

    # Lytte på inngående forbindelser
    server_socket.listen(10)

    print(f'Server kjører på {server_ip}:{port}')

    while True:
        # Godta en inngående forbindelse
        client_socket, addr = server_socket.accept()
        print(f'Forbindelse fra {addr}')

        # Motta HTTP-forespørsel
        request = client_socket.recv(1024).decode()
        print(f'Mottatt følgende HTTP-forespørsel: \n{request}')
        # send data back over the connection
        client_socket.send(request.encode())
        # Del opp HTTP-forespørsel for å hente filnavn
        file_name = request.split()[1]
        # Åpne filen på serverens filsystem
        try:
            with open('oblig1'+file_name):
                response = file_name.read()
            # Send HTTP-respons tilbake til klienten
            client_socket.send(response)
            for i in range(0, len(file_name)):
                 client_socket.send(file_name[i].encode())
            client_socket.send("\r\n".encode())
            client_socket.close()

        # Send HTTP "404 Not Found" tilbake til klienten
        except FileNotFoundError:
            response = "HTTP/1.1 404 Not Found\n\n<html><body><h1>404 Not Found</h1></body></html>"
            client_socket.sendall(response.encode())
            client_socket.close()
            sys.exit()

        server_socket.close()



if __name__ == '__main__':
    main()