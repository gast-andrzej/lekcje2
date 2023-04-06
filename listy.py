# # LISTA
#
# lista1 = []
#
# # TUPLA
#
# tupel = tuple()

import random
import string


def lista1():
    x = list(range(1,101))
    z = []
    for i in x:
        if i % 2 == 0:
            z.append(i)
        else:
            pass
    return z


def funcer():
    x = []
    for i in range(1,101):
        x.append(i)
    print(x)





def lista2():
    z = []
    indexer = 0
    while indexer < 5:
        bb = input('wprowadź słowo')
        z.append(bb)
        print(z)
        indexer += 1



def alpha():
    return list(string.ascii_letters + string.digits + string.punctuation)


def func1(n):
    z = alpha()
    bb = []
    for i in range(0,n):
        bb.append(z[random.randint(0,len(z)-1)])
    passwd = ''.join(i for i in bb)
    # return print(''.join(i for i in bb))
    return passwd

def tranzition():
    passwd = func1(50)
    b = open('texter.txt', 'a')

    # 'r' -> read (do odczytu),
    # 'w' - write (zapis z usunięciem stanu poprzedniego),
    # 'a' - append (zapis z zachowaniem stanu poprzedniego)
    b.write(f"\n{passwd}")

tranzition()



# func1(128)
# func1(32)




def listex1():
    print(list(range(0,1001)))

# listex1()




listaaaa1 = list(range(0,100))

listaa2 = ["Zbigniew","Ala", "Tomek", "Bartek"]

listaa3 = [33,22,44,55,11,77]

# append -> dodawanie do listy   listaaaa1.append(el. do appendu)

# usuwanie elementu listaaaa1.remove()



# usunięcie ostatniego elementu z listy listaaaa1.pop()

# obrócenie listy listaaaa1.reverse()

# sort alfabetyczny i liczbowy listaa2.sort()

# sort liczbowy listaa3.sort()

# listaa3.sort()
# listaa3.reverse()

# print(listaa3[::-1])

# służy do poszukiwania elementu w liście listaa3.count(22)

print()
