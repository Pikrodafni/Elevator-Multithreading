import random
import threading
import time


exitFlag = 0
global asansio2, asansio3, asansio4, asansio5
global f


def girenSayisi():
    insan = random.randint(1, 10)
    return insan


def cikanSayisi():
    insan = random.randint(1, 5)
    return insan


def hedefKat():
    kat = random.randint(1, 4)
    return kat


def quekle(counter):
    while counter:
        kat = hedefKat()
        ins = girenSayisi()
        time.sleep(0.5)
        print("gireninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
        queue.enque([ins, kat])
        counter -= 1


def qucikar(counter):
    while counter:
        kat = hedefKat()
        ins = cikanSayisi()
        time.sleep(1)
        print("cikaninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
        queue2.enque([ins, kat])
        counter -= 1


def asansorBinis(queue, asansio1):
    tmp = queue.deque()
    binecek = 0
    for i in range(0, tmp):
        print("evveti", i)
        asansio1.customer.append(queue.item[i])
        print("customa", asansio1.customer)
        binecek += asansio1.customer[i][0]
        print("aha:", binecek)

    if (binecek < 10):
        queue.item[tmp][0] -= (10 - binecek)
        asansio1.customer.append([(10 - binecek), queue.item[tmp][1]])
        print(asansio1.customer)

    for i in range(0, tmp):
        queue.item.pop(0)


def asansorInis(asansio1, f):
    print("merhaba")
    hedef(asansio1)
    grupsayisi = len(asansio1.customer)
    a = 0
    copyitem = asansio1.customer.copy()
    if (asansio1.floor == asansio1.destination):
        while (a != grupsayisi):
            if (asansio1.customer[a][1] == asansio1.floor):
                f[asansio1.floor] += asansio1.customer[a][0]
                print(f[asansio1.floor])
                copyitem.remove(asansio1.customer[a])
            a += 1
    asansio1.customer = copyitem.copy()
    print("customerlar",asansio1.customer)

def hedef(asansio1):
    i = 0
    j = 1
    temp = list()
    for a in range(len(asansio1.customer)):
        temp.append(asansio1.customer[a][1])

    print(min(temp))
    asansio1.destination = min(temp)
    if (asansio1.destination < asansio1.floor):
        asansio1.direction = "down"
    else:
        asansio1.direction = "up"

    while (asansio1.floor != asansio1.destination):
        time.sleep(0.2)
        asansio1.floor += 1
        print("floor : %d time : %s" % (asansio1.floor, time.ctime(time.time())))

def asansor(asansio1):
    asansorBinis(queue, asansio1)
    hedef(asansio1)
    asansorInis(asansio1, f)

class Asansor(object):
    def __init__(self, name):
        self.name = name
        self.customer = []
        self.mode = "working"
        self.floor = 0
        self.destination = 0
        self.direction = "up"
        self.capacity = 10
        self.count_inside = 0
        self.inside = []
        self.active = "Active"

    def __repr__(self):
        return "{}".format(self.direction)

    def __str__(self):
        return "{}".format(self.direction)


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

f=[0,0,0,0,0]
queue = Queue()
queue2 = Queue()
asansio1 = Asansor("birinci asansör")
counter = 5

try:
    threadgiris = threading.Thread(target=quekle, args=(counter,))
except:
    print("Error: unable to start thread")

try:
    threadcikis = threading.Thread(target=qucikar, args=(counter,))
except:
    print("Error: unable to start thread")

try:
    threadAsansor = threading.Thread(target=asansor, args=(asansio1,))
except:
    print("Error: unable to start thread")

threadgiris.start()
threadcikis.start()
print("somecode")

threadcikis.join()
threadAsansor.start()
threadAsansor.join()