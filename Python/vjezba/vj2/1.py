def unos():
    a = 1
    while a == 1:
        adr1 = input("Unesite adresu: ")
        adr2 = input("Unesite adresu: ")
        adr3 = input("Unesite adresu: ")
        adr4 = input("Unesite adresu: ")

        chk1 = adr1[::-1]
        chk1 = chk1[:2]

        chk2 = adr2[::-1]
        chk2 = chk2[:2]

        chk3 = adr3[::-1]
        chk3 = chk3[:2]

        chk4 = adr4[::-1]
        chk4 = chk4[:2]

        try:
            chk1 = int(chk1)
            chk2 = int(chk2)
            chk3 = int(chk3)
            chk4 = int(chk4)

            a = 0
            return chk1, chk2, chk3, chk4
        except ValueError:
            print("bad")


def main():
    adr1, adr2, adr3, adr4 = unos()
    zbroj = adr1 + adr2 + adr3 + adr4
    print(f"Zbroj  brojeva kucnih adresa je {zbroj}")
    adr1, adr2, adr3, adr4 = str(adr1), str(adr2), str(adr3), str(adr4)
    a = adr1.count("1") + adr2.count("1") + adr3.count("1") + adr4.count("1")
    b = adr1.count("2") + adr2.count("2") + adr3.count("2") + adr4.count("2")
    c = adr1.count("3") + adr2.count("3") + adr3.count("3") + adr4.count("3")
    d = adr1.count("4") + adr2.count("4") + adr3.count("4") + adr4.count("4")
    e = adr1.count("5") + adr2.count("5") + adr3.count("5") + adr4.count("5")
    f = adr1.count("6") + adr2.count("6") + adr3.count("6") + adr4.count("6")
    g = adr1.count("7") + adr2.count("7") + adr3.count("7") + adr4.count("7")
    h = adr1.count("8") + adr2.count("8") + adr3.count("8") + adr4.count("8")
    i = adr1.count("9") + adr2.count("9") + adr3.count("9") + adr4.count("9")

    print(f"Znamenka 1 se pojavila {a}")
    print(f"Znamenka 2 se pojavila {b}")
    print(f"Znamenka 3 se pojavila {c}")
    print(f"Znamenka 4 se pojavila {d}")
    print(f"Znamenka 5 se pojavila {e}")
    print(f"Znamenka 6 se pojavila {f}")
    print(f"Znamenka 7 se pojavila {g}")
    print(f"Znamenka 8 se pojavila {h}")
    print(f"Znamenka 9 se pojavila {i}")


main()
