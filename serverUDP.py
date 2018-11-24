import socket

def server(p):
    host = 'localhost'      # or '127.0.0.1'
    port = p                # make port equal to received parameter

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a UDP socket

    s.bind((host, port))    # bind created socket to host and port number
    print("The server is on")

    while True:
        command, addr = s.recvfrom(1024)   # receive a command and address
        command = command.decode('utf-8')  # decrypt it and save it
        data, address = s.recvfrom(2048)   # receive a message and address
        data = data.decode('utf-8')        # decode it with 'utf-8'
        if command == "upper":
            data = data.upper()
        elif command == "reverse":
            data = rev(data)
        elif command == "lower":
            data = data.lower()
        print("Sending..."+data)
        s.sendto(data.encode('utf-8'), address)  # encrypt it and send it back
    s.close()


def rev(data):                                   # Reverse a string and return reversed result
    s = list(data)
    r = ""
    i=(int(len(s))-1)
    while i >= 0:
        r = r+(s[i])
        i -= 1
    return r


def fun():
    port = input("Enter a port number: ")        # set up a user input
    if port == "":  # pass a default function
        server(9999)
    else:
        server(int(port))                        # pass the user input
fun()
