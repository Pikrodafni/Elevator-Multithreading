import random
import threading
import time
import tkinter as tk

root =tk.Tk()
canvas = tk.Canvas(root,width=1024,height=600)
frame = tk.Frame(root, bg='darkgray')
frame.place(relwidth=1.0,relheight=1.0)
framekuyruk = tk.Frame(root, bg='darkgray')
framekuyruk.place(relwidth=1, relheight=1)




f=[0,0,0,0,0]

def girenSayisi():
    insan = random.randint(1, 10)
    return insan

def hedefKat():
    kat = random.randint(1, 4)
    return kat

def prints(cikiskati,insan,):
    liste = list()
    liste.append([insan,cikiskati])
    #print("cikis yapan insansayisi,kat :",liste)
    cikantop.cikan+=insan
    return liste

def kuyruksay(kuyruk):

    kuyrukinsan = 0
    qcopy = kuyruk.item.copy()

    while (bool(qcopy)==True):
        kuyrukinsan += qcopy[0][0]
        qcopy.pop(0)
    return kuyrukinsan

def yazdir():
    print(0, ". floor   queue:", kuyruksay(queue))
    print(1, ". floor  all:", f[1], " queue:", kuyruksay(queue1))
    print(2, ". floor  all:", f[2], " queue:", kuyruksay(queue2))
    print(3, ". floor  all:", f[3], " queue:", kuyruksay(queue3))
    print(4, ". floor  all:", f[4], " queue:", kuyruksay(queue4))
    print("exitcount:",cikantop.cikan)
    yaz = 0, ". floor   queue:", kuyruksay(queue), "\n", 1, ". floor  all:", f[1], " queue:", kuyruksay(queue1), \
               "\n", 2, ". floor  all:", f[2], " queue:", kuyruksay(queue2), "\n", 3, ". floor  all:", f[3], \
               " queue:", kuyruksay(queue3), "\n", 4, ". floor  all:", f[4], " queue:", kuyruksay(queue4)
    label11.config(text=yaz)

    yaz1 = "ASANSÖR1", "\n", "aktiflik", asansio1.active, "\n", "mode", asansio1.mode, "\n","floor :", asansio1.floor,\
           "\n","destination :", asansio1.destination, "\n","capacity:", asansio1.capacity, "\n","countinside :", countinside(asansio1),\
           "\n","Customer:", asansio1.customer
    label12.config(text=yaz1)

    yaz2 = "ASANSÖR2", "\n", "aktiflik", asansio2.active, "\n", "mode", asansio2.mode, "\n","floor :", asansio2.floor,\
           "\n","destination :", asansio2.destination, "\n","capacity:", asansio2.capacity, "\n","countinside :", countinside(asansio2),\
           "\n","Customer:", asansio2.customer
    label13.config(text=yaz2)

    yaz3 = "ASANSÖR3", "\n", "aktiflik", asansio3.active, "\n", "mode", asansio3.mode, "\n","floor :", asansio3.floor,\
           "\n","destination :", asansio3.destination, "\n","capacity:", asansio3.capacity, "\n","countinside :", countinside(asansio3),\
           "\n","Customer:", asansio3.customer
    label14.config(text=yaz3)

    yaz4 = "ASANSÖR4", "\n", "aktiflik", asansio4.active, "\n", "mode", asansio4.mode, "\n","floor :", asansio4.floor,\
           "\n","destination :", asansio4.destination, "\n","capacity:", asansio4.capacity, "\n","countinside :", countinside(asansio4),\
           "\n","Customer:", asansio4.customer
    label15.config(text=yaz4)

    yaz5 = "ASANSÖR5", "\n", "aktiflik", asansio5.active, "\n", "mode:", asansio5.mode, "\n","floor :", asansio5.floor,\
           "\n","destination :", asansio5.destination, "\n","capacity:", asansio5.capacity, "\n","countinside :", countinside(asansio5),\
           "\n","Customer:", asansio5.customer
    label16.config(text=yaz5)


    asansoryazdir(asansio1)
    asansoryazdir(asansio2)
    print("Asansör3:")
    asansoryazdir(asansio3)
    print("Asansör4:")
    asansoryazdir(asansio4)
    print("Asansör5:")
    asansoryazdir(asansio5)
    kuyrukyazdir()

def asansoryazdir(asansor):
    print("aktiflik", asansor.active)
    print("mode", asansor.mode)
    print("floor", asansor.floor)
    print("destination", asansor.destination)
    print("capacity", asansor.capacity)
    print("count inside", countinside(asansor))
    print("inside:", asansor.customer)
    print("")
def kuyrukyazdir():
    print("0.floor",queue.item)
    print("1.floor", queue1.item)
    print("2.floor", queue2.item)
    print("3.floor", queue3.item)
    print("4.floor", queue4.item)
    kuyrukyaz = "0.floor", queue.item, "\n", "1.floor", queue1.item, "\n", "2.floor", queue2.item,\
                "\n", "3.floor", queue3.item,"\n","4.floor", queue4.item
    labelKuyruk.config(text=kuyrukyaz)


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

class topcikan(object):

    def __init__(self):
        self.cikan = 0

cikantop=topcikan()

def quekle():
    while True:
        kat = hedefKat()
        ins = girenSayisi()
        time.sleep(0.5)
        #print("gireninsan : %s kat :%s time : %s" % (ins, kat, time.ctime(time.time())))
        queue.enque([ins, kat])
        #print("Queue : ",queue.item)

def qucikar(f):
    yazdir()
    while True:
        if(f[1]>0 or f[2]>0 or f[3]>0 or f[4]>0):
            ins = cikanSayisicikis(f)
            time.sleep(1)
            if (ins[1] == 1):
                queue1.enque(ins)
            elif (ins[1] == 2):
                queue2.enque(ins)
            elif (ins[1] == 3):
                queue3.enque(ins)
            elif (ins[1] == 4):
                queue4.enque(ins)


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
    yazdir()
    #print("asansördekiler : ",asansio1.customer)

def asansorInis(asansio1, f):
    hedef(asansio1)
    grupsayisi = len(asansio1.customer)
    a = 0
    copyitem = asansio1.customer.copy()
    if (asansio1.floor == asansio1.destination):
        while (a != grupsayisi):
            if (asansio1.customer[a][1] == asansio1.floor):
                f[asansio1.floor] += asansio1.customer[a][0]
                copyitem.remove(asansio1.customer[a])
            a += 1
    asansio1.customer = copyitem.copy()
    yazdir()



def hedef(asansio):

    if(bool(asansio.customer) == True):
        temp = list()
        for a in range(len(asansio.customer)):
            temp.append(asansio.customer[a][1])
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
        yazdir()
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

        #print("floor : %d asansördekiler : %s time : %s" % (asansio.floor, asansio.customer, time.ctime(time.time())))

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
            asansio2.active = "False"
            asansio2.mode = "Idle"
            devam1 = False

        if (bekleyen <= 30 and bool(asansio3.customer) == False):
            asansio3.active = "False"
            asansio3.mode = "Idle"
            devam1 = False

        elif (bekleyen <= 40 and bool(asansio4.customer) == False):
            asansio4.active = "False"
            asansio4.mode = "Idle"
            devam1 = False

        elif (bekleyen < 50 and bool(asansio5.customer) == False):
            asansio5.active = "False"
            asansio5.mode = "Idle"
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
        bekleyen = kuyruk()
        if (bekleyen > 20):
            devam2 = True
            if(devam2==True):
                print("Asansör2 Çalışıyor!!!")
                asansio2.active="True"
                asansio2.mode="Working"

            asansor(asansio2, deva, devam2, f)

        if (bekleyen > 30):
            devam3 = True
            if (devam3 == True):
                print("Asansör3 Çalışıyor!!!")
                asansio3.active = "True"
                asansio3.mode = "Working"

            asansor(asansio3, deva, devam3, f)

        if (bekleyen > 40):
            devam4 = True
            if (devam4 == True):
                print("Asansör4 Çalışıyor!!!")
                asansio4.active = "True"
                asansio4.mode = "Working"

            asansor(asansio4, deva, devam4, f)

        if (bekleyen > 50):
            devam5 = True
            if (devam5 == True):
                print("Asansör5 Çalışıyor!!!")
                asansio5.active = "True"
                asansio5.mode = "Working"

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
        self.active = "False"



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
asansio1.active="True"
asansio1.mode="Working"

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

yazansor = 0, ". floor   queue:", kuyruksay(queue), "\n", 1, ". floor  all:", f[1], " queue:", kuyruksay(queue1), \
           "\n",2, ". floor  all:", f[2], " queue:", kuyruksay(queue2), "\n",3, ". floor  all:", f[3], \
           " queue:", kuyruksay(queue3), "\n",4, ". floor  all:", f[4], " queue:", kuyruksay(queue4)
label11 = tk.Label(root, text=yazansor, fg='white', bg='#192633')
label11.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)

yaz1 = "ASANSÖR1", "\n", "aktiflik", asansio1.active, "\n", "mode", asansio1.mode, "\n", asansio1.floor, "\n",\
       asansio1.destination, "\n", asansio1.capacity, "\n", countinside(asansio1), "\n", asansio1.customer
label12 = tk.Label(frame, text=yaz1, fg='white', bg='#192633')
label12.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)

yaz2 = "ASANSÖR2", "\n", "aktiflik", asansio2.active, "\n", "mode", asansio2.mode, "\n", asansio2.floor, "\n",\
       asansio2.destination, "\n", asansio2.capacity, "\n", countinside(asansio2), "\n", asansio2.customer
label13 = tk.Label(frame, text=yaz2, fg='white', bg='#192633')
label13.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)

yaz3 = "ASANSÖR3", "\n", "aktiflik", asansio3.active, "\n", "mode", asansio3.mode, "\n", asansio3.floor, "\n",\
       asansio3.destination, "\n", asansio3.capacity, "\n", countinside(asansio3), "\n", asansio3.customer
label14 = tk.Label(frame, text=yaz3, fg='white', bg='#192633')
label14.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)

yaz4 = "ASANSÖR4", "\n", "aktiflik", asansio4.active, "\n", "mode", asansio4.mode, "\n", asansio4.floor,\
        "\n", asansio4.destination, "\n", asansio4.capacity, "\n", countinside(asansio4), "\n", asansio4.customer
label15 = tk.Label(frame, text=yaz4, fg='white', bg='#192633')
label15.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)

yaz5 = "ASANSÖR5", "\n", "aktiflik", asansio5.active, "\n", "mode", asansio5.mode, "\n", asansio5.floor,\
        "\n", asansio5.destination, "\n", asansio5.capacity, "\n", countinside(asansio5), "\n", asansio5.customer
label16 = tk.Label(frame, text=yaz5, fg='white', bg='#192633')
label16.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)

kuyrukyaz = "0.floor", queue, "\n", "1.floor", queue1, "\n", "2.floor", queue2, \
            "\n", "3.floor", queue3, "4.floor", queue4

labelKuyruk = tk.Label(framekuyruk, text=kuyrukyaz, fg='white', bg='#192633')
labelKuyruk.place(relx=0.1, rely=0.2, relwidth=1, relheight=1)


threadgiris.start()
threadAsansor.start()
threadcikis.start()
threadKontrol.start()


label11.pack()
frame.pack()
label12.pack()
label13.pack()
label14.pack()
label15.pack()
label16.pack()
labelKuyruk.pack()
framekuyruk.pack()
canvas.pack()
root.mainloop()
