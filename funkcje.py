'''
Funkcje to najbardziej podstawowe narzędzia programistyczne w Pythonie

'''
# def func1():
#     x = 5
#     y = 7
#     return print(x+y)
#
# def func1(x,y):
#     print(x+y)

# def func1():
#     while True:
#         x = input("Wprowadź liczbę ")
#         if x.upper() == "EXIT":
#             break
#         else:
#             try:
#                 int(x)
#                 z = input("Wprowadź liczbę ")
#                 try:
#                     int(z)
#                     print(int(x)%int(z))
#                     print(int(x)**int(z))
#                     print(int(x)*int(z))
#                     print(int(x)/int(z))
#                     print(int(x)+int(z))
#                     print(int(x)-int(z))
#                 except:
#                     print("Wiadomość o błędzie, wartość musi być liczbowa")
#             except:
#                 print("Wiadomość o błędzie, wartość musi być liczbowa")
#
# func1()



def func1():
    x = int(input())
    y = int(input())
    print(x+y)


# x = int(input('wprowadź liczbę'))
# y = int(input('wprowadź liczbę'))

def dodawanie(x,y):
    print(x+y)
def odejmowanie(x,y):
    print(x-y)
def mnozenie(x,y):
    print(x*y)
def dzielenie(x,y):
    print(x/y)
def modulo(x,y):
    print(x%y)
def potegowanie(x,y):
    print(x**y)