#!/usr/bin/env python3

import socket
import sys

#cliente precisa saber o host e a porta do servidor.

HOST = '127.0.0.1'    # localhost = esta máquina
PORT = 9999           # portas abaixo de 1023 exigem permissão de root

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
   print('# erro de conexão')
   sys.exit()

#--------------------------
# insira aqui o codigo para tratar uma conexao
#--------------------------

#// s: objeto socket criado anteriormente

print('digite o texto a ser transmitido:')

while True:
    try:
        line = input()
        if not line:
            print('linha vazia encerra o programa')
            break
    except:
            print('programa abortado com CTRL+C')
            break

    data = bytes(line, 'utf-8') #converte string para bytes
    tam = s.send(data)
           
    print('enviei ', tam, 'bytes')
    print(data)