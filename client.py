import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    # Send data
    while True:
        print('Digite sua mensagem')
        message = raw_input('>>')
        print('sending {!r}'.format(message))
        sock.sendall(message)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        full_message = ""

        while amount_received < amount_expected:
            data = sock.recv(16)
            full_message = full_message + data
            amount_received += len(data)
        print('received {!r}'.format(full_message))

finally:
    print('closing socket')
    sock.close()
