#!/usr/bin/env python3

from multiprocessing import Process, Value, Lock
import time
import random
import os

EXE = 1

# REGISTRA O LANÇAMENTO DA THREAD EM UM LOG
def writelog(n):
    f = open('log.txt','a')
    f.write(f'thread {n}\n')
    f.close()

# REPRESENTA UM PROCESSO FILHO
def meuprocesso(n, count, lock):
    
    t = random.randint(1,3)
    time.sleep(t)

    if EXE == 4 and n == 5:
        os._exit(0) # Aborta o processo imediatamente

    lock.acquire()
    mycount = count.value
    writelog(n)
    print(f'Processo {n} lançada em {t}s')
    count.value = mycount + 1
    lock.release()

#--------------------------------------------------------------------------
# PROCESSO PAI

if __name__ == '__main__':

    count = Value('i',0)
    start = time.time()
    lock = Lock()

    open('log.txt','w').close()

    processes = [ ]
    for i in range(10):
        t = Process(target=meuprocesso, args=(i,count,lock))
        processes.append(t)
        t.start()

    for x in processes : x.join()

    print("Processos lançados! ", count.value)
    print('Tempo decorrido', time.time() - start )