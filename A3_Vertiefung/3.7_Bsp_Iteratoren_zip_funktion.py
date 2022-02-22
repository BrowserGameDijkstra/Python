# mehrere Listen gleichzeitig zu durchlaufen. iter()­Funktion erzeugt für die vorgegebene
# Liste einen Iterator k.Aufruf Methode next() nächste Element der Liste zurückgegeben
# ein und dieselbe Liste können durchaus mehrere Iteratoren erzeugt werden. Ebenso können mehrere
# Listen mittels Iteratoren gleichzeitig durchlaufen werden.
Staedte = ["Essen","Dortmund","Wuppertal"]
k = iter(Staedte)
next(k)
next(k)
next(k)
# Bsp zusammenführung 2 Listen in Tupel
"""Pseudo
1. Tupel array ertellen
2. Liste 2 als iter deklarieren
"""

Staedte = ["Essen", "Dortmund", "Wuppertal"]
Kfz = ["E", "DO", "W"]
Liste = []
k = iter(Kfz)
for s in Staedte:
    t = next(k)
    Liste.append( (s,t))
print(Liste)

# Standardfunktion namens zip(). Damit wird weder eine Schleife noch ein Iterator benötigt
Staedte = ["Essen", "Dortmund", "Wuppertal"]
Kfz = ["E", "DO", "W"]
Ergebnis = zip(Staedte,Kfz)
list(Ergebnis)
print(Ergebnis)