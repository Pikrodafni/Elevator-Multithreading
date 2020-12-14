import random
import threading
import time

f=[0,0,0,0,0]

def girenSayisi():
    insan = random.randint(1, 10)
    return insan

def hedefKat():
    kat = random.randint(1, 4)
    return kat

def prints(cikiskati,insan):
    liste = list()
    liste.append([insan,cikiskati])
    print("cikis yapan insansayisi,kat :",liste)
    return liste

def hedefKatcikis(f):
    cikisKati = list()
    for a in range(len(f)):
        if(f[a]>0):
            cikisKati.append(a)

    kat = random.choice(cikisKati)
    return kat

def cikanSayisicikis(f):
    cikiskati = hedefKatcikis(f)
    if (f[cikiskati] >= 5):
        insan = random.randint(1, 5)
    elif (f[cikiskati] < 5):
        insan = random.randint(1, f[cikiskati])
    f[cikiskati] -= insan
    prints(cikiskati, insan)
    cikisYapan = [insan, 0]
    return cikisYapan

def quekle():
    while True:
        kat = hedefKat()
        ins = girenSayisi()
        time.sleep(0.5)
        print("gireninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
        queue.enque([ins, kat])
        print("Queue : ",queue.item)

def qucikar(f):
        while True:
            if(f[1]>0 or f[2]>0 or f[3]>0 or f[4]>0):
                ins = cikanSayisicikis(f)
                time.sleep(1)
                print("kattan cikaninsan : %s time : %s" % (ins, time.ctime(time.time())))
                if (ins[1] == 1):
                    queue1.enque(ins)
                elif (ins[1] == 2):
                    queue2.enque(ins)
                elif (ins[1] == 3):
                    queue3.enque(ins)
                elif (ins[1] == 4):
                    queue4.enque(ins)
                print(f)


def asansorBinis(queue, asansio1):
    countinsid = countinside(asansio1)
    while(countinsid<10):
        countinsid = countinside(asansio1)
        if (bool(queue.item)==True and countinsid<10):
            futureinside = countinsid + queue.item[0][0]
            binecek = 10-countinsid
            if (futureinside <= 10):
                asansio1.customer.append(queue.item[0])
                queue.item.pop(0)
            elif (futureinside > 10):
                queue.item[0][0] -= binecek
                asansio1.customer.append([binecek, queue.item[0][1]])
    print("asansördekiler : ",asansio1.customer)

def asansorInis(asansio1, f):
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
    print("f.kat : %s All : %s" % (f,f[asansio1.floor]))

def hedef(asansio):

    if(bool(asansio.customer) == True):
        temp = list()
        for a in range(len(asansio.customer)):
            temp.append(asansio.customer[a][1])
        print(min(temp))
        asansio.destination = min(temp)
    elif (bool(asansio.customer) == False):
        destinationLength = 5
        if (bool(queue.item) == True):
            destinationLength = abs(asansio.floor)
            asansio.destination = 0
        if (bool(queue1.item) == True and destinationLength > abs(asansio.floor - 1)):
            destinationLength = abs(asansio.floor - 1)
            asansio.destination = 1
        if (bool(queue2.item) == True and destinationLength > abs(asansio.floor - 2)):
            destinationLength = abs(asansio.floor - 2)
            asansio.destination = 2
        if (bool(queue3.item) == True and destinationLength > abs(asansio.floor - 3)):
            destinationLength = abs(asansio.floor - 3)
            asansio.destination = 3
        if (bool(queue4.item) == True and destinationLength > abs(asansio.floor - 4)):
            destinationLength = abs(asansio.floor - 4)
            asansio.destination = 4

    if (asansio.destination < asansio.floor):
        asansio.direction = "down"
    else:
        asansio.direction = "up"
    while (asansio.floor != asansio.destination):
        time.sleep(0.2)
        if(asansio.direction == "up"):
            asansio.floor += 1
        elif(asansio.direction == "down"):
            if(bool(asansio.customer) == True):
                if (asansio.customer[0][1] == 0):
                    if (bool(queue1.item)==True and asansio.floor == 1):
                        break
                    if (bool(queue2.item)==True and asansio.floor == 2):
                        break
                    if (bool(queue3.item)==True and asansio.floor == 3):
                        break
                    if (bool(queue4.item)==True and asansio.floor == 4):
                        break

            asansio.floor -= 1

        print("floor : %d asansördekiler : %s time : %s" % (asansio.floor, asansio.customer, time.ctime(time.time())))

def countinside(asansio):
    totalinside=0
    for i in range(len(asansio.customer)):
        totalinside += asansio.customer[i][0]
    return totalinside

def asansor(asansio, devam, devam1, f):
    while (devam == True and devam1 != True ):
        isEmpty = True
        if (asansio.floor == 0 and bool(queue.item) == True):
            asansorBinis(queue, asansio)
        if (asansio.floor == 1 and bool(queue1.item) == True):
            asansorBinis(queue1, asansio)
        if (asansio.floor == 2 and bool(queue2.item) == True):
            asansorBinis(queue2, asansio)
        if (asansio.floor == 3 and bool(queue3.item) == True):
            asansorBinis(queue3, asansio)
        if (asansio.floor == 4 and bool(queue4.item) == True):
            asansorBinis(queue4, asansio)
        if (bool(asansio.customer) == True):
            isEmpty = False
        while (isEmpty == False):
            hedef(asansio)
            asansorInis(asansio, f)
            if not asansio.customer:
                isEmpty = True
        hedef(asansio)


    while(devam1 == True):
        isEmpty = True
        if (asansio.floor == 0 and bool(queue.item) == True):
            asansorBinis(queue, asansio)
        if (asansio.floor == 1 and bool(queue1.item) == True):
            asansorBinis(queue1, asansio)
        if (asansio.floor == 2 and bool(queue2.item) == True):
            asansorBinis(queue2, asansio)
        if (asansio.floor == 3 and bool(queue3.item) == True):
            asansorBinis(queue3, asansio)
        if (asansio.floor == 4 and bool(queue4.item) == True):
            asansorBinis(queue4, asansio)
        if (bool(asansio.customer) == True):
            isEmpty = False
        while (isEmpty == False):
            hedef(asansio)
            asansorInis(asansio, f)
            if not asansio.customer:
                isEmpty = True

        hedef(asansio)
        bekleyen = kuyruk()
        if (bekleyen <= 20 and bool(asansio2.customer) == False):
            devam1 = False

        if (bekleyen <= 30 and bool(asansio3.customer) == False):
            devam1 = False

        elif (bekleyen <= 40 and bool(asansio4.customer) == False):
            devam1 = False

        elif (bekleyen < 50 and bool(asansio5.customer) == False):
            devam1 = False


def kuyruk():
    toplamKuyruktakiler = 0
    qcopy = queue.item.copy()
    qcopy1 = queue1.item.copy()
    qcopy2 = queue2.item.copy()
    qcopy3 = queue3.item.copy()
    qcopy4 = queue4.item.copy()

    while (bool(qcopy)==True):
        toplamKuyruktakiler += qcopy[0][0]
        qcopy.pop(0)


    while (bool(qcopy1)==True):
        toplamKuyruktakiler += qcopy1[0][0]
        qcopy1.pop(0)

    while (bool(qcopy2)==True):
        toplamKuyruktakiler += qcopy2[0][0]
        qcopy2.pop(0)

    while (bool(qcopy3)==True):
        toplamKuyruktakiler += qcopy3[0][0]
        qcopy3.pop(0)

    while (bool(qcopy4)==True):
        toplamKuyruktakiler += qcopy4[0][0]
        qcopy4.pop(0)

    return toplamKuyruktakiler

def kontrol(f):
    var = 1
    deva = False
    while(var == 1):
        print("KONTRA")
        bekleyen = kuyruk()
        if (bekleyen > 20):
            devam2 = True
            if(devam2==True):
                print("Asansör2 Çalışıyor!!!")

            asansor(asansio2, deva, devam2, f)

        if (bekleyen > 30):
            devam3 = True
            if (devam3 == True):
                print("Asansör3 Çalışıyor!!!")

            asansor(asansio3, deva, devam3, f)

        if (bekleyen > 40):
            devam4 = True
            if (devam4 == True):
                print("Asansör4 Çalışıyor!!!")

            asansor(asansio4, deva, devam4, f)

        if (bekleyen > 50):
            devam5 = True
            if (devam5 == True):
                print("Asansör5 Çalışıyor!!!")

            asansor(asansio5, deva, devam5, f)



class Asansor(object):
    def __init__(self, name):
        self.name = name
        self.customer = []
        self.mode = "idle"
        self.floor = 0
        self.destination = 0
        self.direction = "up"
        self.capacity = 10
        self.count_inside = 0
        self.inside = []
        self.active = "Active"

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

queue = Queue()
queue1 = Queue()
queue2 = Queue()
queue3 = Queue()
queue4 = Queue()
asansio1 = Asansor("birinci asansör")
asansio2 = Asansor("ikinci asansör")
asansio3 = Asansor("ikinci asansör")
asansio4 = Asansor("ikinci asansör")
asansio5 = Asansor("ikinci asansör")
dev1 = False
dev = True

try:
    threadgiris = threading.Thread(target=quekle, args=())
except:
    print("Error: unable to start thread")

try:
    threadcikis = threading.Thread(target=qucikar, args=(f,))
except:
    print("Error: unable to start thread")

try:
    threadAsansor = threading.Thread(target=asansor, args=(asansio1, dev, dev1, f,))
except:
    print("Error: unable to start thread")

try:
    threadKontrol = threading.Thread(target=kontrol, args=(f,))
except:
    print("Error: unable to start thread")


threadgiris.start()
threadAsansor.start()
threadcikis.start()
threadKontrol.start()
