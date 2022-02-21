# A3.1   drei   Listen für Ganzzahlen, Gleitpunktzahlen Zeichenketten
werte = [12, 22, 'Wuppertal', 34.5, "Solingen", 102.45, 103, 12.3, 45]
# zunächst 3 leere Listen anlegen
Ganzzahlen = []
Gleitpunktzahlen = []
Zeichenketten = []

for x in werte:
    if type(x) == int:
        Ganzzahlen.append(x)
    elif type(x) == float:
        Gleitpunktzahlen.append(x)
    elif type(x) == str:
        Zeichenketten.append(x)
print()
print(Ganzzahlen)
print(Gleitpunktzahlen)
print(Zeichenketten)
