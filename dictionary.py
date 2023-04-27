import string
import random


'''
GENERATOR HASEŁ
'''
def func1(x):
    b = dict(zip(list(i for i in range(0,100)), list(string.ascii_letters + string.digits + string.punctuation)))
    c = list(random.randint(0,len(b)-1) for i in range(0,int(x)))
    g = list(b.get(i) for i in c)
    z = str(''.join(h for h in g))
    return z


def func2():
    b = open('texter.txt', 'a')
    gg = int(input('Jak długie ma być hasło'))
    gg2 = int(input('Ile ma być haseł'))
    for i in range(0,gg2):
        b.write(f"{func1(gg)}\n")

func2()
