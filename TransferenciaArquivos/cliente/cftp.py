import socket
import sys
import time
import os

HOST = '127.0.0.1'          # IP do servidor
PORT = 9999                 #Porta do servidor
diretorio = 'TOPSECRET'

# Coloque a função de Upload aqui

#--------------------------------------------------------------------
# Incio do código principal

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((HOST, PORT))
except:
    print('# erro de conexao')
    sys.exit()

# Verifica se o diretório já foi criado (resposta deve conter a lista de diretórios)

# PASSO1: Substitua COMANDO pelo comando de listar diretórios
s.send(bytes('os.listdir()\n', 'utf-8'))
time.sleep(2) #essa espera é para receber a resposta completa sem ter que criarum while
resposta = s.recv(2048).decode()

# Se não estiver, cria o diretório
if diretorio not in resposta:
    print('Diretorio nao encontrado')

# PASSO2: Substitua COMANDO pelo comando de criar diretório
    s.send(bytes('os.makedirs({})\n'.format(diretorio),'utf-8'))
    time.sleep(2)
    print(s.recv(2048).decode())
else:
    print('Conteudo do diretorio:')
    
    # INCLUA O CÓDIGO PARA MOSTRAR OS ARQUIVOS NA PASTA 
    # talvez você deva usar eval() ...
    s.send(bytes('os.listdir({})\n'.format(diretorio), 'utf-8'))
    time.sleep(2)
    resposta = s.recv(2048).decode()
    print(resposta)

# PASSO3: Inclua o código para verificar se o arquivo existe
arquivo = input('Digite o nome do arquivo para transferir: ')
if not arquivo:
    print('<ENTER> encerra o programa')
    sys.exit()

#---------------------------------------------------------------------------------------------
# PASSO4: Inclua o código de UPLOAD AQUI 