import socket

host = socket.gethostname()
hostIP = socket.gethostbyname(host)

print(host)
print(hostIP)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, 80))     # need sudo for privileged ports (0 ~ 1023)
server.listen(5)
print("Server is listening at port 80. ")
