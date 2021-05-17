#!/usr/bin/python3


import socket


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    print("Client socket : ", client_socket)
    print("Enter : 'bye' to exit")
    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message with encode()
          # receive response with decode()
        data = client_socket.recv(1024).decode()
        print('Received from server: ' + data)  # show in terminal
        message = input(" -> ")  # again take input
    client_socket.close()  # close the connection

if __name__ == '__main__':
    client_program()
