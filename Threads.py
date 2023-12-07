#number 1
from threading import Thread

def temp1():
  for x in range(1):
    print("processo1", x)
    x = 1

#inicializando essa funcao a partir de um objeto thread t1
t1 = Thread(target=temp1,args=[1])

#consulta se o objeto thread criado esta ativo
t1 = threading.activeCount()

#consulta o nome da thread ativa atualmente
import threading
import time
threading.current_thread()

#consulta o identificador de thread do thread atual
threading.enumerate()

#consulta quantidade de thread ativa atulmente
threading.current_thread()

#retorna o numero de objeto thread ativos
threading.active_count()

#mostra todas as lista de threads ativas
threading.enumerate()

#number 2
from threading import Thread
import time
def proc1():
  for x in range(1,11):
    print ("processo 1", x)
    x +=1
    time.sleep(1)


def proc2():
  for x in range(1,11):
    print("processo 2", x)
    x +=1
    time.sleep(2)

t1 = Thread(target=proc1)
t1.start()

t2 = Thread(target=proc2)
t2.start()

t1 = threading.activeCount()
t2 = threading.activeCount()
