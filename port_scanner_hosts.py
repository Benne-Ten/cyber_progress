import socket
import argparse

def test_port(lst_host :list, lst_port :list):
	for host in lst_host:
	        for ip in lst_port:
        	        try:
                	        ip = int(ip)
                        	#gere la partie connection
                        	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        	sock.connect((host, ip))
                        	sock.settimeout(1)

                        	#gere l'envoie de packet
                        	sock.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

                        	#gere la partie reponse
                        	response = sock.recv(4096)
                        	sock.close()
                        	print(f"le port {ip} est ouvert")
                	except :
                        	print(f"le port {ip} est fermer")


parser_port = argparse.ArgumentParser()
parser_port.add_argument("--host")
parser_port.add_argument("--port")
args = parser_port.parse_args()
lst_port = args.port.split(",")
lst_host = args.host.split(",")

print(test_port(lst_host, lst_port))
