import socket
import threading

# Handle client connections
def handle_client(conn, addr):
    print(f'Connected by {addr[0]}:{addr[1]}')
    while True:
        data = conn.recv(1024)
        if not data:
            print(f'Connection closed by {addr[0]}:{addr[1]}')
            break
        print(f'Received from {addr}: {data.decode()}')
        response = input('Enter response to send: ')
        conn.sendall(response.encode())
    conn.close()

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

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen()
print(f'Server listening on {server_ip}:{server_port}')

# Accept connections
while True:
    conn, addr = server_socket.accept()
    client_thread = threading.Thread(target=handle_client, args=(conn, addr))
    client_thread.start()
