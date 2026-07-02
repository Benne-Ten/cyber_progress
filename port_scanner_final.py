import socket
import argparse

def test_port(lst_host :list, lst_port :list):
        for host in lst_host:
		port_fermer = 0
                for ip in lst_port:
                        try:
                                ip = int(ip)
                                #gere la partie connection
                                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock.settimeout(1)
                                sock.connect((host, ip))

                                #gere l'envoie de packet
                                sock.send(b"GET / HTTP/1.1\r\nHost: {host}\r\n\r\n").encode()

                                #gere la partie reponse
                                response = sock.recv(4096)
                                sock.close()
                                print(f"le port {ip} est ouvert")
                        except socket.timeout:
				print(f"le port {ip} n'est pas atteignable : timeout")
				port_fermer +=1

			except:
                                port_fermer += 1
		print(f"{len(lst_port)-port_fermer} sur {len(lst_port)}")


parser_port = argparse.ArgumentParser()
parser_port.add_argument("--host")
parser_port.add_argument("--port")
args = parser_port.parse_args()
lst_port = args.port.split(",")
lst_host = args.host.split(",")

test_port(lst_host, lst_port)
