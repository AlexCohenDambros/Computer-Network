import socket
import sys
import time

from cv2 import add

porta = int(input('Entre com a porta do servidor: '))
ip = input("Entre com o IP do servidor: ")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    # ip 
    s.bind((ip, porta))
except:
   print('# erro de bind')
   sys.exit()

while True:
    input("\nDigite algo para continuar.")
    data, addr = s.recvfrom(1024)
    s.sendto("OK".encode(), addr)
    print('sensor ', addr, ' enviou:', data)

print('o servidor encerrou')
s.close()