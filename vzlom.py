import time
import random 
import colorama

from colorama import init
init()

from colorama import Fore, Back, Style
print (Fore.GREEN)
start_time= time.time()
print ('короч это прога для взлома почты')
print ()

w = input ('введи почту: ')

countl = 0
countn = 0
counto = 0
spase = 0
for i in w:
    if i.isalpha():
        countl += 1
    elif i.isdigit():
        countn += 1
    elif i.isspace():
        spase += 1

    else:
        counto += 1
if counto >=2 and spase == 0:
    b = 10000000
    l= 100000000000000000000000000000000000000000000000
    while b >=1:

        g = (random.randint(1, l))
        print (g)
        b -=1



    def fun():
        a=2
        b=3
        c=a+b
    end_time= time.time()
    fun()
    timetaken = end_time - start_time
    b = timetaken * 1000 / 1000
    n = 4
    g = round(b, n)

    print("Программа работала: " + str(g) + ' секунд') # 0.0345

else:
    print ('введи почту нормальную уёбище блять')