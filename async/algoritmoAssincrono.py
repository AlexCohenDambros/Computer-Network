import asyncio
import time
import random
import os

EXE = 1

# REPRESENTA UMA TAREFA COOPERATIVA (COROUTINES)
async def minhatarefa(n):
    global count

    #while True:
    print(f'Tarefa {n} começou') 
    t = random.randint(1,3)
    await asyncio.sleep(t)
    #time.sleep(t)
    if EXE == 4 and n == 5:
        print("A CORRENTINHA 5 EXPLODIU")
        os._exit(0) # Aborta o processo imediatamente
    count += 1
    print(f'Tarefa {n} terminou')  
        

# LANCA AS TAREFAS
async def main():

    tarefas = []
    for i in range(10) : 
        t = asyncio.create_task( minhatarefa(i) )
        tarefas.append(t)
    
    # espera as tarefas concorrentes terminarem
    print('Tarefas lançadas ...')
    for t in tarefas : await t
    print('Pronto para continuar ...')


#--------------------------------------------------------------------------
# PROCESSO PAI

if __name__ == '__main__':

    count = 0
    start = time.time()

    asyncio.run(main())
        
    print("Tarefas lançadas! ", count)
    print('Tempo decorrido', time.time() - start )
    
    
# Excercício 1 

# sim elas compartilham variaveis


# Exercício 2 

# sim as tarefas podem abortar o processo

# Exercício 3 

# as tarefas serão executados em ordem, sequencial a thread bota o processo para dormir e nada fica em paralelo

# Exercício 4

# as taferas ficam em loop infinito, começando e encerrando as tarefas