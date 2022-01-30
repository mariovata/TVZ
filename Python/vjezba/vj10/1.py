# Napišite program koji za N pisaca zabilježava u datoteku što su napisali.  Svaki pisac unosi redak teksta, te delimiter (znak koji se stavlja između riječi umjesto praznine). U datoteku se za svakog pisca (u funkciji) unosi sljedeći tekst, koji zauzima jedan redak:
#
# <redni_broj_pisca> . pisac pise: rijec1<delimiter>rijec2<delimiter>....
#
# Za sljedeći zapis se prelazi u novi redak.
#
# Nakon što se datoteka zatvori, otvara se za čitanje te se na ekran ispisuje sadržaj datoteke, kao i što su rekli pisac broj A i pisac broj B. (Brojevi A i B se čitaju sa tipkovnice)
# Primjer:


def fun(n):
    brojac = 0
    while brojac < n:
        brojac += 1
        print(f"{brojac}.Pisac")
        delim = input("Delimiter: ")
        tekst = input("Unesite tekst: ")

        lista = tekst.split(" ")
        # print(lista)
        res = ''
        for i in lista:
            res = res + str(i) + delim

        # print(str(res))
        dat = open("C:\\Users\\Mario\\Desktop\\1.txt", "a")
        dat.write(f"{brojac} pisac pise: " + res + '\n')
        dat.close()


def main():
    n = int(input("N: "))
    fun(n)

    print("sadrzaj datoteke: ")
    dat = open("C:\\Users\\Mario\\Desktop\\1.txt", "r")
    file = dat.readlines()
    for i in range(n):
        print(file[i])

    tek1 = int(input("Dohvati sto pise pisac broj: "))
    tek2 = int(input("i sto pise, pisac broj: "))

    tek1 = tek1 - 1
    x = file[tek1]
    x = x[14:]
    print(x)

    tek2 = tek2 - 1
    y = file[tek2]
    y = y[14:]
    print(y)


main()
