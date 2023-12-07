#number 1
import time
time.gmtime(0)

import time
time.strptime("30 nov 00", "%d %b %y")

import time
seconds = time.time()
print("Segundos desde a epoca:", seconds)
print('segunds')

import time
tempo = time.localtime()
print(tempo)

t = time.asctime(tempo)
print(t)

from datetime import date
date_now = date.today
print(date_now)

# number 2
import time
start_exec = time.time()
def ola():
  time.sleep(3)
  print("ola mundo!" * 5)

ola()
and_exec = time.time()
print("O tempo de execuçao total corresponde a: ", and_exec - start_exec)

#number 3
try:
  import time

  #marca o tempo inicial
  start_exec = time.perf_counter()
except TypeError:
  print("execute o codigo")
  for i in range(input(1000000)):

    pass

    def ola():
      time.sleep(3)
      print("ola mundo!" * 5)

      #marca o tempo final
      and_time = time.perf_count()

      #calcula o tempo decorrido
      elapsed_time = and_time - start_time
      print(f"tempo decorrido: {elapsed_time:.6f} segundos")

except SyntaxError:
        print("execute o codigo")

        ola()
        and_exec = time.time()
        print("O tempo de execuçao total corresponde a:", and_exec - start_exec)

#number 4
from datetime import date
date(1987, 10, 16).isocalendar()
date(1987, 10, 25).isocalendar()

#number 5
from datetime import timedelta
delta = timedelta(
    days=50,
    seconds=37,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
# apenas dias, segundos e microssegundos permanecem
)
delta

from datetime import timedelta
d = timedelta(microseconds=-1)
(d.days, d.seconds, d.microseconds)

#number 6
from datetime import datetime
date = datetime.strptime('april 20 2023', '%B %d %Y')
print(date)

#number 7
from datetime import date, timedelta

current_date = date.today()
print("CURRENT DAY :",current_date)
print("OLD Date :" ,current_date - timedelta(8))

#number 8
from datetime import timedelta
year = timedelta(days=365)
ten_years = 10 * year
ten_years
ten_years.days // 365

nine_years = ten_years - year
nine_years

three_years = nine_years // 10
three_years, three_years.days // 365

#number 9
import datetime

today = datetime.date.today()
print('today:', today)

yesterday = today - datetime.timedelta(days=1)
print('Yesterday: ', yesterday)

tomorrow = today + datetime.timedelta(days=1)
print('Tomorrow: ', tomorrow)

print('Time between tomorrow and yesterday: ', tomorrow - yesterday)
