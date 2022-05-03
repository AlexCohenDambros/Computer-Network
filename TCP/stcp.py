#!/usr/bin/env python3

import socket
import sys
import time

#-------------------------------------------------------------------------------
def trataCliente(conn, addr):
    while True:
        try:
            input('digite <ENTER> para continuar')
            data = conn.recv(1024)
            if not data: break
            print(f'{addr}={data}')
        except:
            print('algo horrível aconteceu!!!')
            break

    print(f'o loop do cliente {addr} foi encerrado!')
    conn.close()  

def trataCliente2(conn, addr):
    try:
        data = conn.recv(1024)
        print(f'{addr}={data}')
    except:
        pass 

#-------------------------------------------------------------------------------    

HOST = '127.0.0.1'  # localhost = esta máquina
PORT = 9999           # portas abaixo de 1023 exigem permissão de root

porta = int(input('entre com a porta do servidor: '))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((HOST, porta))
except:
   print('# erro de bind')
   sys.exit()

s.listen(5) # listen ele guarda as conexões, 5 é o número máximo. 

s.setblocking(0) #trabalhar com bloqueio ou sem bloqueio
conns = {} #dicionario que vai armazenar a conexão e o endereço.

while True: # pode ter mais de um cliente (Não sabe o numero de pacotes que pode chegar)

    print('aguardando conexoes em ', porta)
    try:
        conn, addr = s.accept() # coloca o servidor para dormir, quando receber um request acorda o servidor. Conn, numero de conexões.
        conns[conn] = addr
        print('recebi uma conexao de ', addr)
    except:
        pass

    #--------------------------
    # insira aqui o codigo para tratar uma conexao
    #--------------------------

    #trataCliente(conn, addr)

    for k,v in conns.items(): #realiza um varredura a cada 5 segundos para verificar as conexões com clientes. 
        trataCliente2(k,v)
    time.sleep(5)


print('o servidor encerrou')



