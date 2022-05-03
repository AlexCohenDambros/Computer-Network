#Criando um servidor
import socket
import sys

from cv2 import add

HOST = "127.0.0.1" # Localhost = esta máquina
PORT = 9999 # porta abaixo de 1023 exigem permissão de host

# Forçando o erro de BIND()
#PORT = int(input("Escolha uma porta: "))

#Strem = TCP
#AF_INET = ipv4
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((HOST, PORT))
    
except:
    print("# error de bind")
    sys.exit()

s.listen(5)

print("Aguardando conexões em:  ", PORT)

# ==============================
# Insira aqui o código para tratar uma conexão
# ==============================

while True:
    conn, addr = s.accept()
    print("Recebi uma conexão de: ", addr)

    # Recepção ao cliente. (Conversar com o cliente)
    while True:
        data = conn.recv(1024) # ler no máximo 1024 bytes
        print('recebi ', len(data), ' bytes')
 
        if not data: # Encerra a chamada
            break
        print(data)


print("O cliente encerrou")
conn.close()
