def main():
    rec = input("Unos: ")

    rec = rec.strip()
    while rec[-1] != '.':
        rec = input("Unos, tocka na kraju: ")

    rec = rec.strip(".")


    while '  ' in rec:
        rec = rec.replace('  ', ' ')

    rec1, rec2, rec3 = rec.split(' ', 2)

    print("1.", rec1)
    print("2.", rec2)
    print("3.", rec3)

    max_rec = rec1
    rec3 = rec3.replace("lj", "?")

    if len(max_rec) < len(rec2):
        max_rec = rec2
        max_rec = max_rec[::-1]
        max_rec = max_rec.replace("?", "lj")
        print(rec1, max_rec, rec3 + ".")
        exit()
    if len(max_rec) < len(rec3):
        max_rec = rec3
        max_rec = max_rec[::-1]
        max_rec = max_rec.replace("?", "lj")
        print(rec1, rec2, max_rec + ".")
        exit()

    max_rec = max_rec[::-1]
    max_rec = max_rec.replace("?", "lj")
    print(max_rec, rec2, rec3 + ".")


main()
