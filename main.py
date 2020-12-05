import random
import threading
import time

exitFlag = 0
global counter
global queue

class kat (object):
   def __init__(self, name, mode, floor, destination ,direction ,capacity ,count_inside ,inside ,active):
      self.name = name
      self.mode = mode
      self.floor = floor
      self.destination = destination
      self.direction = direction
      self.capacity = capacity
      self.count_inside = count_inside
      self.inside = inside
      self.active = active

   def run(self):
      print("Starting " + self.name)
      counter=5
      while counter:
         if exitFlag:
            self.name.exit()
         time.sleep(0.5)
         print("%s: %s" % (self.name, time.ctime(time.time())))
         counter -= 1

      print("Exiting " + self.name)


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
      if self.size() == 0:
         return None
      else:
         return self.item.pop()

def girenSayisi():
   insan = random.randint(1, 10)

   return insan

def hedefKat():
   kat = random.randint(1,4)
   return kat

def quekle(counter):
   while counter:
      kat = hedefKat()
      ins = girenSayisi()
      time.sleep(0.5)
      print("insan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
      queue.enque([ins, kat])
      counter -=1


queue = Queue()
counter = 5

   #   kat("asansör1","idle",0,0,"up",10,girenSayisi(),0,True)

try:
   thread = threading.Thread(target=quekle, args=(counter, ))
except:
   print("Error: unable to start thread")

thread.start()

print("somecode")

thread.join()
response = queue
print(queue.item[0][1])


