import random
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
   def __init__(self, name, mode, floor, destination ,direction ,capacity ,count_inside ,inside ,active):
      threading.Thread.__init__(self)
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
      print_time(self.name, 5, 0.5)
      print("Exiting " + self.name)

def print_time(threadName, counter, delay):
   while counter:
      if exitFlag:
         threadName.exit()
      time.sleep(delay)
      print("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1


def girenSayisi():
   insan = random.randint(1, 10)
   return insan

def hedefKat():
   kat = random.randint(1,4)
   return kat


thread = myThread("asansör1","idle",0,0,"up",10,girenSayisi(),0,True)

thread.start()