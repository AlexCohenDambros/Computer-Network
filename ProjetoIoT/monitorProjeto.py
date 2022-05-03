#!/usr/bin/env python3
import socket
import sys
import threading

#--------------------------------------------------------------
# FUNÇÕES

def TrataSensor(conn):
    while True:
        try:
            data = conn.recv(1000)
            if not data:
                print("O SENSOR ENCERROU COM FINISH")
                conn.close()
                break
            else:
                print('recebi ', len(data), ' bytes')
                print(data)
        except:
            print("O SENDOR ENCERROU COM RESET")
            break

    conn.close()    
    print('O cliente', conn, 'encerrou')

#--------------------------------------------------------------
# PROGRAMA PRINCIPAL

HOST = ''               # ANY_IP = todos os IPs do HOST
SENSORES={}     # lista de sensores conectados
CONSOLE=None  # conexao com o console remoto

PORTA = 9999
# int(input('Entre com a porta do servidor: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, PORTA))
except:
   print('# erro de bind')
   sys.exit()

s.listen(2) #backlog = 3

print('aguardando conexoes em ', PORTA) 

#--------------------------------------------------------------
# LOOP para tratar clientes

while True: 
    conn, addr = s.accept()
    print('recebi uma conexao de ', addr)
    #TrataSensor(conn) 
    t = threading.Thread( target=TrataSensor, args=(conn,))
    t.start()
    
    #print('o cliente encerrou')
    #conn.close()
#--------------------------------------------------------------

print('o servidor encerrou')
s.close()