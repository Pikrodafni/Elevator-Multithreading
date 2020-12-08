import random
import threading
import time
from collections import deque


exitFlag = 0
global counter
global queue
global asansio1

def girenSayisi():
   insan = random.randint(1, 10)

   return insan

def cikanSayisi():
   insan = random.randint(1, 5)

   return insan

def hedefKat():
   kat = random.randint(1,4)
   return kat

def quekle(counter):
   while counter:
      kat = hedefKat()
      ins = girenSayisi()
      time.sleep(0.5)
      print("gireninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
      queue.enque([ins, kat])
      counter -=1

def qucikar(counter):
   while counter:
      kat = hedefKat()
      ins = cikanSayisi()
      time.sleep(1)
      print("cikaninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
      queue2.enque([ins, kat])
      counter -=1

def asansör():
   tmp = queue.deque()
   binecek = 0
   for i in range(0,tmp):
      print("evveti",i)
      asansio1.customer.append(queue.item[i])
      print("customa",asansio1.customer)
      binecek += asansio1.customer[i][0]
      print("aha:",binecek)

   if(binecek < 10):
      queue.item[tmp][0] -= (10 - binecek)
      asansio1.customer.append([(10 - binecek),queue.item[tmp][1]])
      print(asansio1.customer)

   for i in range(0,tmp):
      queue.item.pop(0)


class Asansor (object):
   def __init__(self):
      self.customer = []
      self.mode = "working"
      self.floor = 0
      self.destination = 2
      self.direction = "up"
      self.capacity = 10
      self.count_inside = 0
      self.inside = []
      self.active = "Active"

class Kat(object):

   def __init__(self):
      self.customer = []

   def __repr__(self):
      return "{}".format(self.customer)

   def __str__(self):
      return "{}".format(self.customer)

   def enque(self, add):
      self.customer.append(add)
      return True

   def size(self):
      return len(self.customer)

   def isempty(self):
      if self.size() == 0:
         return True
      else:
         return False

   def deque(self):
      if self.size() == 0:
         return None
      else:
         return self.customer.pop(0)


class Queue(object):

   def __init__(self):
      self.item = []

   def __repr__(self):
      return "{}".format(self.item)

   def __str__(self):
      return "{}".format(self.item)

   def enque(self, add):
      self.item.append(add)
      return True

   def size(self):
      return len(self.item)

   def isempty(self):
      if self.size() == 0:
         return True
      else:
         return False

   def deque(self):
      binecek = 0
      i = 0
      temp = 0
      if self.size() == 0:
         return None
      else:
         for i in range(len(self.item)):
            if ((binecek + temp) > 10):
               break
            binecek += self.item[i][0]
            i += 1
            temp = self.item[i][0]

         return i


queue = Queue()
queue2 = Queue()
asansio1 = Asansor()
counter = 5

try:
   threadgiris = threading.Thread(target=quekle, args=(counter, ))
except:
   print("Error: unable to start thread")

try:
   threadcikis = threading.Thread(target=qucikar, args=(counter,))
except:
   print("Error: unable to start thread")

threadgiris.start()
threadcikis.start()
print("somecode")

threadgiris.join()
print(queue.deque())


asansör()