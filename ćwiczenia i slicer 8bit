# import string
# import random
#
#
#
# def func1(x):
#     b = dict(zip(list(i for i in range(0,100)), list(string.ascii_letters + string.digits + string.punctuation)))
#     c = list(random.randint(0,len(b)-1) for i in range(0,int(x)))
#     g = list(b.get(i) for i in c)
#     z = str(''.join(h for h in g))
#     return z
#
#
# def func2():
#     b = open('texter.txt', 'a')
#     gg = int(input('Jak długie ma być hasło'))
#     gg2 = int(input('Ile ma być haseł'))
#     for i in range(0,gg2):
#         b.write(f"{func1(gg)}\n")
#
# # func2()
#
#
#
#
#
#
#
#
#
#
#
# import datetime
#
# def func3():
#     print(f"Masz {datetime.date.today().year-int(input('Kiedy się urodziłeś?'))} lat")
#
#
#
# func3()
#
#


'''
Napisz mi funkcje która wymieni elementy z listy zewnętrznej

'''

# x = [645,321,654,879,645,465,132,132,3,1,18,1,9,15,1,51,1,32,2,6,3,4,98,7,97,9,8,7,7,98,4,654,32,1,23,13,1,6,6,4]
#
# def func1(x):
#     for i in range(0,len(x)-1):
#         print(f"{i+1}st element: {x[i]}")
# #
# # func1(x)
import random
import string

'''
Napisz funkcje która stworzy mi losową listę znaków np. na 1000 elementów
'''

def func1(n):
    return list(random.randint(0,1) for i in range(0,n))



'''
Napisz funkcje która sprawdzi czy dana złożoność 8bit jest prawidłowa
'''

lista_wjazd = func1(random.randint(80,8000))


def func2(n):
    if len(n) % 8 == 0:
        return True
    else:
        return False
'''
napiszemy funkcje która kolejne 8 elementów z listy skomasuje do stringu i doda do osobnej listy jeżeli func powyżej zwróci True
'''

def func3(n):
    g = []
    if func2(lista_wjazd) == True:
        indeks = len(lista_wjazd) / 8
        for i in range(0,int(indeks)):
            z = ''.join(str(i) for i in lista_wjazd[0:7])
            g.append(z)
            del lista_wjazd[0:7]
        print(g)
    else:
        pass
func3(lista_wjazd)
