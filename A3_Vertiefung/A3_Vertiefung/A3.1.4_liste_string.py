# A3.14 Liste Städte sortieren
# Ergebnis = [ ["Essen", "E"], ["Dortmund", "DO"], ["Wuppertal", "W"] ]
Stadte = ["Essen", "Dortmund", "Wuppertal"]
Kfz = ["E", "DO", "W"]
Ergebnis = []
laenge = len(Kfz) # Return the length (the number of items)
for i in range(laenge):
    Ergebnis.append([Stadte[i],Kfz[i]]) #hinzufügen
    print(Ergebnis)
 # Analsyse
 # 1. array anlegen 2. anzahl geg. werte als array indizes
 # 3. for Schleife -> solange index geg. werte läuft folgendes tun:
 # 4. array 'Ergebnis' hinzufügen von Container Staedte und Kfz