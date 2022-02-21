# A3.4.1 Dictionary unter Verwendung einer Programmschleife
"""Pseudo
1. dict array erzeugen
2. elemente per len definieren
3. überführen der listen aus Staedte und Post. in dict arry per len
   und for loop
"""
Postleitzahlen = [42097,45289,44137]
Staedte = ["Wuppertal","Essen","Dortmund"]
plz = {}
laenge = len(Staedte)
for i in range(laenge):
    plz[Postleitzahlen[i]] = Staedte[i]
    print(plz)
# A3.4.2  Programmschleife löschen   Schlüssel ohne Rest durch drei teilbar
"""Pseudo
1. dict array erzeugen
2. for Schleife erzeugt ^2 Zahlen
3. ^2 ausgeben
4. liste = list(Quadrat.keys()) 
"""
# Quadrat = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
Quadrat = {}
# laenge = len(Quadrat)
# print(laenge)
for i in range(11): # gibt die Zaheln von 0 bis 10 aus
     Quadrat[i] = i**2
print(Quadrat)
liste = list(Quadrat.keys())
for i in liste:
    if i%3==0:
       del Quadrat[i]
print(Quadrat)