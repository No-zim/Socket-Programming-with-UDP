import socket

def client(address, p):        # should allow user to specify server address and port number
        host = '127.0.0.1'     # has a localhost number
        port = 5555            # port number for UDP client should be different from server
                               # because it's not TCP
        server = (address, p)  # Received parameters for the server

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket for the client

        s.bind((host, port))                                  # bind socket with host and port number

        message = input("Enter something: (expt: quit to quit) ")
        command = input("Your wish is my command: upper/lower/reverse-> ")
        
        while message != 'quit':
            s.sendto(command.encode('utf-8'), server)   # sent your command to the server
            s.sendto(message.encode('utf-8'), server)   # then send your message
            data, addr = s.recvfrom(2048)               # take data you received and address from which it was sent
            data =data.decode('utf-8')                  # decrypt the data
            print("Received back: ", data)              # print your decrypted data
            message = input("Enter something: (expt: quit to quit) ")
            command = input("Your wish is my command: upper/lower/reverse-> ")
        s.close()



def fun():
    address = input("Specify the server address (or don't [default is present]): ")
    port = int(input("Enter the server port number: "))
    if address == "":
        client('127.0.0.1', port)
    else:
        client(address, port)
fun()
