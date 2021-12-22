import string
import random

def lista1(n):
    a = []
    print(len(a))
    while len(a) < n:
        a.append(random.choice(string.ascii_lowercase))
        for i in a:
            if i == "a" or i == "e" or i == "i" or i == "u":
                a.remove(i)
    print(a)
    return a


def fun2(lst,ele):

    count = lst.count(ele)
    print(count)

    inx = lst.index(ele)
    inx = inx+1

    return count,inx


def main():
    n = 0
    while n < 12:
        n = int(input("Unesi n: "))

    lst = lista1(n)
    ele = input("Unesite slovo: ")
    broj,inx = fun2(lst,ele)
    print(f"Slovo {ele} se pojavilo {broj} puta")
    print(f"Redni broj pojave : na {inx}.poziciji")

    min_let = min(lst, key=lst.count)
    min_inx = lst.index(min_let)
    min_inx = min_inx + 1
    print(f"U listi se slovo {min_let} pojavilo najmanje 1. puta redni broj pojave je {min_inx}. pozicija")


main()
