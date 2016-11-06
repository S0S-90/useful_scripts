from __future__ import division

# Primzahlen
# prim(integer): überprüfen, ob Primzahl, bzw. kleinster Teiler -> math
# eratostenes(obergrenze): Erstellung von Primzahlen (Sieb des Eratosthenes) -> numpy, math

# sonstiges zum Thema Zahlen
# quersumme(integer): Quersumme
# anzahl_ziffern(integer): Anzahl der Ziffern
# create_products(summe): Produkte zweier Zahlen mit gegebener Summe
# create_sums(product): Summen zweier Zahlen mit gegebenem Produkt
# wurzel_2_kettenbruch(iterationen): Näherung für die Wurzel aus 2
# e_kettenbruch(iterationen): Näherung für e
# periodenlaenge_kettenbruch_wurzel(integer): Periodenlänge des Kettenbruchs -> math, ggt
# naeherung_kettenbruch_wurzel(integer, iterationen): Näherung für Wurzel -> kehrbruch, addieren, math, ggt_3
# partitions(n,k): Partitionen für Zahl n mit k Summanden
# partitions_sum(n): Partitionen (Möglichkeiten als Summe darzustellen) für Zahl n -> partitions

# Zahlenquadrat, das von der Mitte ausgehendend spiralförmig gefüllt wird
# zahlen_rechts_oben(seitenlaenge): diagonale Zahlen rechts oben 
# zahlen_links_oben(seitenlaenge): diagonale Zahlen links oben 
# zahlen_links_unten(seitenlaenge): diagonale Zahlen links unten 
# zahlen_rechts_unten(seitenlaenge): diagonale Zahlen rechts unten
# diagonale(seitenlaenge): Zahlen beider Diagonalen

# Teiler und Vielfache
# dualzahl(integer): Umrechnung in Dualzahl
# kl_teiler(integer): kleinster Teiler einer Zahl -> math
# teiler(integer): alle Teiler einer Zahl -> math
# summe_teiler(integer): Summe aller Teiler einer Zahl -> math
# primfaktoren(integer): Primfaktoren -> kl_teiler
# distinct_primefactors(integer): unterschiedliche Primfaktoren -> primfaktoren
# abundant(obergrenze): abundante Zahlen -> math (teiler?)
# sum_of_abundant(obergrenze): mögliche Summen aus 2 abundanten Zahlen -> abundant
# fakultaet(integer): Berechnung von n!
# fac_digits_sum(integer): Summe der Fakultäten der einzelnen Ziffern -> Liste faks
# len_fac_digits_sum(integer): Kettenlänge von Kette aus fac_digits_sum -> fac_digits_sum
# binomial(n,k): Binomialkoeffizient 
# kgV(int1, int2): kleinstes gemeinsames Vielfaches
# ggt_3(a,b,c): ggT von 3 Zahlen -> ggt

# Brüche (Klasse beachten!)
# ggt(a,b): größter gemeinsamer Teiler
# kuerzen(zaehler, nenner): Kürzen von Brüchen -> ggt
# kehrbruch(bruch): Kehrbruch
# dezimalbruch(nenner): Zahl als Dezimalbruch schreibbar
# periodenlaenge(nenner): Berechnung der Periodenlänge -> dezimalbruch
# addieren(bruch1, bruch2): Addieren von 2 Brüchen
# multiplizieren(bruch1, bruch2): Multiplizieren von 2 Brüchen -> kuerzen
# teilen(bruch1, bruch2): Dividieren von Brüchen -> kuerzen
# zaehler_more_digits(bruch): Zähler mehr Ziffern als Nenner?
# kuerzen_falsch(zaehler, nenner): "naives Kuerzen" (24/43 = 2/3)

# Folgen und Reihen
# fibonacci(n): n.te Fibonacci-Zahl
# fibonacci_liste(maximum): alle Fibonacci-Zahlen unterhalb des Maximums -> fibonacci
# triangle_number(integer): Dreieckszahl? -> math
# square_number(integer): Quadratzahl? -> math
# pentagon_number(integer): Fünfeckszahl? -> math
# hexagon_number(integer): Sechseckszahl? -> math
# heptagon_number(integer): Siebeneckszahl? -> math
# octagonal_number(integer): Achteckszahl? -> math
# lychrel(integer): Lychrel-Zahl? -> palindrome, rueckwaerts
# collatz(start): Collatzfolge von Start bis 1
# kaprekar(integer): Berechnung der Kaprekar-Konstante
# eulers_phi(integer): Werte für Eulers Phi-Funktion -> kl_teiler
# nextnumber(str(int)): nächste Zahl in der Folge "Look and say sequence"

# Funktionsbetrachtungen
# ableitung(f, x, h=0.0001): Ableitung an Stelle x (Näherung)
# newton(x0, f): Nullstelle mit Newton-Verfahren -> ableitung

# Geometrie
# summe_vektoren(vec1, vec2): Vektorsumme in R³
# produkt_vektor_zahl(vec, zahl): Produkt aus Vektor und Zahl in R³
# skalarprodukt(vec1, vec2): Skalarprodult in R³
# euklid_vektor(vec): Länge eines Vektors in R³
# solutions(perimeter): rechtwinklige Dreiecke mit gegebenem Umfang
# solutions_anzahl(obergrenze): Anzahl rechtwinkliger Dreiecke mit gegebenem Umfang -> ggt

# Anordnungen und Vertauschen
# doppelt(liste): ein Element doppelt?
# palindrome(integer): 6-stellige Zahl Palindrom?
# rueckwaerts(integer): Zahl rückwärts lesen
# rotations(integer): Rotationen einer Zahl (197 -> 971 and 719)
# remove_digits(integer): Entfernen von Ziffern von vorne und hinten
# permutations(iterable): Permutationen von Ziffern
# is_permutation(int1, int2): Zahlen Permutationen?
# ersetzen(integer): Ersetzen von gleichen Ziffern in einer Zahl -> copy
# zusammensetzen(int1, int2): Zusammesetzen von Zahlen

# string-Funktionen
# number_in_alphabet(buchstabe): Position im Alphabet
# alphabetical_value(string): Summe der Buchstaben eines Wortes -> number_in_alphabet


def eratosthenes(obergrenze):
    """gibt eine Liste von Primzahlen von 2 bis zur Obergrenze aus
    Berechnung mittels Sieb des Eratosthenes

    benötigt: numpy, math"""
    prim = numpy.ones(obergrenze+1)
    prim[0] = 0
    prim[1] = 0
    zahl = 2
    teiler = 2
    while teiler <= math.sqrt(obergrenze):
        i = 2
        if prim[teiler] == 1:
            prod = i*teiler
            while prod <= obergrenze:
                prim[prod] = 0
                prod = i*teiler
                i = i+1
        teiler = teiler + 1
    primzahlen = [] #neue Liste
    for counter in range(len(prim)):
        if prim[counter] == 1:
            primzahlen.append(counter)
    return primzahlen

def rotations(integer):
    """gibt eine Liste der Rotationen einer Zahl (197 -> 971 and 719) aus
    """
    zahl = str(integer)
    rot = []
    for i in range(len(zahl)-1): # -1 weg, wenn integer mit ausgegeben werden soll
        zahl = zahl[-1] + zahl[0:-1]
        rot.append(int(zahl))
    return rot

def fakultaet(integer):
    """berechnet die Fakultät n! einer Zahl n
    """
    if integer == 0:
        return 1
    erg = 1
    for i in range(integer, 1, -1):
        erg = erg*i
    return erg

def binomial(n,k):
    """gibt den Binomialkoeffizienten (k aus n) an

    Quelle: http://hodge.mathematik.uni-mainz.de/~stefan/python/lehrerfortbildung2006.pdf, Folie 11
    """
    out=1
    for i in range(1,k+1):
        out = (out*(n-i+1))//i
    return out

def kuerzen_falsch(zaehler, nenner):
    """überprüft, ob "naives Kürzen" (24/43 = 2/3) zum richtigen Ergebnis führt

    "naives Kürzen" entweder nicht möglich oder falsch oder trivial (10/20; 12/12) -> Ausgabe 0
    "naives Kürzen" richtig und nicht trivial -> Ausgabe des gekürzten Bruchs als Liste"""
    z = str(zaehler)
    n = str(nenner)
    if z == n: #trivial
        return 0
    elif int(z[1]) == 0 and int(n[1]) == 0: #trivial
        return 0
    elif z[0] == n[1]:
        if int(n[0]) == 0:
            return 0
        bruch1 = zaehler / nenner
        bruch2 = int(z[1]) / int(n[0])
        if bruch1 == bruch2:
            return [int(z[1]), int(n[0])]
        else:
            return 0
    elif z[1] == n[0]:
        if int(n[1]) == 0:
            return 0
        bruch1 = zaehler / nenner
        bruch2 = int(z[0]) / int(n[1])
        if bruch1 == bruch2:
            return [int(z[0]), int(n[1])]
        else:
            return 0
    else:
        return 0

def summe_teiler(integer):
    """gibt die Summe aller Teiler einer Zahl (ohne Zahl selber) aus

    benötigt: math"""
    i = 2
    teiler = 1
    while i <= math.sqrt(integer):
        if integer%i == 0:
            teiler = teiler + i+ integer/i
        i = i + 1
    return teiler

def teiler(integer):
    """gibt eine Liste aller Teiler einer Zahl (inkl. Zahl selbst) aus
    nicht sortiert!

    benötigt: math

    Verbesserungsmöglichkeit: Hinzufügen zu Liste mit append
    """
    i = 2
    teiler = [1, integer]
    while i <= math.sqrt(integer):
        if integer%i == 0:
            teiler = teiler + [i]+[integer/i]
        i = i + 1
    return teiler

def prim(integer):
    """gibt für Primzahlen den String "prim" zurück, ansonsten den kleinsten Teiler bzw. 0 für 0 und 1

    benötigt: math"""
    if integer == 0 or integer == 1:
        return 0
    i = 2
    erg = "prim"
    while i <= math.sqrt(integer):
        if integer%i == 0:
            erg = i
            break
        i = i + 1
    return erg

def kl_teiler(integer):
    """gibt den kleinsten Teiler einer Zahl (bei Primzahlen die Zahl selbst) zurück

    benötigt: math"""
    i = 2
    erg = integer
    while i <= math.sqrt(integer):
        if integer%i == 0:
            erg = i
            break
        i = i + 1
    return erg

def ggt(a, b):
    """berechnet den groessten gemeinsamen Teiler zweier Zahlen

    Quelle: http://www.iti.fh-flensburg.de/lang/krypto/algo/euklid.htm"""
    while b != 0:
        a, b = b, a%b
    return a

def ggt_3(a,b,c):
    """berechnet den größten gemeinsamen Teiler von drei Zahlen

    benötigt: ggt"""
    erg = ggt(a,b)
    return ggt(erg,c)

def kuerzen(zaehler, nenner):
    """kürzt einen Bruch und gibt das Ergebnis als Liste der Form [zähler, nenner] aus

    benötigt: ggt
    """
    z = zaehler / ggt(zaehler, nenner)
    n = nenner / ggt(zaehler, nenner)
    return [int(z), int(n)]

def addieren(bruch1, bruch2):
    """addiert zwei Brüche ohne das Ergebnis zu kürzen

    Eingabe: bruch1, bruch2 je als Liste der Form [zähler, nenner]
    Ausgabe: Produkt als Bruch der Form [zähler, nenner]
    """
    z = bruch1[0] * bruch2[1] + bruch2[0] * bruch1[1]
    n = bruch1[1] * bruch2[1]
    return [z, n]

def multiplizieren(bruch1, bruch2):
    """multipliziert zwei Brüche

    Eingabe: bruch1, bruch2 je als Liste der Form [zähler, nenner]
    Ausgabe: Produkt als Bruch der Form [zähler, nenner]

    benötigt: kuerzen
    """
    nenner = bruch1[1]*bruch2[1]
    zaehler = bruch1[0]*bruch2[0] 
    return kuerzen(zaehler, nenner)

def teilen(bruch1, bruch2):
    """teilt bruch1 durch bruch2

    Eingabe: bruch1, bruch2 je als Liste der Form [zähler, nenner]
    Ausgabe: Produkt als Bruch der Form [zähler, nenner]

    benötigt: kuerzen
    """
    z = bruch1[0] * bruch2[1]
    n = bruch1[1] * bruch2[0]
    return kuerzen(z, n)

def kehrbruch(bruch):
    """berechnet den Kehrbruch zu einem Bruch der Form [zaehler, nenner]"""
    return [bruch[1], bruch[0]]

def zaehler_more_digits(bruch):
    """überprüft, ob der Zähler des Bruchs mehr Ziffern hat als der Nenner

    Eingabe: bruch als Liste der Form [zähler, nenner]
    Ausgabe:
    - 1, wenn Zähler mehr Ziffern als Nenner
    - 0, wenn Zähler nicht mehr Ziffern als Nenner
    """
    z = str(bruch[0])
    n = str(bruch[1])
    if len(z) > len(n):
        return 1
    else:
        return 0

def dezimalbruch(nenner):
    """überprüft, ob sich eine Zahl als Produkt aus 2ern und 5ern schreiben lässt

    ja -> Ausgabe: 1
    nein -> Ausgabe: Rest, der bleibt, wenn man sooft wie möglich durch 2 und 5 geteilt hat
    """
    while integer%2 == 0:
        integer = integer/2
    while integer%5 == 0:
        integer = integer/5
    if integer == 1:
        return 1
    else:
        return integer

def periodenlaenge(nenner):
    """bestimmt die Periodenlaenge eines Bruchs

    kein periodischer Dezimalbruch -> Ausgabe: 0
    periodischer Dezimalbruch -> Ausgabe: Periodenlänge

    benötigt: dezimalbruch

    Methode: http://www.arndt-bruenner.de/mathe/scripts/periodenlaenge.htm
    """
    if geht_auf(integer) == 1:
        return 0
    else:
        rest = 10 % geht_auf(integer) 
        counter = 1
        while rest != 1:
            counter += 1
            rest = 10*rest % geht_auf(integer) 
        return counter

def abundant(obergrenze):
    """gibt eine Liste aller abundanten Zahlen unterhalb der Obergrenze aus
    abundant: (Summe aller Teiler ohne die Zahl selbst) > (Zahl selbst)

    benötigt: math

    Verbesserungsmöglichkeit: eine der teiler-Funktionen nutzen
    """
    abundant = []
    for integer in range(1, obergrenze):
        i = 2
        teiler = 1
        while i <= math.sqrt(integer):
            if integer%i == 0:
                teiler = teiler + i
                if integer/i != i:
                    teiler = teiler + integer/i
            i = i + 1
        if teiler > integer:
            abundant = abundant + [integer]
    return abundant

def sum_of_abundant(obergrenze):
    """gibt eine Liste aller möglichen Summen von abundanten Zahlen unterhalb der Obergrenze aus

    benötigt: abundant

    Verbesserungsmöglichkeit: Hinzufügen zu Liste mit append
    """
    liste = abundant(obergrenze)
    sums = []
    for a in liste:
        for b in liste:
            summe = a + b
            if summe not in sums:
                sums = sums + [summe]
                if summe >= obergrenze:
                    break
    return sums

def number_in_alphabet(buchstabe):
    """gibt die Position eines Buchstaben im Alphabet aus (nur Großbuchstaben)"""
    return ord(buchstabe) - 64

def alphabetical_value(string):
    """gibt die Summe der Buchstaben (A=1, B=2,...) eines Wortes aus

    benötigt: number_in_alphabet"""
    value = 0
    for i in range(len(string)):
        value = value + number_in_alphabet(string[i])
    return value

def collatz(start):
    """gibt die Collatzfolge vom Startwert bis 1 als Liste aus

    Collatzfunktion:
    n → n/2      if n is even
    n → 3n + 1   if n is odd
    """
    erg = [integer]
    while integer != 1:
        if integer%2 == 0:
            integer = integer/2
        else:
            integer = 3*integer + 1
        erg = erg + [int(integer)]
    return erg

def kgV(int1, int2):
    """gibt das kleinste gemeinsame Vielfache von 2 Zahlen aus"""
    a = max(int1, int2)
    b = min(int1, int2)
    i = 1
    while True:
        prod = a*i
        if prod%b == 0:
            return prod
            break
        i = i+1

def palindrome(integer):
    """überprüft, ob eine Zahl ein Palindrom ist
    
    Ausgabe
    0: kein Palindrom
    1: Palindrom"""
    erg = 1
    string = str(integer)
    for i in range(int(len(string)/2)):
        if string[i] != string[-i-1]:
            erg = 0
            break
    return erg

def fibonacci(n):
    """berechnet die n.te Fibonacci-Zahl

    Verbesserungsmöglichkeit: for-Schleife statt counter = counter + 1"""
    counter = 1
    f1 = 2
    f0 = 1
    f = 0
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        while counter < n:
            f = f0 + f1 
            f0 = f1
            f1 = f
            counter = counter + 1
        return f

def fibonacci_liste(maximum):
    """gibt eine Liste aller Fibonacci-Zahlen unterhalb des Maximums aus

    kann vermutlich noch verbessert werden:
    - nicht für jede Zahl neu alle Fibs darunter berechnen
    - append verwenden

    benötigt: fibonacci"""
    counter = 0
    fibs = []
    while fibonacci(counter) < maximum:
        fibs = fibs + [fibonacci(counter)]
        counter = counter + 1
    return fibs

def doppelt(liste):
    """überprüft, ob ein Element einer Liste oder einem String mindestens doppelt vorkommt

    0: kein Element kommt doppelt vor
    1: min. ein Element kommt mind. 2x vor"""
    erg = 0
    for i in liste:
        start = liste.index(i) + 1
        for j in range(start, len(liste)):
            if i == liste[j]:
                erg = 1
    return erg

def ableitung(f,x,h=0.0001):
    """berechnet die Ableitung (Steigung) einer Funktion f an der Stelle x (Näherung)

    Eingabe:
    f: Name einer Python-Funktion ohne Parameter
    x: x-Wert, an der die Ableitung berechnet werden soll
    h: Größe des "Steigungsdreiecks" -> Genauigkeit
    """
    return (f(x+h)-f(x-h))/(2.0*h)

def newton (x0, f):
    """ Funktion zur Berechnung einer Nullstelle mit Hilfe des Newton-Verfahrens
    Abbruch:
    - f(x) < 10^(-6)
    - Differenz den x-Werten < 10^(-6)
    - 200 Iterationen

    Eingabe:
    x0: Startwert für die Näherung
    f: Python-Funktion ohne Parameter
    
    Ausgabe: Nullstelle, Anzahl Iterationen, Abbruchgrund

    benötigt: ableitung
    """
    n = 0
    vergleich = x0
    if ableitung(f, x0) != 0:
            x_n = x0 - f(x0) / ableitung(f, x0)
    else:
            return "ERROR - Division durch 0"
    while abs(f(x_n)) > 10**(-6) and abs(x_n-vergleich) > 10**(-6) and n < 200:
        if ableitung(f, x0) != 0:
            x_n = x0 - f(x0) / ableitung(f, x0)
        else:
            return "ERROR"
            break
        vergleich = x0
        x0 = x_n
        n = n+1
    if f(x_n) <= 10**(-6):
        ex = "Funktion klein genug"
    elif n >= 200:
        ex = "genug Iterationen"
    else:
        ex = "Nullstelle konstant"
    return x_n, n, ex

def kaprekar(integer):
    """gibt die Kaprekar-Konstante für einen bestimmten Startwert aus
    Kaprekar-Algorithmus:
    - Umsortieren der Ziffern, sodass die größt- und kleinstmögliche Zahl entstehen
    - Bildung der Differenz
    - Anwendung der ersten beiden Schritte auf die neu entstandene Zahl
    Kaprekar-Konstante: Zahl, die sich durch Anwendung des Kaprekar-Algorithmus nicht mehr ändern

    from __future__ import division muss ausgeschaltet werden!
    
    Verbesserungsmöglichkeiten:
    - counter = counter + 1
    - Datentypen geschickter nutzen (Ziffern finden über string, Division über int)
    """
    zahl = 0
    string = str(integer)
    ziff_anz = len(string)

    while integer != zahl:

        zahl = integer

        counter = ziff_anz - 1
        ziffern = []
        z = zahl
        while counter >= 0:
                ziffer = z/(10**counter)
                z = z%(10**counter)
                ziffern = ziffern + [ziffer]
                counter = counter - 1

        ziff_sort = sorted(ziffern)

        g = 0
        counter = 0
        while counter < ziff_anz:
            g = g + (10**counter)*ziff_sort[counter]
            counter = counter + 1

        k = 0
        counter = 0
        while counter < ziff_anz:
            k = k + 10**(ziff_anz-1-counter)*ziff_sort[counter]
            counter = counter + 1

        integer = g - k
        
    return integer

def remove_digits(integer):
    """gibt eine Liste aller Zahlen aus, die entstehen, wenn man von der gegebenen Zahl nacheinander sowohl von vorne als auch von hinten die Ziffern wegnimmt (ohne Zahl selber)
    Bsp.: 3797 -> 797, 97, 7, 379, 37, 3 (nicht in dieser Reihenfolge)
    """
    string = str(integer)
    zahlen = []
    laenge = len(string)
    for i in range(laenge-1):
        zahlen.append(int(string[i+1:laenge]))
        zahlen.append(int(string[0:i+1]))
    return zahlen

def summe_vektoren (vec1, vec2):
    """addiert zwei Vektoren
    Vektor (Eingabe + Ausgabe): Liste der Form [x1, x2, x3]"""
    r1 = vec1[0] + vec2[0]
    r2 = vec1[1] + vec2[1]
    r3 = vec1[2] + vec2[2]
    result = [r1, r2, r3]
    return result

def produkt_vektor_zahl (vec, zahl):
    """bildet das Produkt aus einem Vektor und einer Zahl
    Vektor (Eingabe + Ausgabe): Liste der Form [x1, x2, x3]"""
    r1 = vec[0] * zahl
    r2 = vec[1] * zahl
    r3 = vec[2] * zahl
    result = [r1, r2, r3]
    return result

def skalarprodukt (vec1, vec2):
    """bildet das Skalarprodukt aus zwei Vektoren
    Vektor (Eingabe + Ausgabe): Liste der Form [x1, x2, x3]"""
    result = vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2]
    return result

def euklid_vektor (vec):
    """berechnet die Länge eines Vektors
    Vektor (Eingabe): Liste der Form [x1, x2, x3]"""
    result = (vec[0]**2 + vec[1]**2 + vec[2]**2)**0.5
    return result

def permutations(iterable, r=None):
    """bildet alle Permutationen einer Liste von Ziffern 

    Ausgabe als Integer
    wegen Generator Abruf mit: print list(permutations(liste))

    Quelle (leicht verändert): http://docs.python.org/2/library/itertools.html#itertools.permutations
    """
    pool = list(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    a = list(pool[i] for i in indices[:r])
    string = ""
    for z in a:
        string = string + str(z)
    yield int(string)
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                a = list(pool[i] for i in indices[:r])
                string = ""
                for z in a:
                    string = string + str(z)
                yield int(string)
                break
        else:
            return

def is_permutation(int1, int2):
    """überprüft, ob zwei Zahlen Permutationen derselben Ziffern sind

    1: Permutationen
    0: keine Permutationen
    """
    list1 = list(str(int1))
    list2 = list(str(int2))
    list1.sort()
    list2.sort()
    if list1 == list2:
        return 1
    else:
        return 0

def dualzahl(integer):
    """rechnet eine "normale" Zahl (Basis 10) in eine Dualzahl (Basis 2) um"""
    bases = [1]
    base = 2
    i = 1
    while bases[-1]*2 <= integer:
        bases.append(2**i)
        i = i+1
    bases.reverse()
    ziffern = ""
    for i in bases:
        ziffern = ziffern + str(int(integer/i))
        integer = integer%i
    return int(ziffern)

def solutions(perimeter):
    """berechnet die möglichen Seitenlängen a, b und c für ein rechtwinkliges Dreieck bei gegebenem Umfang"""
    sol = []
    for a in range(1, int(perimeter/2)):
        b = (perimeter*(2*a-perimeter))/(2*(a-perimeter))
        if a<b and b == int(b):
            c = perimeter - a-b
            sol.append([a,b,c])
    return sol

def solutions_anzahl(obergrenze):
    """gibt für jeden ganzzahligen Umfang eines rechtwinkligen Dreiecks an, wie viele Möglichkeiten es gibt, diesen mit ganzzahligen Seitenlängen zu erreichen

    Eingabe: Obergrenze für den Umfang
    Ausgabe: numpy-Array mit Anzahl der entsprechenden Möglichkeiten von 0-Obergrenze

    benötigt: numpy, ggt"""
    sol = numpy.zeros(obergrenze+1)
    for u in range(1, obergrenze):
        if u%2 == 0:
            v = 1
        else:
            v = 2
        perimeter = 2*u**2 + 2*u*v
        while perimeter <= obergrenze and u>v:
            if perimeter < len(sol) and ggt(u,v)==1:
                sol[perimeter] = sol[perimeter] + 1
                faktor = perimeter
                perimeter = 2*perimeter
                while perimeter < len(sol):
                    sol[perimeter] = sol[perimeter] + 1
                    perimeter = perimeter + faktor
            v = v+2
            perimeter = 2*u**2 + 2*u*v
    return sol

def triangle_number(integer):
    """überprüft, ob es sich bei integer um eine Dreieckszahl handelt

    Ausgabe:
    1: Dreieckszahl
    0: keine Dreieckszahl

    benötigt: math
    """
    if (math.sqrt(8*integer + 1) - 1) % 2 == 0:
        return 1
    else:
        return 0

def square_number(integer):
    """überprüft, ob integer eine Quadratzahl (n(2n-1)) ist

    Ausgabe:
    1: Quadratzahl
    0: keine Quadratzahl

    benötigt: math"""
    wurzel = math.sqrt(integer)
    if wurzel == int(wurzel):
        return 1
    else:
        return 0

def pentagon_number(integer):
    """überprüft, ob integer eine Pentagonalzahl (n(3n−1)/2) ist

    Ausgabe:
    1: Pentagonalzahl
    0: keine Pentagonalzahl

    benötigt: math"""
    if (1 + math.sqrt(1+24*integer)) % 6 == 0:
        return 1
    else:
        return 0

def hexagon_number(integer):
    """überprüft, ob integer eine Sechseckszahl (n(2n-1)) ist

    Ausgabe:
    1: Sechseckszahl
    0: keine Sechseckszahl

    benötigt: math"""
    if (1 + math.sqrt(1+8*integer)) % 4 == 0:
        return 1
    else:
        return 0

def heptagon_number(integer):
    """überprüft, ob integer eine Siebeneckszahl (n(2n-1)) ist

    Ausgabe:
    1: Siebeneckszahl
    0: keine Siebeneckszahl

    benötigt: math"""
    if (3 + math.sqrt(9+40*integer)) % 10 == 0:
        return 1
    else:
        return 0

def octagonal_number(integer):
    """überprüft, ob integer eine Achteckszahl (n(2n-1)) ist

    Ausgabe:
    1: Achteckszahl
    0: keine Achteckszahl

    benötigt: math"""
    if (1 + math.sqrt(1+3*integer)) % 3 == 0:
        return 1
    else:
        return 0

def primfaktoren(integer):
    """gibt die Primfaktoren einer Zahl als Liste zurück

    benötigt: kl_teiler"""
    faktoren = []
    neu_fak = kl_teiler(integer)
    while neu_fak != 1:
        faktoren.append(int(neu_fak))
        integer = integer/neu_fak
        neu_fak = kl_teiler(integer)
    return faktoren

def distinct_primefactors(integer):
    """gibt alle unterschiedlichen Primfaktoren einer Zahl zurück

    benötigt: kl_teiler"""
    faktoren = []
    neu_fak = kl_teiler(integer)
    while neu_fak != 1:
        if neu_fak not in faktoren:
            faktoren.append(neu_fak)
        integer = integer/neu_fak
        neu_fak = kl_teiler(integer)
    return faktoren

def ersetzen(integer):
    """ersetzt in einer Zahl von 5-6 Ziffern Länge 2-5 gleiche Ziffern durch andere gleiche Ziffern, wobei die letzte Ziffer nie ersetzt wird

    Ausgabe: Liste von Listen, von denen in einer jeweils die Zahlen stehen, die durch Ersatz der Ziffern xx jeweils durch 0-9 entstehen und größer als integer sind

    Bsp.:
    Eingabe: 526223
    Ausgabe: [[526223, 536323, 546423, 556523, 566623, 576723, 586823, 596923],
             [526223, 536233, 546243, 556253, 566263, 576273, 586283, 596293],
             [526223, 526333, 526443, 526553, 526663, 526773, 526883, 526993],
             [526223, 536333, 546443, 556553, 566663, 576773, 586883, 596993]]

    benötigt: copy
    """
    string = str(integer)
    zahl = list(string)
    liste = []
    for ziffer1 in range(len(zahl)-1):  #zwei ersetzen
        for ziffer2 in range(ziffer1+1, len(zahl)-1):
            if zahl[ziffer1] == zahl[ziffer2]:
                liste.append([integer])
                for i in range(10):
                    zahl_neu = copy.copy(zahl)
                    zahl_neu[ziffer1] = str(i)
                    zahl_neu[ziffer2] = str(i)
                    zahl_neu = "".join(zahl_neu)
                    int_neu = int(zahl_neu)
                    if int_neu > integer:
                        liste[-1].append(int_neu)
    for ziffer1 in range(len(zahl)-1):  #drei ersetzen
        for ziffer2 in range(ziffer1+1, len(zahl)-1):
            for ziffer3 in range(ziffer2+1, len(zahl)-1):
                if zahl[ziffer1] == zahl[ziffer2] and zahl[ziffer2] == zahl[ziffer3]:
                    liste.append([integer])
                    for i in range(10):
                        zahl_neu = copy.copy(zahl)
                        zahl_neu[ziffer1] = str(i)
                        zahl_neu[ziffer2] = str(i)
                        zahl_neu[ziffer3] = str(i)
                        zahl_neu = "".join(zahl_neu)
                        int_neu = int(zahl_neu)
                        if int_neu > integer:
                            liste[-1].append(int_neu)
    for ziffer1 in range(len(zahl)-1):  #vier ersetzen
        for ziffer2 in range(ziffer1+1, len(zahl)-1):
            for ziffer3 in range(ziffer2+1, len(zahl)-1):
                for ziffer4 in range(ziffer3+1, len(zahl)-1):
                    if zahl[ziffer1] == zahl[ziffer2] and zahl[ziffer2] == zahl[ziffer3] and zahl[ziffer3] == zahl[ziffer4]:
                        liste.append([integer])
                        for i in range(10):
                            zahl_neu = copy.copy(zahl)
                            zahl_neu[ziffer1] = str(i)
                            zahl_neu[ziffer2] = str(i)
                            zahl_neu[ziffer3] = str(i)
                            zahl_neu = "".join(zahl_neu)
                            int_neu = int(zahl_neu)
                            if int_neu > integer:
                                liste[-1].append(int_neu)
    if len(zahl) > 5 and zahl[0] == zahl[1] and zahl[1] == zahl[2] and zahl[2] == zahl[3] and zahl[3] == zahl[4]: #fünf ersetzen
        liste.append([integer])
        for i in range(int(zahl[0]), 10):   
            int_neu = int(4*str(i)+str(zahl[-1]))
            if int_neu > integer and int_neu not in liste:
                liste[-1].append(int_neu)
    return liste

def rueckwaerts(integer):
    """bildet die Zahl, die entsteht, wenn man die Ziffern von integer von hinten nach vorne liest"""
    string = str(integer)
    liste = list(string)
    liste.reverse()
    string = ""
    for i in liste:
        string = string + i
    return int(string)

def lychrel(integer):
    """überprüft, ob eine Zahl eine Lychrel-Zahl ist
    Lychrel-Zahl: bildet addiert mit der Zahl rückwärts auch nach mind. 50 Wiederholungen kein Palindrom

    benötigt: palindrome, rueckwaerts
    """
    erg = 1
    for i in range(50):
        rueck = rueckwaerts(integer)
        integer = integer + rueck
        if palindrome(integer) == 1:
            erg = 0
            break
    return erg

def quersumme(integer):
    """bildet die Quersumme einer Zahl"""
    string = str(integer)
    summe = 0
    for ziffer in string:
        summe = summe + int(ziffer)
    return summe

def wurzel_2_kettenbruch(iterationen):
    """bildet über einen Algorithmus (1 + 1/(2 + 1/(2 + 1/(2 + ... )))) eine Näherung für Wurzel 2

    Ausgabe: Liste mit Lösungen für steigende Anzahl von Iterationen, jeweils als Bruch der Form [zähler, nenner]

    benötigt: kehrbruch, addieren"""
    x = [2, 1]
    liste = []
    summand = kehrbruch(x)
    for i in range(1, iterationen+1):
        x = addieren([2,1], summand)
        liste.append(x)
        summand = kehrbruch(addieren(summand, [2, 1]))
    return liste

def e_kettenbruch(iterationen):
    """berechnet eine Näherung für die Euler-Zahl e mittels eines Kettenbruchs

    Ausgabe als Bruch der Form [zähler, nenner]

    benötigt: kehrbruch, addieren"""
    vorfaktoren = [[2,1]]
    for i in range(iterationen-1):
        if i%3 == 0:
            vorfaktoren.append([1,1])
        elif i%3 == 1:
            vorfaktoren.append([2*(((i-1)/3+1)) ,1])
        elif i%3 == 2:
            vorfaktoren.append([1,1])
    k = vorfaktoren[-1]
    for i in range(2,iterationen+1):
        k = addieren(kehrbruch(k), vorfaktoren[-i])
    return [int(k[0]), int(k[1])]

def zahlen_rechts_oben(seitenlaenge):
    """gibt die Zahlen der Diagonalenhälfte rechts oben aus einer spiralförmigen Zahlenmatrix der Seitenlänge seitenlaenge als Liste aus (ohne 1)"""
    anzahl = int((seitenlaenge-1)/2)
    zahl = 1
    summand = 2
    zahlen = []
    for i in range(anzahl):
        zahl = zahl + summand
        zahlen.append(zahl)
        summand = summand + 8
    return zahlen

def zahlen_links_oben(seitenlaenge):
    """gibt die Zahlen der Diagonalenhälfte links oben aus einer spiralförmigen Zahlenmatrix der Seitenlänge seitenlaenge als Liste aus (ohne 1)"""
    anzahl = int((seitenlaenge-1)/2)
    zahl = 1
    summand = 4
    zahlen = []
    for i in range(anzahl):
        zahl = zahl + summand
        zahlen.append(zahl)
        summand = summand + 8
    return zahlen

def zahlen_links_unten(seitenlaenge):
    """gibt die Zahlen der Diagonalenhälfte links unten aus einer spiralförmigen Zahlenmatrix der Seitenlänge seitenlaenge als Liste aus (ohne 1)"""
    anzahl = int((seitenlaenge-1)/2)
    zahl = 1
    summand = 6
    zahlen = []
    for i in range(anzahl):
        zahl = zahl + summand
        zahlen.append(zahl)
        summand = summand + 8
    return zahlen

def zahlen_rechts_unten(seitenlaenge):
    """gibt die Zahlen der Diagonalenhälfte rechts unten aus einer spiralförmigen Zahlenmatrix der Seitenlänge seitenlaenge als Liste aus (ohne 1)"""
    anzahl = int((seitenlaenge-1)/2)
    zahl = 1
    summand = 8
    zahlen = []
    for i in range(anzahl):
        zahl = zahl + summand
        zahlen.append(zahl)
        summand = summand + 8
    return zahlen

def diagonale(seitenlaenge):
    """gibt die Zahlen beider Diagonalen (inkl. 1 in der Mitte) aus einer spiralförmigen Zahlenmatrix der Seitenlänge seitenlaenge als Liste aus (der Größe nach geordnet)"""
    zahlen = [1] + zahlen_rechts_oben(seitenlaenge) + zahlen_links_oben(seitenlaenge) + zahlen_links_unten(seitenlaenge) + zahlen_rechts_unten(seitenlaenge)
    zahlen.sort()
    return zahlen

def zusammensetzen(int1, int2):
    """setzt zwei Zahlen zusammen und gibt die zusammengesetzte Zahl zurück"""
    str1 = str(int1)
    str2 = str(int2)
    return int(str1 + str2)

def anzahl_ziffern(integer):
    """gibt die Anzahl der Ziffern einer Zahl zurück"""
    string = str(integer)
    return len(string)

def periodenlaenge_kettenbruch_wurzel(integer):
    """formt eine Quadratwurzel in einen Kettenbruch um und gibt die Länge des periodischen Teils aus

    benötigt: math, ggt_3
    """
    v = int(math.sqrt(integer))
    q = [1, 1, v]
    reihe = [v]
    qs = [q]
    while True:
        v = int(q[0] / (q[1]*math.sqrt(integer) - q[2]))
        reihe.append(v)
        a = q[1]**2 * integer - q[2]**2
        z = q[0]*q[1]
        b = v * (q[1]**2 * integer - q[2]**2) - q[0]*q[2]
        grgt = ggt_3(a,z,b)
        q = [a/grgt, z/grgt, b/grgt]
        if q in qs:
            #reihe_v = []                  # nicht periodischer Teil
            #for i in range(qs.index(q)+1):
                #reihe_v.append(reihe[i])
            reihe_n = []                   # periodischer Teil
            for i in range(qs.index(q)+1, len(reihe)):
                reihe_n.append(reihe[i])
            break
        qs.append(q)
    return len(reihe_n)

def naeherung_kettenbruch_wurzel(integer, iterationen):
    """berechnet eine Näherung von Wurzel von integer mittels eines Kettenbruchs

    Ausgabe als Bruch der Form [zähler, nenner]

    benötigt: kehrbruch, addieren, math, ggt_3
    """
    v = int(math.sqrt(integer))
    q = [1, 1, v]
    reihe = [[v,1]]
    qs = [q]
    for i in range(iterationen-1):
        v = int(q[0] / (q[1]*math.sqrt(integer) - q[2]))
        reihe.append([v,1])
        a = q[1]**2 * integer - q[2]**2
        z = q[0]*q[1]
        b = v * (q[1]**2 * integer - q[2]**2) - q[0]*q[2]
        grgt = ggt_3(a,z,b)
        q = [a/grgt, z/grgt, b/grgt]
    k = reihe[-1]
    for i in range(2,iterationen+1):
        k = addieren(kehrbruch(k), reihe[-i])
    return [int(k[0]), int(k[1])]

def eulers_phi(integer):
    """gibt eine Liste aller Werte für die Euler'sche Phi-Funktion (Anzahl von teilerfremden Zahlen < Zahl) von 0-integer aus

    benötigt: kl_teiler
    """
    phi = [0, 1]
    for i in range(2, integer+1):
        teil = kl_teiler(i)
        if teil == i:     # Primzahl
            phi.append(i-1)
        else:
            sec_teiler = int(i/teil)
            if sec_teiler%teil != 0:            # Produkt aus teilerfremden Zahlen (kleinster Teiler dabei)
                phi.append(phi[teil]*phi[int(i/teil)])
            else:
                teil_n = teil
                teil_v = 1
                while sec_teiler%teil_n == 0 and sec_teiler != teil:
                    teil_v = teil_n*teil_v
                    teil_n = kl_teiler(sec_teiler)
                    sec_teiler = int(i/(teil_v*teil_n))
                if sec_teiler == teil:          # Potenz von Primzahl
                    phi.append(int(i*(1-1/teil)))
                else:                              # Produkt aus teilerfremden Zahlen
                    phi.append(phi[teil_n*teil_v]*phi[sec_teiler])
    return phi

def fac_digits_sum(integer):
    """berechnet sie Summe aus den Fakultäten der einzelnen Ziffern

    benötigt: Liste faks mit Fakultäten von 0 - 9"""
    string = str(integer)
    erg = 0
    for i in string:
        erg = erg + faks[int(i)]
    return erg

def len_fac_digits_sum(integer):
    """berechnet die Länge der Kette, die entsteht, wenn man von jedem Glied die Summe aus den Fakultäten der einzelnen Ziffern berechnet, bis sich eine Zahl wiederholt

    benötigt: fac_digits_sum
    """
    erg = 0
    while integer != 145 and integer != 169 and integer != 40585 and integer != 363601 and integer != 1454 and integer != 871 and integer != 45361 and integer != 872 and integer != 45362 and integer != 1 and integer != 2:
        integer = fac_digits_sum(integer)
        erg = erg+1
    if integer == 145 or integer == 1 or integer == 2 or integer == 40585:
        erg = erg+1
    elif integer == 169 or integer == 363601 or integer == 1454:
        erg = erg+3
    elif integer == 871 or integer == 45361 or integer == 872 or integer == 45362:
        erg = erg+2
    return erg

def create_products(summe):
    """gibt alle möglichen Produkte zweier Zahlen zurück, deren Summe summe ist"""
    erg = []
    for i in range(1, int(summe/2)+1):
        erg.append(i*(summe-i))
    return erg

def create_sums(product):
    """gibt alle möglichen Summen zweier Zahlen zurück, deren Produkt product ist

    benötigt: math"""
    i = 2
    teiler = [1 + product]
    while i <= math.sqrt(product):
        if product%i == 0:
            teiler.append(int(i + product/i))
        i = i + 1
    return teiler

def partitions(n,k):
    """gibt die Anzahl an Möglichkeiten zurück, die Zahl n als Summe von k Summanden darzustellen

    Methode: https://de.wikipedia.org/wiki/Partitionsfunktion"""
    if k == 1:
        return 1
    elif k == 0 or n == 0:
        return 0
    elif k > n:
        return 0
    else:
        return partitions(n-k,k) + partitions(n-1,k-1)

def partitions_sum(n):
    """gibt die Anzahl an Möglichkeiten zurück, die Zahl n als Summe darzustellen (inkl. der Zahl selbst)

    benötigt: partitions"""
    erg = 0
    for i in range(1,n+1):
        erg = erg + partitions(n,i)
    return erg

def nextnumber(s):
    """gibt fuer eine Zahl, die als String eingegeben wird, die naechste Zahl der Folge "Look and Say sequence" (https://oeis.org/A005150) ebenfalls als String aus
    Beispiel: 21 -> 1211
    """

    liste = []
    part = ""
    for i in range(len(s)):
        if len(part) == 0 or s[i] == part[-1]:
            part = part + s[i]
            if i == len(s)-1:
                liste.append(part)
        else:
            liste.append(part)
            part = s[i]
            if i == len(s)-1:
                liste.append(part)
    newnumber = ""
    for l in liste:
        newnumber = newnumber + str(len(l)) + l[0]
    return newnumber
