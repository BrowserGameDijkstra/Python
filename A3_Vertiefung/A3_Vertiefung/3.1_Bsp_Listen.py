# Basis Listen
a = [1,3,5,7,9]
b = [2,"Hallo!", 12.5]
c = [[2,4], ['a','b']]
print(a[0], a[3])
print(b[1])
print(c[1], c[1][1])

# Operator in ob ein Element in einer Liste enthalten ist oder nicht
moegliche_farben = ["rot", "grün", "blau"]
farbe = input("Bitte Farbe eingeben: ")
if farbe not in moegliche_farben:
    print("Diese Farbe ist nicht enthalten!")

# Listenelemente ausgegeben
moegliche_farben = ["rot", "grün", "blau"]
for i in moegliche_farben:
    print(i)

# Index eines Listenelements Listenmethode index()
moegliche_farben = ["rot", "grün", "blau"]
for i in moegliche_farben:
    j = moegliche_farben.index(i)
    print(j,i)  # 0 rot 1 grün 2 blau

# Methoden sort() und reverse() benutzt.
inhalt = [ 5,23,45,15,22,54]
print(inhalt)
inhalt.sort()
print(inhalt)
inhalt.reverse()
print(inhalt)

# Methoden index(), remove() und append()
#
inhalt = [ 23.5, 12, [19, "Hallo"], 12, 45]
print(inhalt)
inhalt.append(100) # hinzufügen
print(inhalt)
inhalt[2].append(200)
print(inhalt)
anzahl = inhalt.count(12) # zählt wie oft 12 vorkommt
print(anzahl)
inhalt.remove(23.5) # entfernt
print(inhalt)
ind = inhalt.index(45) # Index der Zahl
print(ind)
inhalt.insert(3,7)
print(inhalt)

# Operatoren +verketten  und * Listen n-fach wiederholen
Liste1 = [1,2,3]
Liste2 = [3,4,5]
Ergebnis = Liste1+Liste2
print(Ergebnis)
E = 4*Liste2
print(E)

# Überschreiben von Listenelementen
# – Zugriff auf das letzte Listenelement
Liste1 = [10,20,40,70]
Liste1[2]=-45
Liste1[-1] = 90
print(Liste1)

# Ermittlung des Maximums und des Minimums in einer Liste
Liste1 = [10,20,40,70]
max(Liste1)
min(Liste1)
Orte = ["Xanten", "Essen", "Aachen", "Wuppertal"]
min(Orte) #  "Aachen"
max(Orte) # "Xanten"