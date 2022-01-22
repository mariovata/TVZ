# Napišite program koji učitava riječ(riječ je predstavljena malim slovima) i stvara odgovarajuću zbirku <zbirka1> koja sadrži zapis o tome koliko puta se pojavilo koje slovo u riječi.Primjerice za riječ:ivana treba pohraniti da se 'i' pojavilo 1 puta, 'v' 1 puta, 'a' 2 puta, te 'n' 1 puta.
#
# Nakon kreiranja zbirke sa zapisima o pojavi slova,tu zbirku treba ispisati.
#
# ---------------------------------------------------------------------------------
#
# Nakon toga je potrebno napisati funkciju koja od korisnika traži unos 2 jedinstvena mala slova i smješta ih u skup.Ukoliko se unese isti znak potrebno je ispisati:'Ponovi unos' i tražiti novi unos.Funkcija nakon uspješnog učitavanja ispisuje kreirani skup od 2 jedinstvena slova,te kao povratnu vrijednost vraća koeficijent.
#
# Koeficijent se izračunava kao:
#
# ( (broj pojava prvog slova iz skupa u riječi + broj pojava drugog slova iz skupa u riječi)+2 ) / 2
#
# ----------------------------------------------------------------------------------
#
# Potrebno je pozvati prethodnu funkciju koja će tražiti unos slova i ispisati skup, te  povratnu vrijednost funkcije spremiti u varijablu <koeficijent>.Treba ispisati varijablu koeficijent u poruci:'Koeficijent je <koeficijent>'
#
#
# Nakon toga je potrebno iz zbirke <zbirka1> kreirati listu koja će sadržavati samo ona slova koja su se pojavila u riječi manje nego što iznosi <koeficijent> (ujedno broj pojava mora biti neparan broj). Tu listu je potrebno ispisati.
#
# Primjer željenog rada programa:

import collections
import math

def calc_1(rijec,rijec_d):
    let1, let2 = 'a', 'a'
    while let1 == let2:
        let1 = str(input(('Unesite slovo:')).lower())
        let2 = str(input(('Unesite slovo:')).lower())
        if let1 == let2:
            print('Ponovite unos')
    a = set(let1)
    b = set(let2)
    set_1 = a | b
    print(f"Skup slova je: {set_1}")

    for slovo, pojava in rijec_d.items():
        if pojava != 0:
            if slovo == let1:
                # print(slovo,pojava,sep='\t')
                pojava1 = pojava
                # print(pojava1)
            else:
                pojava1 = 0
                # print(pojava1)

    for slovo, pojava in rijec_d.items():
        if pojava != 0:
            if slovo == let2:
                # print(slovo,pojava,sep='\t')
                pojava2 = pojava
                # print(pojava2)
            else:
                pojava2 = 0
                # print(pojava2)

    kof = ((pojava1 + pojava2) + 2) / 2
    return kof


def main():
    rijec = input("Unesite rijec: ")
    rijec_d = dict(collections.Counter(rijec))
    print(rijec_d)

    kof = calc_1(rijec,rijec_d)
    print(f"Koeficijent je {kof}")
    kof2 = int(round(kof))

    lista_1 = list(rijec_d.keys())
    while len(lista_1) > kof2 or len(lista_1) % 2 == 0:
            print(len(lista_1), kof2,lista_1)
            lista_1.pop()
            # if len(lista_1) % 2 and not len(lista_1) == 1:
            #     lista_1.pop()

    print(f"Lista je: {lista_1}")


main()
