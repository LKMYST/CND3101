import socket
import threading

# Receive messages from server
def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                print('Connection closed')
                break

            print(f'Received from server: {data.decode()}')

        except OSError:
            print("Client closed")


# Get host ip
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # create a ipv4, UDP socket
    s.connect(("8.8.8.8", 80))      # fake connection to outer ip to get host ip
    ip = s.getsockname()[0]
    s.close()
    return ip


# Set server ip and port
server_ip = get_local_ip()
server_port = 12345
### For convenience, I copied get_local_ip() from mult_server.py
### So that I don't have to set server ip and port manually no matter where or when I run this practice


# Create client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

server_ip, server_port = client_socket.getpeername()    # show server info
print(f'Connected to server at {server_ip}:{server_port}')


# Start thread to receive messages
receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()


# Send messages to server
while True:
    message = input('Enter message to send: ')
    if message.lower() == 'exit':
        print("Closing connection...")
        client_socket.shutdown(socket.SHUT_RDWR)
        client_socket.close()
        break
    client_socket.sendall(message.encode())
