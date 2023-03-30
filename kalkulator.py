from funkcje import dodawanie
from funkcje import odejmowanie
from funkcje import mnozenie
from funkcje import dzielenie
from funkcje import potegowanie
from funkcje import modulo

def kalkulator():
    '''
    kalkulator musi zapytać użytkownika o to jakie działanie chce podjąć i następnie kazać mu wprowadzić zmienne i dopasować odpowiednie funkcje do działania usera.

    proj:
        - pada temat pytania ?? -> index?? int(input("Jakie działanie chcesz wykonać? \n
                                            1  2  3  4  5  6"))
    '''
    index = int(input("Jakie działanie chcesz podjąć"))
    match index:
        case 1:
            x = int(input())
            y = int(input())
            dodawanie(x,y)
        case 2:
            pass
        case 3:
            pass