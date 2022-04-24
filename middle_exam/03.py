import socket

ip = '220.69.189.125'
port = 443

print(socket.gethostbyaddr(ip)[0])

print(socket.getservbyport(port))

print(f"{socket.getservbyport(port)}://{socket.gethostbyaddr(ip)[0]}")

print(socket.inet_aton(ip))