import socket


#gere la partie connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("google.com", 80))


#gere l'envoie de packet
sock.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#gere la partie reponse
response = sock.recv(4096)
print(response.decode())
sock.close()
