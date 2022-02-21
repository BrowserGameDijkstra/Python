#  Funktion Liste sortiert minimum aus und fügt dann grösse nach neue Liste. nicht Methode sort() verwenden!
# Pseudocode Lsg
"""
1. Originalliste ausgeben
2. leere Ergebnisliste erstellen
3. Algorithmus
- durchsuche Orig.Liste nach minimum und gib die Zahl in ErgebL aus (while)
- lösche dann minimum
- repeat bis Originalliste leer
4. Ausgabe ErgebnisL
"""
OrgListe = [45, 23, 12.5, 2, 119.23, 44]
ErgListe = []
while len(OrgListe)!=0:
    minimum = min(OrgListe)
    ErgListe.append(minimum)
    OrgListe.remove(minimum)
    print(ErgListe)


